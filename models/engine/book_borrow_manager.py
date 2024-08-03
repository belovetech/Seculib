import uuid
from models.book import  BorrowedBook, Book

class BorrowBookManager:

    def __init__(self, db):
        self.db = db

    def borrow_book(self, **kwargs):
        try:
            book = self.db.session.query(Book).filter(Book.id == kwargs['book_id']).first()
            if not book.available:
                return None

            print('kwargs: ', kwargs)
            kwargs['id'] = str(uuid.uuid4())
            borrowed_book = BorrowedBook(**kwargs)
            self.db.session.add(borrowed_book)
            self.db.session.commit()

            #ser book as unavailable
            self.set_book_available(kwargs['book_id'])
            return borrowed_book
        except Exception as e:
            print("Borrow book error: ", e)
            self.db.session.rollback()
            raise e

    def get_borrowed_books(self):
        borrowed_books = self.db.session.query(BorrowedBook).all()
        if borrowed_books:
            borrowed_books = [borrowed_book.__dict__ for borrowed_book in borrowed_books]
            return borrowed_books
        return None


    def get_book_borrowed_by_student(self, student_id):
        borrowed_books = self.db.session.query(BorrowedBook).filter(BorrowedBook.student_id == student_id).all()
        if borrowed_books:
            borrowed_books = [borrowed_book.__dict__ for borrowed_book in borrowed_books]
            return borrowed_books
        return None

    def return_book(self, borrowed_book):
        try:
            self.db.session.delete(borrowed_book)
            self.db.session.commit()
            return True
        except Exception as e:
            print("Return book error: ", e)
            self.db.session.rollback()
            return False

    def set_book_available(self, book_id):
        try:
            book = self.db.session.query(Book).filter(Book.id == book_id).first()
            book.available = not book.available
            self.db.session.commit()
            return True
        except Exception as e:
            print("Set book available error: ", e)
            self.db.session.rollback()
            return False
