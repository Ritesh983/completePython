class Battery:
    def battery_info(self):
        return "Battery capacity is 100 kWh"

class Engine:
    def engine_info(self):
        return "Engine horsepower is 670 hp"

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

class ElectricCar(Battery, Engine,Car):
   pass

my_tesla = ElectricCar("Tesla", "Model S")
print(my_tesla.battery_info()) 
print(my_tesla.engine_info())   