from car import Car

#Importing Engine module classes and functions
from engines.capulet_engine import CapuletEngine
from engines.sterman_engine import StermanEngine
from engines.willoughby_engine import WilloughbyEngine

#Importing Battery module classes and functions
from batteries.nubbin import Nubbin
from batteries.spindler import Spindler

#importing Tire module classes and functions
from tires.carrigan import Carrigan
from tires.octoprime import Octoprime



class CarFactory():
    @staticmethod
    def create_calliope(self,current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = Spindler(last_service_date, current_date)
        tire = Carrigan(tire_wear_array)

        car = Car(engine, battery, tire)

        return car
    
    @staticmethod
    def create_glissade(self,current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = Spindler(last_service_date, current_date)
        tire = Carrigan(tire_wear_array)

        car = Car(engine, battery, tire)

        return car
    
    @staticmethod
    def create_palindrome(self,current_date, last_service_date, warning_ligh_on, tire_wear_array):
        engine = StermanEngine(warning_ligh_on)
        battery = Spindler(last_service_date, current_date)
        tire = Octoprime(tire_wear_array)

        car = Car(engine, battery, tire)

        return car
    
    @staticmethod
    def create_rorschach(self,current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = Nubbin(last_service_date, current_date)
        tire = Octoprime(tire_wear_array)

        car = Car(engine, battery, tire)

        return car
    
    @staticmethod
    def create_thovex(self,current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = Nubbin(last_service_date, current_date)
        tire = Carrigan(tire_wear_array)

        car = Car(engine, battery, tire)

        return car
