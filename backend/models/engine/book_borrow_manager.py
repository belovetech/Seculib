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

            kwargs['id'] = str(uuid.uuid4())
            borrowed_book = BorrowedBook(**kwargs)
            self.db.session.add(borrowed_book)
            self.db.session.commit()

            #ser book as unavailable
            self.set_book_unavailable(kwargs['book_id'])
            return True
        except Exception as e:
            print("Borrow book error: ", e)
            self.db.session.rollback()
            raise e

    def get_book_borrowed_by_student(self, student_id):
        try:
            objs = []
            borrowed_books = self.db.session.query(BorrowedBook).filter(BorrowedBook.student_id == student_id).all()
            for borrowed_book in borrowed_books:
                borrowed_book = borrowed_book.__dict__.copy()
                borrowed_book.pop('_sa_instance_state')
                book = self.db.session.query(Book).filter(Book.id == borrowed_book['book_id']).first()
                borrowed_book['book'] = book.__dict__
                borrowed_book['book'].pop('_sa_instance_state')
                borrowed_book['book'].pop('available')
                objs.append(borrowed_book)
            return objs
        except Exception as e:
            print("Get borrowed books error: ", e)
            return objs

    def get_borrowed_book_by_id(self, borrowed_book_id):
        """Get a book by its id"""
        borrowd_book =  self.db.session.query(BorrowedBook).filter(BorrowedBook.book_id == borrowed_book_id).first()
        print("Borrowed book: ", borrowd_book)
        if borrowd_book:
            borrowd_book = borrowd_book.__dict__.copy()
            borrowd_book.pop('_sa_instance_state')
            return borrowd_book
        return None

    def return_book(self, borrowed_book_id):
        try:
            self.db.session.query(BorrowedBook).filter(BorrowedBook.book_id == borrowed_book_id).delete()
            self.db.session.commit()
            self.set_book_available(borrowed_book_id)
            return True
        except Exception as e:
            print("Return book error: ", e)
            self.db.session.rollback()
            return False

    def set_book_available(self, book_id):
        try:
            book = self.db.session.query(Book).filter(Book.id == book_id).first()
            book.available = True
            self.db.session.commit()
            return True
        except Exception as e:
            print("Set book available error: ", e)
            self.db.session.rollback()
            return False

    def set_book_unavailable(self, book_id):
        try:
            book = self.db.session.query(Book).filter(Book.id == book_id).first()
            book.available = False
            self.db.session.commit()
            return True
        except Exception as e:
            print("Set book unavailable error: ", e)
            self.db.session.rollback()
            return False
