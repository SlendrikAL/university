class Vehicle:
    make = None
    model = None
    def get_info(self):
        print(self.make,self.model)
class Car(Vehicle):
    fuel_type = None
    def get_info(self):
        print(self.make,self.model,self.fuel_type)
Car1 = Car()
Car1.make = 'Honda'
Car1.model = 'CR-V'
Car1.fuel_type = 'Дизель'

Car1.get_info()
