# static methods are methods that belong to the class rather than an instance of the class.

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    @staticmethod
    def general_description():
        return "Cars are designed for transportation."
    
my_car = Car("Toyota", "Corolla")

print(my_car.general_description())  # Calling static method through an instance
print(Car.general_description())  # Calling static method through the class