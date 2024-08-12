from models.engine.db import db

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.String(25), primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    available = db.Column(db.Boolean, default=True)

    # Relationships
    borrowed_books = db.relationship('BorrowedBook', backref='book', lazy=True)


class BorrowedBook(db.Model):
    __tablename__ = 'borrowed_books'

    id = db.Column(db.String(25), primary_key=True)
    book_id = db.Column(db.String(25), db.ForeignKey('books.id'))
    student_id = db.Column(db.String(25), db.ForeignKey('students.id'))
    borrow_date = db.Column(db.DateTime)
    return_date = db.Column(db.DateTime)
