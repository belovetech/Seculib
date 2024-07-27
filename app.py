from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import jwt
import os
import datetime
from user_manager import UserManager


app = Flask(__name__)

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

# users = {}

user_manager = UserManager('users.db')


@app.route('/healthz', methods=['GET'])
def healthz():
    return jsonify({'message': 'OK'})

@app.route('/protected', methods=['GET'])
def protected():
    bearerToken = request.headers.get('Authorization')
    if not bearerToken:
        return jsonify({'message': 'Token is missing!'}), 401

    try:
        token = bearerToken.split(' ')[1]
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.PyJWTError as e:
        print(e)
        return jsonify({'message': 'Token is invalid!'}), 401


    return jsonify({'message': 'You are in!'})

@app.route('/unprotected', methods=['GET'])
def unprotected():
    return jsonify({'message': 'You are in!'})

@app.route('/register', methods=['POST'])
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

@app.route('/login', methods=['POST'])
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

        token = jwt.encode({
            'user': matric_no,
            'exp': datetime.datetime.now() + datetime.timedelta(hours=1)
        }, SECRET_KEY)

        return jsonify({'message': 'Logged in!', 'data': {'token':token}}), 200
    except Exception as e:
        print(e)
        return jsonify({'message': 'An error occurred!'}), 500



#get user profile
@app.route('/profile', methods=['GET'])
def profile():
    try:
        bearerToken = request.headers.get('Authorization')
        if not bearerToken:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            token = bearerToken.split(' ')[1]
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.PyJWTError as e:
            print(e)
            return jsonify({'message': 'Token is invalid!'}), 401

        user = user_manager.get_user_by_matric_no(data['user'])
        del user['password'] # Remove password from the response

        return jsonify({'data': user, "message": "User profile"}), 200
    except Exception as e:
        print(e)
        return jsonify({'message': 'An error occurred!'}), 500

if __name__ == '__main__':
    app.run(debug=True)
