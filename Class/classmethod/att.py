class car:
    wheels = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def driven(self):
        return f"{self.brand} {self.model} is driving...."


car1 = car("Toyota", "Corolla")
car2 = car("Tesla", "Model s")

print(car1.brand)
print(car2.model)
print(car1.driven())