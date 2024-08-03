from flask import  jsonify
from api.library.views import app_views
from models.engine.db import db
from models.engine.book_manager import BookManager


book_manager = BookManager(db)

@app_views.route('/books', methods=['GET'])
def get_books():
    try:
       books = book_manager.get_all_books()
       return jsonify({'message': 'Book fetch successfully', 'data': books}), 200
    except Exception as e:
        print("Get books error: ", e)
        return jsonify({'message': "Unable to fetch book from the library"}), 500

@app_views.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    try:
       book = book_manager.get_book_by_id(book_id)
       return jsonify({'message': 'Book fetch successfully', 'data': book}), 200
    except Exception as e:
        print("Get book error: ", e)
        return jsonify({'message': "Unable to fetch book from the library"}), 500
