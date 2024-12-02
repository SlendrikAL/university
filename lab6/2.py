class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def get_info(self):
        return (self.make,self.model)
class Car(Vehicle):
    def __init__(self,make,model, fuel_type):
        self.fuel_type = fuel_type
        super().__init__(make,model)
    def get_info(self):
        return (self.make,self.model,self.fuel_type)
Car1 = Car('Honda', 'C9', 'Дизель')
Car2 = Car('Hyundai','Solaris','Бензин')
print(Car1.get_info())
print(Car2.get_info())
