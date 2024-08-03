
from models.book import Book

class BookManager:
    def __init__(self, db):
        self.db = db

    def get_all_books(self):
        return self.db.session.query(Book).all()

    def get_book_by_id(self, book_id):
        return self.db.session.query(Book).filter(Book.id == book_id).first()

    def add_book(self, **kwargs):
        book = Book(**kwargs)
        self.db.session.add(book)
        self.db.session.commit()

    def update_book(self, book):
        self.db.session.commit()

    def delete_book(self, book):
        self.db.session.delete(book)
        self.db.session.commit()

