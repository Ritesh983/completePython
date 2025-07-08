
class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    def get__brand(self):
        return self.__brand + "!"
    def full_name(self):
        return f"{self.__brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla=ElectricCar("Tesla", "Model S", "100 kWh")
#print(my_tesla.__brand)  cannot access private attribute
print(my_tesla.get__brand())  # Accessing private attribute through a method
print(my_tesla.model) 
print(my_tesla.battery_size)
print(my_tesla.full_name())