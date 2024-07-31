import sqlite3
import uuid



class sessionManager:

    def __init__(self, db_name:str):
        self.db_name = db_name
        self.create_session_table()


    def create_connection(self):
        """Create a database connection."""
        conn = sqlite3.connect(self.db_name)
        return conn

    def create_session_table(self):
        """Create the sessions table if it doesn't already exist."""
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS sessions (
                    session_id TEXT PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    expires_at TIMESTAMP NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                )
            ''')
            conn.commit()


    def create_session(self, user_id, expires_at):
        """Create a new session for the user."""
        session = self.get_session_by_user_id(user_id)
        if session:
            session_id = session[0]
            self.delete_session(session_id)

        session_id = str(uuid.uuid4())
        self.insert_session(session_id, user_id, expires_at)
        return session_id

    def insert_session(self, session_id, user_id, expires_at):
        """Insert a session into the table."""
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO sessions (session_id, user_id, expires_at)
                VALUES (?, ?, ?)
            ''', (session_id, user_id, expires_at))
            conn.commit()

    def delete_session(self, session_id):
        """Delete a session by its ID."""
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM sessions WHERE session_id = ?
            ''', (session_id,))
            conn.commit()

    def get_session_by_user_id(self, user_id):
        """Retrieve a session by user ID."""
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM sessions WHERE user_id = ?
            ''', (user_id,))
            return cursor.fetchone()

    def get_session_by_session_id(self, session_id):
        """Retrieve a session by its ID."""
        with self.create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM sessions WHERE session_id = ?
            ''', (session_id,))
            return cursor.fetchone()


