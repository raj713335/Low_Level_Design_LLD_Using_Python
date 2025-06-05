from abc import ABC, abstractmethod


# Define an interface

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        ...

    def breaks(self):
        print("Applying Breaks")

    @abstractmethod
    def stop(self):
        ...


class Vehicle_Registration(ABC):
    @abstractmethod
    def register(self):
        ...


# Implement the vehicle interface in a Car class
class Car(Vehicle_Registration, Vehicle):
    def register(self):
        print("Car is registered...")

    def start(self):
        print("Car is starting...")

    def breaks(self):
        print("Car is applying breaks...")

    def stop(self):
        print("Car is stopping...")


# Real World Example


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")


if __name__ == "__main__":
    my_car = Car()  # Instantiating the class
    my_car.register()
    my_car.start()
    my_car.breaks()
    my_car.stop()

    payment1 = CreditCardPayment()
    payment1.pay(100.50)

    payment2 = PayPalPayment()
    payment2.pay(200.75)
