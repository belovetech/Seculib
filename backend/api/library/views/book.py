import datetime
from flask import  jsonify, request
from helpers.decorators import token_required, rate_limiter
from api.library.views import app_views
from models.engine.db import db
from models.engine.book_manager import BookManager
from models.engine.book_borrow_manager import BorrowBookManager


book_manager = BookManager(db)
book_borrow_manager = BorrowBookManager(db)


@app_views.route('/books', methods=['GET'])
@rate_limiter('/books')
def get_available_books():
    try:
        books = book_manager.get_available_books()

        ip_address = request.remote_addr
        user_agent = request.headers.get('User-Agent')
        request_url = request.url
        print(f"IP Address: {ip_address}, User Agent: {user_agent}, Request URL: {request_url}")

        return jsonify({'message': 'Book fetch successfully', 'data': books, 'count': len(books)}), 200
    except Exception as e:
        print("Get books error: ", e)
        return jsonify({'message': "Unable to fetch book from the library"}), 500



@app_views.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    try:
       book = book_manager.get_book_by_id(book_id)
       if not book:
              return jsonify({'message': 'Book not found!'}), 404

       return jsonify({'message': 'Book fetch successfully', 'data': book}), 200
    except Exception as e:
        print("Get book error: ", e)
        return jsonify({'message': "Unable to fetch book from the library"}), 500


@app_views.route('/books/borrow', methods=['POST'])
@token_required
def borrow_book():
    try:
        data = request.get_json()
        current_student = request.student_data

        if 'book_id' not in data:
            return jsonify({'message': 'book_id is required'}), 400

        book_id = data['book_id']
        student_id = current_student['student_id']
        borrow_date = datetime.datetime.now()
        return_date = borrow_date + datetime.timedelta(days=7)
        book = book_borrow_manager.borrow_book(
            book_id=book_id,
            student_id=student_id,
            borrow_date=borrow_date,
            return_date=return_date
        )
        if not book:
            return jsonify({'message': 'Book not available'}), 400

        print('Book borrowed: ', book)

        return jsonify({'message': 'Book borrowed successfully'}), 200
    except Exception as e:
        print("Get books error: ", e)
        return jsonify({'message': "Unable to borrowed book from the library"}), 500


@app_views.route('/books/return', methods=['POST'])
@token_required
def return_book():
    try:
        data = request.get_json()

        if 'borrowed_book_id' not in data:
            return jsonify({'message': 'borrowed_book_id is required'}), 400

        borrowed_book_id = data['borrowed_book_id']
        borrowed_book = book_borrow_manager.get_borrowed_book_by_id(borrowed_book_id)

        if not borrowed_book:
            return jsonify({'message': 'Borrowed book not found!'}), 404

        print("Borrowed book: ", borrowed_book)

        if borrowed_book['student_id'] != request.student_data['student_id']:
            return jsonify({'message': 'Forbidden!'}), 403


        book_borrow_manager.return_book(data['borrowed_book_id'])
        return jsonify({'message': 'Book returned successfully!'}), 200
    except Exception as e:
        print("Return book error: ", e)
        return jsonify({'message': "Unable to return book to the library"}), 500




@app_views.route('/books/borrowed', methods=['GET'])
@token_required
def get_book_borrowed_by_student():
    try:
        student_id = request.student_data['student_id']
        borrowed_books = book_borrow_manager.get_book_borrowed_by_student(student_id)
        return jsonify({
            'message': 'Borrowed book fetch successfully',
            'data': {
                'borrowed_books': borrowed_books,
                'count': len(borrowed_books)
            }
        }), 200
    except Exception as e:
        print("Get borrowd books error: ", e)
        return jsonify({'message': "Unable to fetch borrowed book from the library"}), 500
