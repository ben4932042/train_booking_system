# order
from dataclasses import dataclass, field


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
#ticket
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

# =============================================================

# picking ticket strategy
from typing import List
from typing import Callable

TicketOrderingStrategy = Callable[[str], List[TicketInfo]]

def one_ticket_business_level_random_seat_strategy(order_id: str) -> List[TicketInfo]:
    return [TicketInfo(order_id, 1, 1, 'C')]

def one_ticket_business_level_window_seat_strategy(order_id: str) -> List[TicketInfo]:
    return [TicketInfo(order_id, 1, 2, 'A')]

def one_ticket_business_level_aisle_seat_strategy(order_id: str) -> List[TicketInfo]:
    return [TicketInfo(order_id, 1, 3, 'B')]

# =============================================================

# main 
import random
import string
from typing import List

def generate_id(length: int = 8) -> str:
    """gen random id."""
    return "".join(random.choices(
                    string.ascii_uppercase+string.digits,
                    k=length))

def request_booking_api(tickets: List[TicketInfo]) -> bool:
    """random return booking result."""
    return random.choice([True, False])

class CustomerSupport:
    def __init__(self, customerinfo: TrainTicketOrder) -> None:
        self.customerinfo = customerinfo
        self.order_id = generate_id(20)
        self.tickets: list[TicketInfo] = []

    def pick_tickets(self, picking_strategy: TicketOrderingStrategy):
        """choosing tickets by some defined picking strategy"""
        self.tickets = picking_strategy(order_id=self.order_id)
        
    def booking_tickets(self) -> bool:
        """booking tickets"""
        if request_booking_api(self.tickets):
            print('booking success.')
            self.customerinfo.id = self.order_id
            print('*'*20)
            self.customerinfo.status()
        else:
            print('booking failed.')

if __name__ == "__main__":
    customerinfo = TrainTicketOrder(id='123qwe')
    customer = CustomerSupport(customerinfo=customerinfo)
    customer.pick_tickets(one_ticket_business_level_random_seat_strategy)
    customer.booking_tickets()
