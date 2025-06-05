from abc import ABC, abstractmethod


# Abstract class for Payment
class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        ...


# Implementing Payment Methods
class CreditCardPayment(Payment):
    def pay(self):
        print(f"Paid {self.amount} using credit card")


class PayPalPayment(Payment):
    def pay(self):
        print(f"Paid {self.amount} using PayPal")


if __name__ == "__main__":
    payment_1 = CreditCardPayment(100)
    payment_1.pay()

    payment_2 = PayPalPayment(76.1)
    payment_2.pay()
