from battery import Battery
from datetime import datetime, date, time

class Nubbin(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        due_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return self.current_date > due_date
