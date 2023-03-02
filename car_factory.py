from car import Car

class CarFactory():
    def create_calliope(self,current_date, last_service_date, current_mileage, last_service_mileage):
        self.create_calliope = Car

    def create_glissade(self,current_date, last_service_date, current_mileage, last_service_mileage):
        self.create_glissade = Car

    def create_palindrome(self,current_date, last_service_date, warning_ligh_on):
        self.create_palindrome = Car

    def create_rorschach(self,current_date, last_service_date, current_mileage, last_service_mileage):
        self.create_rorschach = Car

    def create_thovex(self,current_date, last_service_date, current_mileage, last_service_mileage):
        self.create_thovex = Car
