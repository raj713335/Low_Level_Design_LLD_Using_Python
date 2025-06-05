# Parent Class

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking...")

    def eat(self):
        super().eat()
        print(f"{self.name} is eating bones...")

class Indian_Dog(Dog):
    def bark(self):
        print(f"{self.name} is barking...")

    def eat(self):
        print(f"{self.name} is eating rice...")

class Labrador(Dog):
    def bark(self):
        print(f"{self.name} is barking...")

    def eat(self):
        print(f"{self.name} is eating meat...")

class MyDog(Indian_Dog, Labrador):
    def passing(self):
        pass



if __name__ == "__main__":
    my_dog = MyDog("Motu")
    my_dog.eat()
    my_dog.bark()
