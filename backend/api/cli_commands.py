import uuid
from models.book import Book
from models.student import Student
from werkzeug.security import generate_password_hash
from api.seed_books import seed_books
from models.engine.db import db


def register_cli_commands(app):
    @app.cli.command('seed_books')
    def seed_books_command():
        print('Seeding books...')

        try:
            for book in seed_books:
                book_id = str(uuid.uuid4())
                new_book = Book(
                    id=book_id,
                    title=book['title'],
                    author=book['author'],
                    available=book.get('available', True)
                )
                db.session.add(new_book)
            db.session.commit()
            print('Books seeded successfully.')
        except Exception as e:
            db.session.rollback()
            print(f'Error seeding books: {str(e)}')
        finally:
            db.session.close()

    @app.cli.command('create_admin')
    def create_admin_command():

        try:
            admin_exists = Student.query.filter_by(matric_no='admin').first()
            if admin_exists:
                print('Admin has already been created.')
                return

            admin = Student(
                id=str(uuid.uuid4()),
                name='admin',
                matric_no='admin',
                department='admin',
                level='admin',
                password=generate_password_hash('admin'),
                role='admin'
            )
            db.session.add(admin)
            db.session.commit()
            print('Admin user created successfully.')
        except Exception as e:
            db.session.rollback()
            print(f'Error creating admin user: {str(e)}')
        finally:
            db.session.close()
