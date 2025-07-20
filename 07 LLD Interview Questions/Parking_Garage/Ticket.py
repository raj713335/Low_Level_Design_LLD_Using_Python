import Vehicle
from ParkingSpot import ParkingSpot
import uuid
from datetime import datetime


class Ticket:
    def __init__(self, vehicle: Vehicle, spot: ParkingSpot):
        self.ticket_id = str(uuid.uuid4())
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.now()
        self.exit_time = None

    def close(self):
        self.exit_time = datetime.now()

    def get_fees(self):
        duration_minutes = (self.exit_time - self.entry_time).seconds / 60
        return max(10, int(duration_minutes) * 1)
