from typing import Callable, List

from src.model.ticket import TicketInfo

seat_list_list = [[1 for i in range(5)] for j in range(10)]

TicketOrderingStrategy = Callable[[List[TicketInfo]], List[TicketInfo]]

#col_dic = {
#    0:'A',
#    1:'B',
#    2:'C',
#    3:'D',
#    4:'E',
#}

def check_have_seats(seat_list: list) -> bool:
    """[summary]

    Args:
        seat_list (list): check have any seats in required car no.

    Returns:
        bool: have any seat or not
    """
    check = True
    for i in seat_list:
        if i == 0:
            check = False
            break
    return check

#one ticket
def one_ticket_level_random_seat_strategy(tickets: List[TicketInfo]) -> List[TicketInfo]:
    """[summary]

    Args:
        tickets (List[TicketInfo]): ticket info with car no

    Raises:
        Exception: No seat availble.

    Returns:
        List[TicketInfo]: fully ticket info with row no and col no.
    """
    global seat_list_list
    for row_index, row in enumerate(seat_list_list):
        for col_index, col in enumerate(row):
            if col:
                seat_list_list[row_index][col_index] = 0
                ticket = tickets[0]
                ticket.row_no = row_index
                ticket.col_no = col_index
                return [ticket]
    raise Exception("No seat availble.")

def one_ticket_level_window_seat_strategy(tickets: List[TicketInfo]) -> List[TicketInfo]:
    """[summary]

    Args:
        tickets (List[TicketInfo]): ticket info with car no

    Raises:
        Exception: No seat availble.

    Returns:
        List[TicketInfo]: fully ticket info with row no and col no.
    """
    global seat_list_list
    for col_index in [0, 4]:
        for row_index in range(10):
            first_seat = seat_list_list[row_index][col_index]
            if first_seat:
                seat_list_list[row_index][col_index] = 0
                ticket = tickets[0]
                ticket.row_no = row_index
                ticket.col_no = col_index
                return [ticket]
            
    return one_ticket_level_random_seat_strategy(tickets)

def one_ticket_level_aisle_seat_strategy(tickets: List[TicketInfo]) -> List[TicketInfo]:
    """[summary]

    Args:
        tickets (List[TicketInfo]): ticket info with car no

    Raises:
        Exception: No seat availble.

    Returns:
        List[TicketInfo]: fully ticket info with row no and col no.
    """
    global seat_list_list
    for row_index in range(10):
        for col_index in range(1, 4):
            first_seat = seat_list_list[row_index][col_index]
            if first_seat:
                seat_list_list[row_index][col_index] = 0

                ticket = tickets[0]                      
                ticket.row_no = row_index            
                ticket.col_no = col_index
                return [ticket]

    return one_ticket_level_random_seat_strategy(tickets)


def two_ticket_level_random_seat_strategy(tickets: List[TicketInfo]) -> List[TicketInfo]:
    """[summary]

    Args:
        tickets (List[TicketInfo]): ticket info with car no

    Raises:
        Exception: No seat availble.

    Returns:
        List[TicketInfo]: fully ticket info with row no and col no.
    """
    global seat_list_list
    for row_index in range(10):
        for col_index in range(4):
            first_seat = seat_list_list[row_index][col_index: col_index+2]
            if check_have_seats(first_seat):
                seat_list_list[row_index][col_index] = 0
                seat_list_list[row_index][col_index+1] = 0
                result_ticket_list = []
                for revise_no, ticket in enumerate(tickets):
                    ticket.row_no = row_index
                    ticket.col_no = col_index+revise_no
                    result_ticket_list.append(ticket)

                return result_ticket_list

    return one_ticket_level_random_seat_strategy([tickets[0]]) + one_ticket_level_random_seat_strategy([tickets[1]])

