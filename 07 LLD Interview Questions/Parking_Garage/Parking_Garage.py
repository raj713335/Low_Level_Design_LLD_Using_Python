from ParkingLot import ParkingLot
from ParkingSpot import ParkingSpot
from Vehicle import Vehicle
from Ticket import Ticket
from SpotType import SpotType

if __name__ == "__main__":

    # create lot and add spots
    lot = ParkingLot()
    lot.add_spot(ParkingSpot("S1", SpotType.COMPACT))
    lot.add_spot(ParkingSpot("S1", SpotType.LARGE))
    lot.add_spot(ParkingSpot("S1", SpotType.REGULAR))

    # Park Vehicle

    vehicle = Vehicle("KA-01-AB-1234")
    ticket = lot.park_vehicle(vehicle, SpotType.REGULAR)
    print(f"Vehicle parked. Ticket ID: {ticket.ticket_id}")

    # Unpark a vehicle

    fee = lot.unpark_vehicle(ticket.ticket_id)
    print(f"Vehicle unparked. Fee: {fee}")