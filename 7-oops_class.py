# define a car class
class Car:  
    def __init__(self, **kwargs): #keyword arguments can pass in as many arguments as you want
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.variant = kwargs.get("variant")

my_car = Car(make = "Honda", model = "Accord", color = "Green", variant = "LX")
print(my_car.make)
his_car = Car(make = "Toyota")
print(his_car.model)


