import uuid
import datetime
from models.student import  Session

class SessionManager:

    def __init__(self, db):
        self.db = db


    def create_session(self, student_id, expiry_at):
        try:
            session = self.get_session_by_student_id(student_id)
            if session:
                session_id = session['id']
                self.delete_session(session_id)

            session_id = str(uuid.uuid4())
            created_at = datetime.datetime.now()
            session = Session(id=session_id, student_id=student_id, created_at=created_at, expiry_at=expiry_at)
            self.db.session.add(session)
            self.db.session.commit()
            return session_id
        except Exception as e:
            print("Create session error: ", e)
            self.db.session.rollback()
            return

    def get_session_by_student_id(self, student_id):
        session = self.db.session.query(Session).filter(Session.student_id == student_id).first()
        if session:
            return session.__dict__
        return None

    def get_session_by_session_id(self, session_id):
        session = self.db.session.query(Session).filter(Session.id == session_id).first()
        if session:
            del session.__dict__['_sa_instance_state']
            return session.__dict__
        return None

    def delete_session(self, session_id):
        return Session.query.filter_by(id=session_id).delete()






