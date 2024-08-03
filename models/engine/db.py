import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from api.app import app

app = Flask(__name__)


DATABASE_URL = os.getenv('DATABASE_URL')

# initialize database
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)


# import models to create tables
from models.student import Student, Session
from models.book import Book, BorrowedBook

# create tables
with app.app_context():
    db.create_all()
