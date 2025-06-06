class Vehicle:
    def start(self):
        raise NotImplementedError

class Car(Vehicle):
    def start(self):
        print("Starting the car engine...")

class Cycle(Vehicle):
    def start(self):
        # This doesn't make sense for cycle
        print("Pedaling the bicycle")


if __name__ == "__main__":
    car1 = Car()
    bike1 = Cycle()

    car1.start()
    bike1.start()