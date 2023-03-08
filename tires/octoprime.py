from tire import Tire
import numpy as np

class Octoprime(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        sum_of_damage = np.sum(self.tire_wear_array)
        
        return sum_of_damage >= 3