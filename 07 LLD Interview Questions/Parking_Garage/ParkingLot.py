from ParkingSpot import ParkingSpot
from Ticket import Ticket
from SpotType import SpotType
from Vehicle import Vehicle


class ParkingLot:
    def __init__(self):
        self.spots: list[ParkingSpot] = []
        self.active_tickets: dict[str, Ticket] = {}

    def add_spot(self, spot: ParkingSpot):
        self.spots.append(spot)

    def find_available_spot(self, requested_type: SpotType):
        for spot in self.spots:
            if spot.spot_type == requested_type and spot.is_free():
                return spot

        return None

    def park_vehicle(self, vehicle: Vehicle, spot_type: SpotType) -> Ticket:
        spot = self.find_available_spot(spot_type)
        if not spot:
            raise Exception("No available spots for requested type")

        spot.assign_vehicle(vehicle)
        ticket = Ticket(vehicle, spot)
        self.active_tickets[ticket.ticket_id] = ticket
        return ticket

    def unpark_vehicle(self, ticket_id: str):
        ticket = self.active_tickets.get(ticket_id)
        if not ticket:
            raise Exception("Invalid ticket Id")
        ticket.close()
        free = ticket.get_fees()
        ticket.spot.remove_vehicle()
        del self.active_tickets[ticket_id]
        return free
