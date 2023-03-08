from serviceable import Serviceable
from engines.engine import Engine
from batteries.battery import Battery
from tires.tire import Tire

class Car(Serviceable):
    def __init__(self):
        self.engine = Engine
        self.battery = Battery
        self.tire = Tire

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()
