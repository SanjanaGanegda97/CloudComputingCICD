import sqlite3

class DatabaseClient:
    def __init__(self, db_path="aggregator.db"):
        self.connection = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        with self.connection:
            self.connection.execute(
                """CREATE TABLE IF NOT EXISTS appointments (
                   id INTEGER PRIMARY KEY,
                   doctor_id INTEGER,
                   patient_id INTEGER,
                   condition TEXT,
                   timestamp TEXT
                )"""
            )

    def get_appointments_per_doctor(self):
        query = "SELECT doctor_id, COUNT(*) FROM appointments GROUP BY doctor_id"
        return self.execute_query(query)

    def get_common_conditions(self):
        query = "SELECT condition, COUNT(*) FROM appointments GROUP BY condition ORDER BY COUNT(*) DESC"
        return self.execute_query(query)

    def execute_query(self, query, params=()):
        with self.connection:
            cursor = self.connection.execute(query, params)
            return cursor.fetchall()
