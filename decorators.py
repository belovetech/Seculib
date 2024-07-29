import os
from functools import wraps
from flask import request, jsonify
import jwt

SECRET_KEY = os.getenv('SECRET_KEY')

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        bearerToken = request.headers.get('Authorization')
        if not bearerToken:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            token = bearerToken.split(' ')[1]
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.PyJWTError:
            return jsonify({'message': 'Token is invalid!'}), 401

        request.user_data = data  # Store user data in request for access in the route
        return f(*args, **kwargs)

    return decorated_function
