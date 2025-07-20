from SpotType import SpotType
from Vehicle import Vehicle


class ParkingSpot:
    def __init__(self, spot_id: str, spot_type: SpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.vehicle = None

    def is_free(self):
        return self.vehicle is None

    def assign_vehicle(self, vehicle: Vehicle):
        if not self.is_free():
            raise Exception("Spot already taken")
        self.vehicle = vehicle

    def remove_vehicle(self):
        self.vehicle = None
