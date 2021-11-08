import os
import sys
import pytest

from src.model.ticket import TicketInfo
from src.cabin_strategy import business_cabin_strategy
from src.cabin_strategy import economy_cabin_strategy

def test_business_cabin_strategy(monkeypatch):
    #Different cabin no for each ticket  with three ticket
    monkeypatch.setattr(
        'src.cabin_strategy.all_seat_list_list',
        [[[1 for col in range(1)] for row in range(1)] for cabin in range(10)]
    )
    
    input_ticket_list = [TicketInfo(order_id='pytest') for ticket_no in range(3)]

    ticket_list = business_cabin_strategy(input_ticket_list)
    
    for ticket_index, tickets_car_number in enumerate([0, 1, 2]):
        ticket = ticket_list[ticket_index]
        assert ticket.car_number == tickets_car_number
    
    #Same cabin no for two ticket and different cabin no for one ticket with three ticket
    monkeypatch.setattr(
        'src.cabin_strategy.all_seat_list_list',
        [[[1 for col in range(2)] for row in range(1)] for cabin in range(10)]
    )
    
    input_ticket_list = [TicketInfo(order_id='pytest') for ticket_no in range(3)]
    
    ticket_list = business_cabin_strategy(input_ticket_list)
    
    for ticket_index, tickets_car_number in enumerate([0, 0, 1]):
        ticket = ticket_list[ticket_index]
        assert ticket.car_number == tickets_car_number
        
    #Not enough seats with four tickets
    monkeypatch.setattr(
        'src.cabin_strategy.all_seat_list_list',
        [[[1 for col in range(1)] for row in range(1)] for cabin in range(10)]
    )
    
    with pytest.raises(Exception, match=r".* seat .*"):
        input_ticket_list = [TicketInfo(order_id='pytest') for ticket_no in range(4)]
        ticket_list = business_cabin_strategy(input_ticket_list)
        
def test_economy_cabin_strategy(monkeypatch):
    #Different cabin no for each ticket  with three ticket
    monkeypatch.setattr(
        'src.cabin_strategy.all_seat_list_list',
        [[[1 for col in range(1)] for row in range(1)] for cabin in range(10)]
    )
    
    input_ticket_list = [TicketInfo(order_id='pytest') for ticket_no in range(3)]

    ticket_list = economy_cabin_strategy(input_ticket_list)
    
    for ticket_index, tickets_car_number in enumerate([3, 4, 5]):
        ticket = ticket_list[ticket_index]
        assert ticket.car_number == tickets_car_number
        
    #Same cabin no for two ticket and different cabin no for one ticket with three ticket
    monkeypatch.setattr(
        'src.cabin_strategy.all_seat_list_list',
        [[[1 for col in range(2)] for row in range(1)] for cabin in range(10)]
    )
    
    input_ticket_list = [TicketInfo(order_id='pytest') for ticket_no in range(3)]
    
    ticket_list = economy_cabin_strategy(input_ticket_list)
    
    for ticket_index, tickets_car_number in enumerate([3, 3, 4]):
        ticket = ticket_list[ticket_index]
        assert ticket.car_number == tickets_car_number
        
    #Not enough seats with four tickets
    monkeypatch.setattr(
        'src.cabin_strategy.all_seat_list_list',
        [[[[1 for col in range(1)] for row in range(1)] for cabin in range(5)],
         [[[0 for col in range(1)] for row in range(1)] for cabin in range(5)]]
    )
    
    with pytest.raises(Exception, match=r".* seat .*"):
        input_ticket_list = [TicketInfo(order_id='pytest') for ticket_no in range(4)]
        ticket_list = economy_cabin_strategy(input_ticket_list)