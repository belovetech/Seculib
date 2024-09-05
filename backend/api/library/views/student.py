import os
from flask import  jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from api.library.views import app_views
from models.engine.db import db
from models.engine.student_manager import StudentManager
from helpers.decorators import token_required, rate_limiter


SECRET_KEY = os.getenv('SECRET_KEY')
student_manager = StudentManager(db)


@app_views.route('students/register', methods=['POST'])
def register():
    try:
        data = request.get_json()

        if not data:
            return jsonify({'message': 'Missing data!'}), 400

        if 'name' not in data:
            return jsonify({'message': 'name is required'}), 400

        if 'matric_no' not in data:
            return jsonify({'message': 'matric_no is required'}), 400

        if 'department' not in data:
            return jsonify({'message': 'department is required'}), 400

        if 'level' not in data:
            return jsonify({'message': 'level is required'}), 400

        if 'password' not in data:
            return jsonify({'message': 'password is required'}), 400


        student_with_matric_no_exists = student_manager.get_student_by_matric_no(data['matric_no'])

        if student_with_matric_no_exists:
            return jsonify({'message': 'User already exists!'}), 409

        student =  student_manager.register_student(
            name=data['name'],
            matric_no=data['matric_no'],
            department=data['department'],
            level=data['level'],
            password=generate_password_hash(data['password'])
        )
        return jsonify({'message': 'Student registered successfully!', 'data':student}), 201
    except KeyError as e:
        print(e)
        return jsonify({'message': 'Missing data!'}), 400
    except Exception as e:
        print(e)
        return jsonify({'message': 'An error occurred!'}), 500

@app_views.route('students/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        if not data:
            return jsonify({'message': 'Missing data!'}), 400

        if 'matric_no' not in data:
            return jsonify({'message': 'matric_no is required'}), 400

        if 'password' not in data:
            return jsonify({'message': 'password is required'}), 400

        token = student_manager.login_student(
            matric_no=data['matric_no'],
            password=data['password']
        )

        if not token:
            return jsonify({'message': 'Invalid credentials!'}), 401

        return jsonify({'message': 'Logged in!', 'data': {'token':token}}), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred!'}), 500


@app_views.route('students/profile', methods=['GET'])
@token_required
def profile():
    try:
        data = request.student_data

        student = student_manager.get_student_by_matric_no(data['metric_no'])
        del student['password'] # Remove password from the response

        return jsonify({'data': student, "message": "Student profile fetched successfully"}), 200
    except Exception as e:
        print(e)
        return jsonify({'message': 'An error occurred!'}), 500


@app_views.route('students', methods=['GET'])
def get_students():
    try:
        students = student_manager.get_all_students()
        return jsonify({'data': students, "message": "Students fetched successfully"}), 200
    except Exception as e:
        print(e)
        return jsonify({'message': 'An error occurred!'}), 500
