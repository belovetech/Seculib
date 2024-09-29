#  Create a table to store the request statistics, such that admin can view the number of requests made by legitimate students and the number of requests made by malicious students or attackers

from models.engine.db import db


class RequestStatistics(db.Model):
    __tablename__ = 'request_statistics'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.String(25), db.ForeignKey('students.id'))
    request_type = db.Column(db.String(25), nullable=False)
    request_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())

    def __init__(self, student_id, request_type, request_count):
        self.student_id = student_id
        self.request_type = request_type
        self.request_count = request_count

    def __repr__(self):
        return f'<RequestStatistics {self.id}>'
