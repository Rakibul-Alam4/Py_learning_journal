class Car:
    # class attribute
    wheels = 4  
    
    # constructor (object তৈরি হলে এটা চলবে)
    def __init__(self, brand, model):
        self.brand = brand      # instance attribute
        self.model = model

    # instance method
    def drive(self):
        return f"{self.brand} {self.model} is driving..."

car1 = Car("Toyota", "Corolla")
car2 = Car("Tesla", "Model S")

print(car1.brand)     
print(car2.model)     
print(car1.drive())   
print
