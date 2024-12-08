import sqlite3

class Database:
    def __init__(self, db_path=":memory:"):
        self.connection = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        with self.connection:
            self.connection.execute(
                """CREATE TABLE IF NOT EXISTS patients (
                   id INTEGER PRIMARY KEY,
                   name TEXT,
                   age INTEGER,
                   medical_history TEXT
                )"""
            )

    def execute_query(self, query, params=()):
        with self.connection:
            cursor = self.connection.execute(query, params)
            return cursor.fetchall()
