import pytest

from src.model.cabin_info import *
from src.model.ticket import TicketInfo
from src.cabin_strategy import CabinStrategy

def test_business_cabin_strategy():
    car_type = 0
    number_of_seats_dict = {f'car_{cabin}': CabinInfo.number_of_cabin_col * CabinInfo.number_of_cabin_row for cabin in range(CabinInfo.number_of_cabin)}
    
    for i in range(4):
        input_ticket_list = [TicketInfo() for _ in range(i+1)]
        cabin_strategy = CabinStrategy(car_type, input_ticket_list, number_of_seats_dict)
        for ticket in cabin_strategy.tickets:
            assert ticket.car_number == 0
    
    with pytest.raises(Exception, match=r".* seat .*"):
        input_ticket_list = [TicketInfo() for _ in range(200)]
        assert CabinStrategy(car_type, input_ticket_list, number_of_seats_dict)

    number_of_seats_dict['car_0'] = 0
    for i in range(4):
        input_ticket_list = [TicketInfo() for _ in range(i+1)]
        cabin_strategy = CabinStrategy(car_type, input_ticket_list, number_of_seats_dict)
        for ticket in cabin_strategy.tickets:
            assert ticket.car_number == 1

    number_of_seats_dict['car_1'] = 0
    for i in range(4):
        input_ticket_list = [TicketInfo() for _ in range(i+1)]
        cabin_strategy = CabinStrategy(car_type, input_ticket_list, number_of_seats_dict)
        for ticket in cabin_strategy.tickets:
            assert ticket.car_number == 2

    number_of_seats_dict['car_2'] = 0
    for i in range(4):
        input_ticket_list = [TicketInfo() for _ in range(i+1)]
        with pytest.raises(Exception, match=r".* seat .*"):
            CabinStrategy(car_type, input_ticket_list, number_of_seats_dict)


def test_economy_cabin_strategy():
    car_type = 1
    number_of_seats_dict = {f'car_{cabin}': CabinInfo.number_of_cabin_col * CabinInfo.number_of_cabin_row for cabin in range(CabinInfo.number_of_cabin)}
    
    for i in range(4):
        input_ticket_list = [TicketInfo() for _ in range(i+1)]
        cabin_strategy = CabinStrategy(car_type, input_ticket_list, number_of_seats_dict)
        for ticket in cabin_strategy.tickets:
            assert ticket.car_number == 3

    with pytest.raises(Exception, match=r".* seat .*"):
        input_ticket_list = [TicketInfo() for _ in range(400)]
        assert CabinStrategy(car_type, input_ticket_list, number_of_seats_dict)