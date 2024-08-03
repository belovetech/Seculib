
import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from helpers.middlewares import RateLimitMiddleware
from api import app_views

# initialize flask app and enable CORS
app = Flask(__name__)
CORS(app)

# load environment variables
load_dotenv(override=True)
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE_URL = os.getenv('DATABASE_URL')


# initialize database
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)

from models.student import Student, Session
from models.book import Book, BorrowedBook

# create tables
with app.app_context():
    db.create_all()

# initialize Flask-Migrate
migrate = Migrate(app, db)


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
    from models.engine.seed_books import seed_books
    import uuid

    for book in seed_books:
        book_id = str(uuid.uuid4())
        new_book = Book(id=book_id, title=book['title'], author=book['author'], available=book['available'])
        db.session.add(new_book)
    db.session.commit()
    print('Books seeded successfully.')





if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
