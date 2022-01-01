from typing import List
from dataclasses import dataclass


@dataclass
class TicketInfo:
    """Seat Info:
    car_number:
        range: 0 - 9
    seat_number:
        range: 0 - 49

    Raises:
        ValueError: Unknown car number.
        ValueError: Unknown seat number.
    """
    car_number: int = None
    seat_number: int = None
    
    def verify(self):
        # verify seat info
        if not self.seat_number and self.car_number not in range(10):
            raise ValueError('Unknown car number.')
        elif not self.seat_number and self.seat_number not in range(50):
            raise ValueError('Unknown seat number.')


@dataclass
class TicketsOrder:
    """[summary]

    Arge:
        ticket_number (int): ticket number from order info

    Raises:
        ValueError: lost user id  or too many tickets.
        TypeError: invalid ticket object type.
    """
    uuid: str = None
    tickets: List[TicketInfo] = None
    train_no: int = '9487'
    departure_station: str = 'departure_station'
    arrival_station: str = 'arrival_station'

    def status(self):
        print(f"train number: {self.train_no}")
        print(f"user id: {self.uuid}")

    def verify(self):
        if not self.uuid:
            raise ValueError("Lost user id")

        if not all(isinstance(ticket, TicketInfo) for ticket in self.tickets):
            raise TypeError("Get invalid ticket.")

        if len(self.tickets) > 4:
            raise ValueError("Get too many tickets")

        try:
            for ticket in self.tickets:
                ticket.verify()
        except TypeError as err_msg:
            raise TypeError("Verify ticket error") from err_msg