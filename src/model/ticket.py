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
    order_id: str = 'test'
    car_number: int = field(init=False)
    row_no: int = field(init=False)
    col_no: int = field(init=False)
    def __post_init__(self):
        # vertify seat info
        try:
            if self.car_number not in range(10):
                raise TypeError('unknown car number')
            elif not self.col_no and self.col_no not in range(5):
                raise TypeError('unknown column number')
            elif not self.row_no and self.row_no not in range(10):
                raise TypeError('unknown row number')
        except AttributeError:
            pass

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
