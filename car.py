from serviceable import Serviceable
from engines import Engine
from batteries import Battery

class Car(Serviceable):
    def __init__(self):
        self.engine = Engine
        self.battery = Battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
