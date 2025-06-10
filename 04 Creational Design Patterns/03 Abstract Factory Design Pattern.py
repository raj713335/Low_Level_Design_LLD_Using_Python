# Abstract Product Interface

from abc import ABC, abstractmethod


# Chair Interface

class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        ...


# Sofa Interface

class Sofa(ABC):

    @abstractmethod
    def lie_on(self):
        ...


# CoffeeTable Interface

class CoffeeTable(ABC):
    @abstractmethod
    def place_items(self):
        ...


# Concreate Product Variant

# Modern Products

class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on Modern chair"


class ModernSofa(Sofa):
    def lie_on(self):
        return "Lying on a modern sofa"


class ModernCoffeeTable(CoffeeTable):
    def place_items(self):
        return "Items placed on a modern coffee table."


# Victorian Products

class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on Victorian chair"


class VictorianSofa(Sofa):
    def lie_on(self):
        return "Lying on a Victorian sofa"


class VictorianCoffeeTable(CoffeeTable):
    def place_items(self):
        return "Items placed on a Victorian coffee table."


# ArtDeco Products

class ArtDecoChair(Chair):
    def sit_on(self):
        return "Sitting on ArtDeco chair"


class ArtDecoSofa(Sofa):
    def lie_on(self):
        return "Lying on a ArtDeco sofa"


class ArtDecoCoffeeTable(CoffeeTable):
    def place_items(self):
        return "Items placed on a ArtDeco coffee table."


# Abstract Factory Interface

class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        ...

    @abstractmethod
    def create_sofa(self) -> Sofa:
        ...

    @abstractmethod
    def create_coffee_table(self) -> CoffeeTable:
        ...


# Modern Furniture Factory

class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()

    def create_coffee_table(self) -> CoffeeTable:
        return ModernCoffeeTable()


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()

    def create_coffee_table(self) -> CoffeeTable:
        return VictorianCoffeeTable()


class ArtDecoFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ArtDecoChair()

    def create_sofa(self) -> Sofa:
        return ArtDecoSofa()

    def create_coffee_table(self) -> CoffeeTable:
        return ArtDecoCoffeeTable()


# Client Code

class FurnitureStore:
    def __init__(self, _factory: FurnitureFactory):
        self.chair = _factory.create_chair()
        self.sofa = _factory.create_sofa()
        self.coffee_table = _factory.create_coffee_table()

    def show_furniture(self):
        print(self.chair.sit_on())
        print(self.sofa.lie_on())
        print(self.coffee_table.place_items())


if __name__ == "__main__":
    style = input("Enter Furniture Style (modern/victorian/art deco):").strip().lower()

    if style == "modern":
        factory = ModernFurnitureFactory()
    elif style == "victorian":
        factory = VictorianFurnitureFactory()
    elif style == "art deco":
        factory = ArtDecoFurnitureFactory()
    else:
        raise ValueError("Unknown furniture Style")

    store = FurnitureStore(factory)
    store.show_furniture()
