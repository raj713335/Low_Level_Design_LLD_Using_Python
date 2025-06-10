# Product (House)

class House:
    def __init__(self):
        self.walls = None
        self.doors = None
        self.windows = None
        self.roof = None
        self.garden = None
        self.swimming_pool = None
        self.garage = None

    def __str__(self):
        return (f"House with {self.walls} walls, {self.doors} doors,"
                f"{self.windows} windows, {self.roof} roof, "
                f"{self.garden} garden, {self.swimming_pool} swimming Pool,"
                f"{self.garage} garage.")

# Builder Interface

from abc import ABC, abstractmethod

class HouseBuilder(ABC):
    @abstractmethod
    def reset(self):
        ...

    @abstractmethod
    def build_walls(self):
        ...


    @abstractmethod
    def build_doors(self):
        ...

    @abstractmethod
    def build_windows(self):
        ...


    @abstractmethod
    def build_roof(self):
        ...


    @abstractmethod
    def add_garden(self):
        ...


    @abstractmethod
    def add_swimming_pool(self):
        ...


    @abstractmethod
    def add_garage(self):
        ...


    @abstractmethod
    def get_result(self):
        ...


# Concreate Builder (Simple and Luxury Houses)

class SimpleHouseBuilder(HouseBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.house = House()


    def build_walls(self):
        self.house.walls = 4

    def build_doors(self):
        self.house.doors = 1


    def build_windows(self):
        self.house.windows = 2


    def build_roof(self):
        self.house.roof = "Simple Roof"


    def add_garden(self):
        self.house.garden = False


    def add_swimming_pool(self):
        self.house.swimming_pool = False


    def add_garage(self):
        self.house.garage = False


    def get_result(self):
        return self.house


class LuxuryHouseBuilder(HouseBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = 10

    def build_doors(self):
        self.house.doors = 4

    def build_windows(self):
        self.house.windows = 8

    def build_roof(self):
        self.house.roof = "Luxury Roof with SkyLights"

    def add_garden(self):
        self.house.garden = True

    def add_swimming_pool(self):
        self.house.swimming_pool = True

    def add_garage(self):
        self.house.garage = True

    def get_result(self):
        return self.house


# Director

class Director:
    def __init__(self, builder: HouseBuilder):
        self.builder = builder

    def construct_simple_house(self):
        self.builder.reset()
        self.builder.build_walls()
        self.builder.build_doors()
        self.builder.build_windows()
        self.builder.build_roof()
        self.builder.add_garden()

    def construct_luxury_house(self):
        self.builder.reset()
        self.builder.build_walls()
        self.builder.build_doors()
        self.builder.build_windows()
        self.builder.build_roof()
        self.builder.add_garden()
        self.builder.add_swimming_pool()
        self.builder.add_garage()


# Client Code

if __name__ == "__main__":
    # Build a simple house

    simple_builder = SimpleHouseBuilder()
    director = Director(simple_builder)
    director.construct_simple_house()
    simple_house = simple_builder.get_result()
    print("Simple House: ", simple_house)

    luxury_builder = LuxuryHouseBuilder()
    director = Director(luxury_builder)
    director.construct_luxury_house()
    luxury_house = luxury_builder.get_result()
    print("Luxury House: ", luxury_house)


