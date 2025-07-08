class Car:
    total_car=0
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_car += 1 # Incrementing the class variable total_car each time a new object is created

my_car1 = Car("Toyota", "Corolla")
my_car2 = Car("Honda", "Civic") 
my_car3 = Car("Ford", "Mustang")
print(Car.total_car)  # Accessing the class variable total_car
print(my_car1.total_car)  # Accessing the class variable through an instance
