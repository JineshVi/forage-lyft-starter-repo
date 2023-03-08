from engine import Engine

class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        mileage_limit = self.current_mileage - self.last_service_mileage

        return mileage_limit > 60000
