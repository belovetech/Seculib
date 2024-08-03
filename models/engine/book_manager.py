
from models.book import Book

class BookManager:
    def __init__(self, db):
        self.db = db

    def add_book(self, **kwargs):
        """Add a book to the library"""
        try:
            book = Book(**kwargs)
            self.db.session.add(book)
            self.db.session.commit()
            return book.__dict__
        except Exception as e:
            print("Add book error: ", e)
            self.db.session.rollback()
            return None

    def get_all_books(self, **kwargs):
        try:
            book_objs = []
            books = self.db.session.query(Book).all()
            for book in books:
                book = book.__dict__.copy()
                book.pop('_sa_instance_state')
                book_objs.append(book)
            return book_objs
        except Exception as e:
            print("Get books error: ", e)
            return book_objs


    def get_book_by_id(self, book_id):
        book =  self.db.session.query(Book).filter(Book.id == book_id).first()
        if book:
            book = book.__dict__.copy()
            book.pop('_sa_instance_state')
            return book
        return None

    def update_book(self, book_id,  **kwargs):
        try:
            book = self.get_book_by_id(book_id)
            if not book:
                return False
            for key, value in kwargs.items():
                setattr(book, key, value)
            self.db.session.commit()
            return True
        except Exception as e:
            print("Update book error: ", e)
            self.db.session.rollback()
            return False

    def delete_book(self, book):
        try:
            self.db.session.delete(book)
            self.db.session.commit()
            return True
        except Exception as e:
            print("Delete book error: ", e)
            return False

