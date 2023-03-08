from tire import Tire
import numpy as np

class Carrigan(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        wornout_tire_count = np.count_nonzero(self.tire_wear_array >= 0.9)

        return wornout_tire_count >= 1