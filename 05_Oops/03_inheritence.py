class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla=ElectricCar("Tesla", "Model S", "100 kWh")
print(my_tesla.brand)
print(my_tesla.model) 
print(my_tesla.battery_size)
print(my_tesla.full_name())