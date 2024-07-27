from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import jwt
import os
import datetime


app = Flask(__name__)

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

users = {}


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
    username = data['username']
    password = generate_password_hash(data['password'])

    if username in users:
        return jsonify({'message': 'User already exists!'}), 400

    users[username] = password

    print(users)
    return jsonify({'message': 'Registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if username not in users or not check_password_hash(users[username], password):
        return jsonify({'message': 'Invalid credentials!'}), 401

    token = jwt.encode({
        'user': username,
        'exp': datetime.datetime.now() + datetime.timedelta(hours=1)
    }, SECRET_KEY)

    return jsonify({'token': token})

if __name__ == '__main__':
    app.run(debug=True)
