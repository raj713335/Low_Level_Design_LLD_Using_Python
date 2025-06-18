# Composite Pattern Python Implementation: Products and Boxes

from abc import ABC, abstractmethod


# Component Interface

class Item(ABC):
    @abstractmethod
    def get_price(self):
        ...

    @abstractmethod
    def get_description(self):
        ...


# Leaf Class: Product

class Product(Item):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def get_description(self):
        return f"Product: {self.name} (${self.price})"


# Composite Class: Box

class Box(Item):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item: Item):
        self.items.append(item)

    def remove(self, item: Item):
        self.items.remove(item)

    def get_price(self):
        total = 0

        for item in self.items:
            total += item.get_price()
        return total

    def get_description(self):
        description = [item.get_description() for item in self.items]
        return f"Box: {self.name} containing:\n " + "\n ".join(description)


# client Code

if __name__ == "__main__":
    # Leaf Products
    pen = Product("Pen", 2.5)
    notebook = Product("Notebook", 5.0)
    charger = Product("Charger", 15.0)

    # Small Box
    small_box = Box("Stationary Box")
    small_box.add(pen)
    small_box.add(notebook)

    # Another box

    electronics_box = Box("Electronics Box")
    electronics_box.add(charger)

    # Big Box

    main_box = Box("Main Box")
    main_box.add(small_box)
    main_box.add(electronics_box)
    main_box.add(Product("USB Drive", 8.0))

    print(main_box.get_description())
    print(f"Total Price: ${main_box.get_price()}")
