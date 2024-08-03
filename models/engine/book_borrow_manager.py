

from models.book import  BorrowedBook

class BorrowManager:

    def __init__(self, db):
        self.db = db

    def get_all_borrowed_books(self):
        return self.db.session.query(BorrowedBook).all()

    def get_borrowed_book_by_id(self, borrowed_book_id):
        return self.db.session.query(BorrowedBook).filter(BorrowedBook.id == borrowed_book_id).first()

    def add_borrowed_book(self, borrowed_book):
        self.db.session.add(borrowed_book)
        self.db.session.commit()

    def update_borrowed_book(self, borrowed_book):
        self.db.session.commit()

    def delete_borrowed_book(self, borrowed_book):
        self.db.session.delete(borrowed_book)
        self.db.session.commit()

