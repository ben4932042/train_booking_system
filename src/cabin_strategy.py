from typing import List
from src.model.ticket import TicketInfo

all_seat_list_list = [ [[1 for col in range(5)] for row in range(10)] for cabin in range(10)]

def cabin_strategy(
        tickets: List[TicketInfo],
        all_seat_list_list: List[list]
        )-> List[TicketInfo]:
    """[summary]

    Args:
        tickets (List[TicketInfo]): initial ticket list.
        all_seat_list_list (List[list]): initial seats.

    Raises:
        Exception: None

    Returns:
        List[TicketInfo]: ticket info with car no.
    """
    ticket_number = len(tickets)
    
    cabin_seat = [sum([sum(row) for row in singal_cabin]) for singal_cabin in all_seat_list_list[0:3]]

    if sum(cabin_seat) < ticket_number:
        raise Exception("No seat availble.")

    cabin_index_dict = dict(zip([i for i in range(3)], cabin_seat))
    
    cabin_sort_index_dict = {k: v for k, v in sorted(cabin_index_dict.items(), key=lambda item: item[1])}
    cabin_sort_index_key_list = [ _ for _ in cabin_sort_index_dict.keys()]
    
    return_ticket_list = []
    cabin_no = cabin_sort_index_key_list.pop(0)
    for ticket in tickets:
        if cabin_sort_index_dict[cabin_no] == 0:
            cabin_no = cabin_sort_index_key_list.pop(0)
        ticket.car_number = cabin_no
        cabin_sort_index_dict[cabin_no] -= 1
        return_ticket_list.append(ticket)

    return return_ticket_list
    
def economy_cabin_strategy(
        tickets: List[TicketInfo],
        all_seat_list_list: List[list]
        ) -> List[TicketInfo]:
    """[summary]

    Args:
        tickets (List[TicketInfo]): initial ticket list.
        all_seat_list_list (List[list]): initial seats.

    Raises:
        Exception: None

    Returns:
        List[TicketInfo]: ticket info with car no.
    """
    ticket_number = len(tickets)
    
    cabin_seat = [sum([sum(row) for row in singal_cabin]) for singal_cabin in all_seat_list_list[3:]]

    if sum(cabin_seat) < ticket_number:
        raise Exception("No seat availble.")

    cabin_index_dict = dict(zip([i for i in range(3, 10)], cabin_seat))
    cabin_sort_index_dict = {k: v for k, v in sorted(cabin_index_dict.items(), key=lambda item: item[1])}
    cabin_sort_index_key_list = [_ for _ in cabin_sort_index_dict.keys()]
    
    return_ticket_list = []
    cabin_no = cabin_sort_index_key_list.pop(0)
    for ticket in tickets:
        if cabin_sort_index_dict[cabin_no] == 0:
            cabin_no = cabin_sort_index_key_list.pop(0)
        ticket.car_number = cabin_no
        cabin_sort_index_dict[cabin_no] -= 1
        return_ticket_list.append(ticket)

    return return_ticket_list
