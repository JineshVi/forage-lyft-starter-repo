import unittest
from datetime import datetime, date, time

#importing engine modules and functions
from ..engines import capulet_engine
from ..engines import willoughby_engine
from ..engines import sterman_engine

#importing battery modules and functions
from ..batteries import nubbin
from ..batteries import spindler


class Testing_engines(unittest.TestCase):
    #Engine Testing
    def test_capulet_engine_1(self):
        last_sevice_mileage = 40000
        current_mileage = 80000

        car_engine = capulet_engine.CapuletEngine(last_sevice_mileage,current_mileage)
        self.assertTrue(car_engine.needs_service())

    def test_capulet_engine_2(self):
        last_sevice_mileage = 70000
        current_mileage = 80000

        car_engine = capulet_engine.CapuletEngine(last_sevice_mileage,current_mileage)
        self.assertFalse(car_engine.needs_service())
    
    def test_willoughby_engine_1(self):
        last_service_mileage = 50000
        current_mileage = 120000

        car_engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(car_engine.needs_service())

    def test_willoughby_engine_2(self):
        last_service_mileage = 80000
        current_mileage = 120000

        car_engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(car_engine.needs_service())

    def test_sterman_engine_1(self):
        warning_light_on = True

        car_engine = sterman_engine.StermanEngine(warning_light_on)
        self.assertTrue(car_engine.needs_service())

    def test_sterman_engine_2(self):
        warning_light_on = False

        car_engine = sterman_engine.StermanEngine(warning_light_on)
        self.assertFalse(car_engine.needs_service())

    #Battery Testing
    def test_nubbin_battery_1(self):
        last_service_date = date(2019, 2, 7)
        current_date = date.today()

        car_battery = nubbin.Nubbin(last_service_date, current_date)
        self.assertTrue(car_battery.needs_service())

    def test_nubbin_battery_2(self):
        last_service_date = date(2020, 6, 17)
        current_date = date.today()

        car_battery = nubbin.Nubbin(last_service_date, current_date)
        self.assertFalse(car_battery.needs_service())

    def test_spindler_battery_1(self):
        last_service_date = date(2020, 6, 7)
        current_date = date.today()

        car_battery = spindler.Spindler(last_service_date, current_date)
        self.assertTrue(car_battery.needs_service())

    def test_spindler_battery_2(self):
        last_service_date = date(2022, 6, 17)
        current_date = date.today()

        car_battery = spindler.Spindler(last_service_date, current_date)
        self.assertFalse(car_battery.needs_service())
    

if __name__ == '__main__':
    unittest.main()
