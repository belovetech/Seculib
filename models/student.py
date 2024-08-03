from models.engine.db import db

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.String(25), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    matric_no = db.Column(db.String(20), nullable=False, unique=True)
    department = db.Column(db.String(55), nullable=False)
    level = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    # Relationships
    sessions = db.relationship('Session', backref='student', lazy=True)
    borrowed_books = db.relationship('BorrowedBook', backref='student', lazy=True)


class Session(db.Model):
    __tablename__ = 'sessions'

    id = db.Column(db.String(25), primary_key=True)
    student_id = db.Column(db.String(25), db.ForeignKey('students.id'))
    created_at = db.Column(db.DateTime)
    expiry_at = db.Column(db.DateTime)