def two_ticket_level_window_seat_strategy(tickets: List[TicketInfo]) -> List[TicketInfo]:
    """[summary]

    Args:
        tickets (List[TicketInfo]): ticket info with car no

    Raises:
        Exception: No seat availble.

    Returns:
        List[TicketInfo]: fully ticket info with row no and col no.
    """
    global seat_list_list
    for col_index in [0, 3]:
        for row_index in range(10):
            first_seat = seat_list_list[row_index][col_index: col_index+2]
            if check_have_seats(first_seat):
                seat_list_list[row_index][col_index] = 0
                seat_list_list[row_index][col_index+1] = 0
                result_ticket_list = []
                for revise_no, ticket in enumerate(tickets):
                    ticket.row_no = row_index
                    ticket.col_no = col_index+revise_no
                    result_ticket_list.append(ticket)

                return result_ticket_list
            
    return two_ticket_level_random_seat_strategy(tickets)

def two_ticket_level_aisle_seat_strategy(tickets: List[TicketInfo]) -> List[TicketInfo]:
    """[summary]

    Args:
        tickets (List[TicketInfo]): ticket info with car no

    Raises:
        Exception: No seat availble.

    Returns:
        List[TicketInfo]: fully ticket info with row no and col no.
    """
    global seat_list_list
    for row_index in range(10):
        for col_index in [1, 2]:
            first_seat = seat_list_list[row_index][col_index: col_index+2]
            if first_seat[1] == 0:
                break
            if check_have_seats(first_seat):
                seat_list_list[row_index][col_index] = 0
                seat_list_list[row_index][col_index+1] = 0
                result_ticket_list = []
                for revise_no, ticket in enumerate(tickets):
                    ticket.row_no = row_index
                    ticket.col_no = col_index+revise_no
                    result_ticket_list.append(ticket)

                return result_ticket_list

    return two_ticket_level_random_seat_strategy(tickets) 

def three_ticket_level_random_seat_strategy(tickets: List[TicketInfo]) -> List[TicketInfo]:
    """[summary]

    Args:
        tickets (List[TicketInfo]): ticket info with car no

    Raises:
        Exception: No seat availble.

    Returns:
        List[TicketInfo]: fully ticket info with row no and col no.
    """
    global seat_list_list
    for row_index in range(10):
        for col_index in range(3):
            first_seat = seat_list_list[row_index][col_index: col_index+3]
            if check_have_seats(first_seat):
                seat_list_list[row_index][col_index] = 0
                seat_list_list[row_index][col_index+1] = 0
                seat_list_list[row_index][col_index+2] = 0

                result_ticket_list = []
                for revise_no, ticket in enumerate(tickets):
                    ticket.row_no = row_index
                    ticket.col_no = col_index+revise_no
                    result_ticket_list.append(ticket)

                return result_ticket_list

    return two_ticket_level_random_seat_strategy(tickets[:2]) + one_ticket_level_random_seat_strategy(tickets[2:])

def four_ticket_level_random_seat_strategy(tickets: List[TicketInfo]) -> List[TicketInfo]:
    """[summary]

    Args:
        tickets (List[TicketInfo]): ticket info with car no

    Raises:
        Exception: No seat availble.

    Returns:
        List[TicketInfo]: fully ticket info with row no and col no.
    """
    global seat_list_list
    for row_index in range(10):
        for col_index in range(2):
            first_seat = seat_list_list[row_index][col_index: col_index+4]
            if check_have_seats(first_seat):
                seat_list_list[row_index][col_index] = 0
                seat_list_list[row_index][col_index+1] = 0
                seat_list_list[row_index][col_index+2] = 0
                seat_list_list[row_index][col_index+3] = 0

                result_ticket_list = []
                for revise_no, ticket in enumerate(tickets):
                    ticket.row_no = row_index
                    ticket.col_no = col_index+revise_no
                    result_ticket_list.append(ticket)

                return result_ticket_list

    return two_ticket_level_random_seat_strategy(tickets[:2]) + two_ticket_level_random_seat_strategy(tickets[2:])

