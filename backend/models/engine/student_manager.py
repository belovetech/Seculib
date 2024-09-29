import os
import datetime
import jwt
import uuid
from werkzeug.security import check_password_hash
from models.student import Student
from models.engine.session_manager import SessionManager

SECRET_KEY = os.getenv('SECRET_KEY')


class StudentManager(SessionManager):
    def __init__(self, db):
        self.db = db

    def register_student(self, **kwargs):
        try:
            kwargs['id'] = str(uuid.uuid4())
            student = Student(**kwargs)
            self.db.session.add(student)
            self.db.session.commit()

            return self.create_token(student_id=student.id, matric_no=student.matric_no)
        except Exception as e:
            print("Add student error: ", e)
            self.db.session.rollback()
            raise e

    def create_admin(self, **kwargs):
        try:
            kwargs['id'] = str(uuid.uuid4())
            admin = Student(**kwargs)
            self.db.session.add(admin)
            self.db.session.commit()

            return self.create_token(student_id=admin.id, matric_no=admin.matric_no)
        except Exception as e:
            print("Add admin error: ", e)

    def login_student(self, **kwargs):
        try:
            password = kwargs['password']
            matric_no = kwargs['matric_no']

            student = self.db.session.query(Student).filter(
                Student.matric_no == matric_no).first()
            if not student or not check_password_hash(student.password, password):
                raise Exception('Invalid credentials!', 401)

            token = self.create_token(
                student_id=student.id, matric_no=matric_no, role=student.role)
            is_admin = self.is_admin(student.id)

            return {'token': token, 'is_admin': is_admin}
        except Exception as e:
            print("Login student error: ", e)
            return None

    def get_all_students(self, **kwargs):
        try:
            student_objs = []
            students = self.db.session.query(Student).filter(
                Student.role != 'admin').all()
            print(students)
            for student in students:
                student = student.__dict__.copy()
                student.pop('_sa_instance_state')
                student.pop('password')
                student_objs.append(student)
            return student_objs
        except Exception as e:
            print("Get students error: ", e)
            return student_objs

    def get_student_by_id(self, student_id):
        student = self.db.session.query(Student).filter(
            Student.id == student_id).first()
        if student:
            student = student.__dict__.copy()
            student.pop('_sa_instance_state')
            student.pop('password')
            return student
        return None

    def get_student_by_matric_no(self, matric_no):
        student = self.db.session.query(Student).filter(
            Student.matric_no == matric_no).first()
        if student:
            student = student.__dict__.copy()
            student.pop('_sa_instance_state')
            return student
        return None

    def create_token(self, **kwargs):
        student_id = kwargs['student_id']
        expires_at = datetime.datetime.now() + datetime.timedelta(hours=1)

        try:
            session_id = self.create_session(student_id, expires_at)
            token = jwt.encode({
                'metric_no': kwargs['matric_no'],
                'exp': expires_at,
                'session_id': session_id,
                'student_id':  student_id,
                'role': kwargs['role']
            }, SECRET_KEY)

            return token
        except Exception as e:
            print("Create token error: ", e)
            return None

    def is_admin(self, student_id):
        student = self.db.session.query(Student).filter(
            Student.id == student_id).first()
        if student:
            return student.role == 'admin'
        return False
