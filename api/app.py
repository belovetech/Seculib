#!/usr/bin/env python3
import os
from flask import jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from helpers.middlewares import RateLimitMiddleware
from api.library.views import app_views
from models.engine.db import db, app

# initialize database
CORS(app)

# load environment variables
load_dotenv(override=True)
SECRET_KEY = os.getenv('SECRET_KEY')


# apply rate limit middleware
RateLimitMiddleware(app, rate_limit=100, time_window=60)

# register blueprints
app.register_blueprint(app_views)


# health check endpoint
@app.route('/healthz', methods=['GET'])
def healthz():
    print("Health check.")
    return jsonify({'message': 'OK'})


@app.cli.command('seed_books')
def seed_books():
    print('Seeding books...')
    from models.book import Book
    from api.seed_books import seed_books
    import uuid

    for book in seed_books:
        book_id = str(uuid.uuid4())
        new_book = Book(id=book_id, title=book['title'], author=book['author'], available=book['available'])
        db.session.add(new_book)
    db.session.commit()
    print('Books seeded successfully.')



if __name__ == '__main__':
    port = int(os.getenv('PORT', 3000))  # Use the PORT environment variable or default to 3000
    app.run(host="0.0.0.0", port=port, debug=True)
