from typing import List
from dataclasses import dataclass


@dataclass
class TicketInfo:
    """Seat Info:
    car:
        range: 1 - 10
    row:
        window seat: A, E
        aisle seat: B, C, D
    column:
        range: 1 - 10
    """
    car_number: int = None
    seat_number: int = None
    
    def vertify(self):
        # vertify seat info
        if self.car_number not in range(10):
            raise TypeError('unknown car number')
        elif not self.col_no and self.col_no not in range(5):
            raise TypeError('unknown column number')
        elif not self.row_no and self.row_no not in range(10):
            raise TypeError('unknown row number')

@dataclass
class TicketsOder:
    """[summary]

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

    def vertify(self):
        if not self.uuid:
            raise ValueError("Lost user id")

        if not all(isinstance(ticket, TicketInfo) for ticket in self.tickets):
            raise TypeError("Get invalid ticket.")

        if len(self.tickets) > 4:
            raise ValueError("Get too many tickets")

        try:
            for ticket in self.tickets:
                ticket.vertify()
        except TypeError as err_msg:
            raise TypeError("Vertify ticket error") from err_msg
