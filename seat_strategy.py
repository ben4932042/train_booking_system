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


TicketOrderingStrategy = Callable[[str], List[TicketInfo]]

col_dic = {
    0:'A',
    1:'B',
    2:'C',
    3:'D',
    4:'E',
}

def check_have_seats(seat_list: list) -> bool:
    check = True
    for i in seat_list:
        if i == 0:
            check = False
            break
    return check

#one ticket
def one_ticket_business_level_random_seat_strategy(order_id: str) -> List[TicketInfo]:
    global seat_list_list
    for row_index, row in enumerate(seat_list_list):
        for col_index, col in enumerate(row):
            if col:
                seat_list_list[row_index][col_index] = 0
                return [TicketInfo(order_id, 1, row_index+1, col_dic[col_index])]
    raise Exception("No seat availble.")

def one_ticket_business_level_window_seat_strategy(order_id: str) -> List[TicketInfo]:
    global seat_list_list
    for col_index in [0, 4]:
        for row_index in range(10):
            first_seat = seat_list_list[row_index][col_index]
            if first_seat:
                seat_list_list[row_index][col_index] = 0
                return [TicketInfo(order_id, 1, row_index+1, col_dic[col_index])]
            
    return one_ticket_business_level_random_seat_strategy(seat_list_list, order_id)

def one_ticket_business_level_aisle_seat_strategy(order_id: str) -> List[TicketInfo]:
    global seat_list_list
    for row_index in range(10):
        for col_index in range(1, 4):
            first_seat = seat_list_list[row_index][col_index]
            if first_seat:
                seat_list_list[row_index][col_index] = 0
                return [TicketInfo(order_id, 1, row_index+1, col_dic[col_index])]
    return one_ticket_business_level_random_seat_strategy(order_id)


def two_ticket_business_level_random_seat_strategy(order_id: str) -> List[TicketInfo]:
    global seat_list_list
    for col_index in [0, 4]:
        for row_index in range(10):
            first_seat = seat_list_list[row_index][col_index: col_index+2]
            if check_have_seats(first_seat):
                seat_list_list[row_index][col_index] = 0
                seat_list_list[row_index][col_index+1] = 0
                return [
                    TicketInfo(order_id, 1, row_index+1, col_dic[col_index]),
                    TicketInfo(order_id, 1, row_index+1, col_dic[col_index+1])
                ]

    return [
        one_ticket_business_level_random_seat_strategy(order_id=order_id),
        one_ticket_business_level_random_seat_strategy(order_id=order_id)   
    ]

def two_ticket_business_level_window_seat_strategy(order_id: str) -> List[TicketInfo]:
    global seat_list_list
    for col_index in [0, 3]:
        for row_index in range(10):
            first_seat = seat_list_list[row_index][col_index: col_index+2]
            if check_have_seats(first_seat):
                seat_list_list[row_index][col_index] = 0
                seat_list_list[row_index][col_index+1] = 0
                return [
                    TicketInfo(order_id, 1, row_index+1, col_dic[col_index]),
                    TicketInfo(order_id, 1, row_index+1, col_dic[col_index+1])
                ]
            
    return two_ticket_business_level_random_seat_strategy(order_id=order_id)

def two_ticket_business_level_aisle_seat_strategy(order_id: str) -> List[TicketInfo]:
    global seat_list_list
    for col_index in range(1,5):
        for row_index in range(10):
            first_seat = seat_list_list[row_index][col_index-1:col_index+1]
            if first_seat[1] == 0:
                continue
            if check_have_seats(first_seat):
                seat_list_list[row_index][col_index-1] = 0
                seat_list_list[row_index][col_index] = 0
                return [
                    TicketInfo(order_id, 1, row_index+1, col_dic[col_index-1]),
                    TicketInfo(order_id, 1, row_index+1, col_dic[col_index])
                ]
    return two_ticket_business_level_random_seat_strategy(order_id=order_id)    

def three_ticket_business_level_random_seat_strategy(order_id: str) -> List[TicketInfo]:
    global seat_list_list
    for row_index in range(10):
        col_index = 2
        first_seat = seat_list_list[row_index][col_index: col_index+3]
        if check_have_seats(first_seat):
            seat_list_list[row_index][col_index] = 0
            seat_list_list[row_index][col_index+1] = 0
            seat_list_list[row_index][col_index+2] = 0
            return [
                    TicketInfo(order_id, 1, row_index+1, col_dic[col_index]),
                    TicketInfo(order_id, 1, row_index+1, col_dic[col_index+1]),
                    TicketInfo(order_id, 1, row_index+1, col_dic[col_index+2])
                    ]

    return two_ticket_business_level_random_seat_strategy(order_id=order_id) + one_ticket_business_level_random_seat_strategy(order_id=order_id)

def four_ticket_business_level_random_seat_strategy(order_id: str) -> List[TicketInfo]:
    global seat_list_list
    for row_index in range(10):
        for col_index in range(2):
            first_seat = seat_list_list[row_index][col_index: col_index+4]
            if check_have_seats(first_seat):
                seat_list_list[row_index][col_index] = 0
                seat_list_list[row_index][col_index+1] = 0
                seat_list_list[row_index][col_index+2] = 0
                seat_list_list[row_index][col_index+3] = 0
                return [
                    TicketInfo(order_id, 1, row_index+1, col_dic[col_index]),
                    TicketInfo(order_id, 1, row_index+1, col_dic[col_index+1]),
                    TicketInfo(order_id, 1, row_index+1, col_dic[col_index+2]),
                    TicketInfo(order_id, 1, row_index+1, col_dic[col_index+3])
                    ]
    return two_ticket_business_level_random_seat_strategy(order_id=order_id) + two_ticket_business_level_random_seat_strategy(order_id=order_id)


if __name__ == "__main__":
    seat_list_list = [
         [1, 0, 1, 1, 1],
         [1, 1, 1, 0, 1],
         [1, 1, 0, 1, 1],
         [1, 1, 1, 1, 1],
         [0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
    ]


    tick = four_ticket_business_level_window_seat_strategy(order_id = '123456')
    print(tick)

