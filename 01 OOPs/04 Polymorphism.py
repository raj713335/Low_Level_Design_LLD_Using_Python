class MathOperation:
    def add(self, a, b, c=0, *args):
        sumx = a + b + c
        for each in args:
            sumx += each

        return sumx


math = MathOperation()
print("Sum of 2 Numbers :", math.add(6, 7))
print("Sum of 3 Numbers :", math.add(6, 7, 9))
print("Sum of many Numbers :", math.add(6, 7, 9, 9, 7, 9, 8, 4, 8))


class Animal:
    def make_sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def make_sound(self):
        print("Dod Barks")


class Cat(Animal):
    def make_sound(self):
        print("Cat Meows")


animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()


class Car:
    def start(self):
        print("Car is Starting..")


class Bike:
    def start(self):
        print("Bike is Starting...")


# Polymorphic Function
def vehicle_start(vehicle):
    vehicle.start()


vehicle_start(Car())
vehicle_start(Bike())
