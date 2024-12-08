import schedule
import time
from datetime import datetime
from utils.database_client import DatabaseClient

class DataAggregator:
    def __init__(self):
        self.db_client = DatabaseClient()

    def aggregate_data(self):
        print(f"[{datetime.now()}] Aggregating data...")
        appointments_per_doctor = self.db_client.get_appointments_per_doctor()
        print("Appointments per doctor:", appointments_per_doctor)

        common_conditions = self.db_client.get_common_conditions()
        print("Common conditions treated:", common_conditions)

    def start(self):
        schedule.every(5).minutes.do(self.aggregate_data)
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    aggregator = DataAggregator()
    aggregator.start()
