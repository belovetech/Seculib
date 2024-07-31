import sqlite3

class UserManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.create_table()

    def create_connection(self):
        """Create a database connection."""
        conn = sqlite3.connect(self.db_name)
        return conn

    def create_table(self):
        """Create the users table if it doesn't already exist."""
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT NOT NULL,
                    matric_no TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()

    def create_user(self, full_name, matric_no, password):
        """Insert a new user into the users table."""
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (full_name, matric_no, password)
                VALUES (?, ?, ?)
            ''', (full_name, matric_no, password))
            conn.commit()

    def read_user(self, user_id):
        """Retrieve a user by their ID."""
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM users WHERE id = ?
            ''', (user_id,))
            return cursor.fetchone()

    def update_user(self, user_id, full_name=None, matric_no=None, password=None):
        """Update user details."""
        with self.create_connection() as conn:
            cursor = conn.cursor()
            if full_name:
                cursor.execute('''
                    UPDATE users SET full_name = ? WHERE id = ?
                ''', (full_name, user_id))
            if matric_no:
                cursor.execute('''
                    UPDATE users SET matric_no = ? WHERE id = ?
                ''', (matric_no, user_id))
            if password:
                cursor.execute('''
                    UPDATE users SET password = ? WHERE id = ?
                ''', (password, user_id))
            conn.commit()

    def delete_user(self, user_id):
        """Delete a user by their ID."""
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM users WHERE id = ?
            ''', (user_id,))
            conn.commit()

    def list_users(self):
        """List all users in the table."""
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM users
            ''')
            return cursor.fetchall()


    def get_user_by_matric_no(self, matric_no):
        """Retrieve a user by their matric_no."""
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM users WHERE matric_no = ?
            ''', (matric_no,))
            user = cursor.fetchone()

            if user is None:
                return None

            return self.tuple_to_dict(user)


    def tuple_to_dict(self, user_tuple):
        """Convert a user tuple to a dictionary."""
        columns = ['id', 'full_name', 'matric_no', 'password']
        return dict(zip(columns, user_tuple))
