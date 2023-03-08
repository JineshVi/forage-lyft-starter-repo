from batteries.battery import Battery
from datetime import datetime, date, time

class Spindler():
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        due_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        return self.current_date > due_date
