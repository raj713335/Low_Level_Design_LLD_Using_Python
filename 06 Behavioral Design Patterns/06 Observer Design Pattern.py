from abc import ABC, abstractmethod
from typing import List


# Observer Interface
class Subscriber(ABC):
    @abstractmethod
    def update(self, product_name: str):
        ...


# Concreate Observers
class EmailCustomer(Subscriber):
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def update(self, product_name: str):
        print(f"[Email] To: {self.email} | {self.name}, the product '{product_name}' is now available.")


class SMSCustomer(Subscriber):
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def update(self, product_name: str):
        print(f"[SMS] To: {self.phone} | {self.name}, the product '{product_name}' is available.")


# PUBLISHER Class

class Store:
    def __init__(self, store_name: str):
        self.store_name = store_name
        self._subscribers: List[Subscriber] = []

    def subscribe(self, subscriber: Subscriber):
        self._subscribers.append(subscriber)
        print(f"{subscriber.__class__.__name__} subscribed to {self.store_name}")

    def unscribe(self, subscriber: Subscriber):
        self._subscribers.remove(subscriber)
        print(f"{subscriber.__class__.__name__} unsubscribed from {self.store_name}")

    def notify_subscriber(self, product_name: str):
        print(f"\n[{self.store_name}] Notifying all subscriber about: {product_name}")
        for subscriber in self._subscribers:
            subscriber.update(product_name)

    def add_new_product(self, product_name: str):
        print(f"\n[{self.store_name}] New Product added: {product_name}")
        self.notify_subscriber(product_name)


# Client Code

if __name__ == "__main__":
    # Create a store (Publisher)
    apple_store = Store("Apple Store")

    # Create customers (Subscribers)
    john = EmailCustomer("John Doe", "john@gmail.com")
    jane = SMSCustomer("Jane Doe", "+1288488483")

    # Subscriptions
    apple_store.subscribe(john)
    apple_store.subscribe(jane)

    # Store adds a product
    apple_store.add_new_product("Iphone 20 Max Pro")

    # Unsubscribe Jane
    apple_store.unscribe(jane)

    # Add another product
    apple_store.add_new_product("Mac Book Air 20 Plus")
