import os
from functools import wraps
from flask import request, jsonify
import jwt
from models.engine.session_manager import SessionManager
from models.engine.db import db


SECRET_KEY = os.getenv('SECRET_KEY')
session_manager = SessionManager(db)

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        bearerToken = request.headers.get('Authorization')
        if not bearerToken:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            token = bearerToken.split(' ')[1]
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            session_id = data['session_id']
            session = session_manager.get_session_by_session_id(session_id)
            if session is None:
                return jsonify({'message': 'Session expired or you have logged in with another browser. Kindly login to create a new session'}), 401
        except jwt.PyJWTError:
            return jsonify({'message': 'Token is invalid!'}), 401

        request.student_data = data  # Store user data in request for access in the route
        return f(*args, **kwargs)

    return decorated_function
