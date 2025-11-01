class Car:
    wheels = 4   # class attribute

    def __init__(self, brand):
        self.brand = brand

    @classmethod
    def change_wheels(cls, count):
        cls.wheels = count   # class attribute change হচ্ছে

car1 = Car("Toyota")
car2 = Car("Tesla")

print(car1.wheels, car2.wheels)  # 4 4

Car.change_wheels(6)  # class method call

print(car1.wheels, car2.wheels)  # 6 6
