from dataclasses import dataclass
from src.model.ticket_info import TicketsOrder


@dataclass
class OrderInfo:
    """Order Info:
    autoticket:
        system automatic ticket allocation: True or False
    uuid: 
        user uuid
    prefer:
        level window: 0
        level aisle: 1
    car type:
        business_cabin: 0
        business_cabin: 1
    number:
        ticket number
    chosen seats list:
        tickets order with ticket info list
    departure_station
        TDB
    arrival_station
        TDB
    """
    uuid: str
    autoticket: bool = True
    prefer: int = 0
    car_type: int = ''
    number: int = ''
    chosen_seats_list: TicketsOrder = None
    departure_station: str = 'departure_station'
    arrival_station: str = 'arrival_station'
    
    def __post_init__(self):
        
        if self.autoticket and self.chosen_seats_list:
            raise TypeError("auto choice ticket do not need chosen_seats_list.")
        elif not self.autoticket and not self.chosen_seats_list:
            raise TypeError("lost chosen_seats_list.")
        
        if not self.autoticket:
            if not (self.prefer or self.car_type or self.number):
                raise TypeError("unuse param exist.")
        if self.prefer and self.prefer not in [0, 1, 2]:
            raise TypeError('unknown prefer mode')
        if self.car_type not in [0, 1]:
            raise TypeError('unknown car_type mode')
        if self.number not in [1, 2, 3, 4]:
            raise TypeError('unknown ticket number.')  