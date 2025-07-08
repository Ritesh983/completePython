class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
    def get__brand(self):
        return self.__brand + "!"
    @property   
    def model(self):
        return self.__model
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
my_car=Car("Toyota","Corolla")

#print(my_car.model())  # Accessing read-only property
print(my_car.model)  # Accessing read-only property directly