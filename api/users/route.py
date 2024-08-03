import jwt
import os
import datetime
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models.user_manager import UserManager
from  models.session_manager import sessionManager
from helpers.decorators import token_required
from api import app_views


SECRET_KEY = os.getenv('SECRET_KEY')

# Initialize the user manager
db_name = 'users.db'
user_manager = UserManager(db_name)
session_manager = sessionManager(db_name)

@app_views.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data:
        return jsonify({'message': 'Missing data!'}), 400

    if 'full_name' not in data:
        return jsonify({'message': 'full_name is required'}), 400

    if 'matric_no' not in data:
        return jsonify({'message': 'matric_no is required'}), 400

    if 'password' not in data:
        return jsonify({'message': 'password is required'}), 400

    full_name = data['full_name']
    matric_no = data['matric_no']
    password = generate_password_hash(data['password'])

    user_with_matric_no_exists = user_manager.get_user_by_matric_no(matric_no)

    if user_with_matric_no_exists:
        return jsonify({'message': 'User already exists!'}), 400

    user_manager.create_user(full_name, matric_no, password)

    return jsonify({'message': 'Registered successfully!'}), 201

@app_views.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        if not data:
            return jsonify({'message': 'Missing data!'}), 400

        if 'matric_no' not in data:
            return jsonify({'message': 'matric_no is required'}), 400

        if 'password' not in data:
            return jsonify({'message': 'password is required'}), 400

        matric_no = data['matric_no']
        password = data['password']

        user = user_manager.get_user_by_matric_no(matric_no)

        if not user or not check_password_hash(user['password'], password):
            return jsonify({'message': 'Invalid credentials!'}), 401

        expires_at = datetime.datetime.now() + datetime.timedelta(hours=1)
         # Create a session for the user
        session_id = session_manager.create_session(user['id'], expires_at)

        token = jwt.encode({
            'user': matric_no,
            'exp': expires_at,
            'session_id': session_id
        }, SECRET_KEY)

        return jsonify({'message': 'Logged in!', 'data': {'token':token}}), 200
    except Exception as e:
        print(e)
        return jsonify({'message': 'An error occurred!'}), 500


@app_views.route('/profile', methods=['GET'])
@token_required
def profile():
    try:
        data = request.user_data



        user = user_manager.get_user_by_matric_no(data['user'])
        del user['password'] # Remove password from the response

        return jsonify({'data': user, "message": "User profile"}), 200
    except Exception as e:
        print(e)
        return jsonify({'message': 'An error occurred!'}), 500



# @app.route('/protected', methods=['GET'])
# @token_required
# def protected():
#     return jsonify({'message': 'You are in!'})

# @app.route('/unprotected', methods=['GET'])
# def unprotected():
#     return jsonify({'message': 'You are in!'})
