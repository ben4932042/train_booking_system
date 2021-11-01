import random
from typing import List
from typing import Callable
from dataclasses import dataclass, field


@dataclass
class TicketInfo:
    """
    Seat Info:
        car:
            range: 1 - 10
        row:
            window seat: A, E
            aisle seat: B, C, D
        column:
            range: 1 - 10
    """
    order_id: str
    car_number: int
    column_no: int
    row_no: str
    def __post_init__(self):
        # vertify seat info
        if self.car_number not in range(1, 11):
            raise TypeError('unknown car number')
        elif self.column_no not in range(1, 11):
            raise TypeError('unknown column number')
        elif self.row_no not in ['A', 'B', 'C', 'D', 'E']:
            raise TypeError('unknown row number')

@dataclass
class TrainTicketOrder:
    customer: str = 'Ben'
    id: str = ''
    departure_station: str = 'departure_station'
    arrival_station: str = 'arrival_station'
    train_num: int = '9487'

    def status(self):
        print(f"train number: {self.train_num}")
        print(f"order id: {self.id}")
        print(f"customer name: {self.customer}")
