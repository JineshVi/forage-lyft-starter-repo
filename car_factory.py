from car import Car

#Importing Engine module classes and functions
from engines.capulet_engine import CapuletEngine
from engines.sterman_engine import StermanEngine
from engines.willoughby_engine import WilloughbyEngine

#Importing Battery module classes and functions
from batteries.nubbin import Nubbin
from batteries.spindler import Spindler



class CarFactory():
    @staticmethod
    def create_calliope(self,current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = Spindler(last_service_date, current_date)

        car = Car(engine, battery)

        return car
    
    @staticmethod
    def create_glissade(self,current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = Spindler(last_service_date, current_date)

        car = Car(engine, battery)

        return car
    
    @staticmethod
    def create_palindrome(self,current_date, last_service_date, warning_ligh_on):
        engine = StermanEngine(warning_ligh_on)
        battery = Spindler(last_service_date, current_date)

        car = Car(engine, battery)

        return car
    
    @staticmethod
    def create_rorschach(self,current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = Nubbin(last_service_date, current_date)

        car = Car(engine, battery)

        return car
    
    @staticmethod
    def create_thovex(self,current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = Nubbin(last_service_date, current_date)

        car = Car(engine, battery)

        return car
