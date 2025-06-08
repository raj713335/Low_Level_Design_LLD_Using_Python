# Define an interface

from abc import ABC, abstractmethod
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        ...

# Implement concreate transport types
class Truck(Transport):
    def deliver(self):
        print("Deliver by land in a truck")

class Ship(Transport):
    def deliver(self):
        print("Deliver by sea in a ship")

class Plane(Transport):
    def deliver(self):
        print("Deliver by air in a plane")

# Creator (Logistic) base class

class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        ...

    def plan_delivery(self):
        transport = self.create_transport()
        transport.deliver()


# Subclass decide which objects to create

class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

class AirLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Plane()

# Client code

def client_code(logistics: Logistics):
    logistics.plan_delivery()

client_code(RoadLogistics())
client_code(SeaLogistics())
client_code(AirLogistics())
