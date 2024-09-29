import os
from functools import wraps
from flask import request, jsonify
import jwt
from models.engine.session_manager import SessionManager
from helpers.middlewares import RateLimitMiddleware
from models.engine.db import db


SECRET_KEY = os.getenv('SECRET_KEY')
session_manager = SessionManager(db)


def is_authenticated():
    bearerToken = request.headers.get('Authorization')
    if not bearerToken:
        return False
    try:
        token = bearerToken.split(' ')[1]
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return data
    except jwt.PyJWTError:
        return False


def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            data = is_authenticated()
            if not data:
                return jsonify({'message': 'Token is missing, invalid or expired!'}), 401
            session_id = data['session_id']
            session = session_manager.get_session_by_session_id(session_id)
            if session is None:
                return jsonify({'message': 'Session expired or you have logged in with another browser. Kindly login to create a new session'}), 401
        except jwt.PyJWTError:
            return jsonify({'message': 'Token is invalid!'}), 401

        request.student_data = data  # Store user data in request for access in the route
        return f(*args, **kwargs)

    return decorated_function


def rate_limiter(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        client_ip = request.remote_addr
        authenticated_requests_per_minute = 100
        unauthenticated_requests_per_minute = 3
        time_window = 60
        endpoint = request.path

        if not is_authenticated():
            rate_limit = RateLimitMiddleware(
                rate_limit=unauthenticated_requests_per_minute, time_window=time_window)
        else:
            rate_limit = RateLimitMiddleware(
                rate_limit=authenticated_requests_per_minute, time_window=time_window)

        if rate_limit.is_rate_limited(client_ip, endpoint):
            return jsonify({"error": "Too many requests"}), 429
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        role = request.student_data['role']
        if role != 'admin':
            return jsonify({'message': 'You are not authorized to access this endpoint'}), 403
        return f(*args, **kwargs)
    return decorated_function
