class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine started with {self.horsepower} HP.")


class Wheel:
    def __init__(self, type):
        self.type = type

    def rotate(self):
        print(f"The {self.type} wheel is rotating.")


class Transmission:
    def __init__(self, type):
        self.type = type

    def shift_gear(self):
        print(f"Transmission shifted: {self.type}")


class Car:
    def __init__(self, engine, wheel, transmission):
        self.engine = engine
        self.wheel = wheel
        self.transmission = transmission

    def drive(self):
        self.engine.start()
        self.wheel.rotate()
        self.transmission.shift_gear()
        print("Car is running")


if __name__ == "__main__":
    engine = Engine(1500)
    wheel = Wheel("Alloy")
    transmission = Transmission("Automatic")

    car = Car(engine, wheel, transmission)
    car.drive()
