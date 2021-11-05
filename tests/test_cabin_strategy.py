import pytest

from src.cabin_strategy import business_cabin_strategy
from src.cabin_strategy import economy_cabin_strategy
from src.model.ticket import TicketInfo

def test_business_cabin_strategy():
    all_seat_list_list = [[[1 for col in range(5)] for row in range(10)] for cabin in range(10)]
    
    for i in range(4):
        input_ticket_list = [TicketInfo() for _ in range(i+1)]
        ticket_list = business_cabin_strategy(input_ticket_list, all_seat_list_list)
        for ticket in ticket_list:
            assert ticket.car_number == 0
    
    with pytest.raises(Exception, match=r".* seat .*"):
        input_ticket_list = [TicketInfo() for _ in range(200)]
        assert business_cabin_strategy(input_ticket_list, all_seat_list_list)

    all_seat_list_list[0] = [[0 for col in range(5)] for row in range(10)]
    for i in range(4):
        input_ticket_list = [TicketInfo() for _ in range(i+1)]
        ticket_list = business_cabin_strategy(input_ticket_list, all_seat_list_list)
        for ticket in ticket_list:
            assert ticket.car_number == 1

    all_seat_list_list[1] = [[0 for col in range(5)] for row in range(10)]

    for i in range(4):
        input_ticket_list = [TicketInfo() for _ in range(i+1)]
        ticket_list = business_cabin_strategy(input_ticket_list, all_seat_list_list)
        for ticket in ticket_list:
            assert ticket.car_number == 2

    all_seat_list_list[2] = [[0 for col in range(5)] for row in range(10)]
    for i in range(4):
        input_ticket_list = [TicketInfo() for _ in range(i+1)]
        with pytest.raises(Exception, match=r".* seat .*"):
            business_cabin_strategy(input_ticket_list, all_seat_list_list)


def test_economy_cabin_strategy():
    all_seat_list_list = [[[1 for col in range(5)] for row in range(10)] for cabin in range(10)]
    
    for i in range(4):
        input_ticket_list = [TicketInfo() for _ in range(i+1)]
        ticket_list = economy_cabin_strategy(input_ticket_list, all_seat_list_list)
        for ticket in ticket_list:
            assert ticket.car_number == 3

    with pytest.raises(Exception, match=r".* seat .*"):
        input_ticket_list = [TicketInfo() for _ in range(400)]
        assert economy_cabin_strategy(input_ticket_list, all_seat_list_list)