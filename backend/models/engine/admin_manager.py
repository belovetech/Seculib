from models.book import Book, BorrowedBook
from models.student import Student, Session


class AdminManager:
    def __init__(self, db):
        self.db = db

    def statistics(self):
        try:
            students = self.db.session.query(Student).filter(
                Student.role == 'student').count()
            admins = self.db.session.query(Student).filter(
                Student.role == 'admin').count()
            available_books = self.db.session.query(Book).count()
            borrowed_books = self.db.session.query(BorrowedBook).count()
            sessions = self.db.session.query(Session).count()

            return {
                'admins': admins,
                'students': students,
                'available_books': available_books,
                'borrowed_books': borrowed_books,
                'logged_in_users': sessions,
            }
        except Exception as e:
            print(e)
            return None
        finally:
            self.db.session.close()
