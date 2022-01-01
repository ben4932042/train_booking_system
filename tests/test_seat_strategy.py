import pytest

from src.model.cabin_info import *
from src.model.ticket_info import TicketInfo
from src.seat_strategy import SeatStrategy

def test_one_ticket_level_random_seat_strategy():
    seat_prefer = 0
    number_of_seats_dict = {f'car_{cabin}': [seat_no  for seat_no in range(CabinInfo.number_of_seats)]
                            for cabin in range(CabinInfo.number_of_cabin)}
    input_ticket_list = [TicketInfo(car_number=0) for _ in range(1)]
    seat_strategy = SeatStrategy(seat_prefer, input_ticket_list, number_of_seats_dict)
    assert seat_strategy.tickets[0].seat_number == 0

    number_of_seats_dict['car_0'] = []
    with pytest.raises(Exception, match=r".* seat .*"):
        SeatStrategy(seat_prefer, input_ticket_list, number_of_seats_dict)

def test_one_ticket_level_window_seat_strategy():
    seat_prefer = 1
    number_of_seats_dict = {f'car_{cabin}': [seat_no  for seat_no in range(CabinInfo.number_of_seats)]
                            for cabin in range(CabinInfo.number_of_cabin)}
    input_ticket_list = [TicketInfo(car_number=0) for _ in range(1)]
    seat_strategy = SeatStrategy(seat_prefer, input_ticket_list, number_of_seats_dict)
    assert seat_strategy.tickets[0].seat_number == 0

    for col_index in [0, 4]:
        for row_index in range(10):
            seat_number = (row_index * 5) + col_index
            seat_strategy = SeatStrategy(seat_prefer, input_ticket_list, number_of_seats_dict)
            assert seat_strategy.tickets[0].seat_number == seat_number
            number_of_seats_dict['car_0'].remove(seat_number)

    number_of_seats_dict['car_0'] = []
    with pytest.raises(Exception, match=r".* seat .*"):
        SeatStrategy(seat_prefer, input_ticket_list, number_of_seats_dict)

def test_one_ticket_level_aisle_seat_strategy():
    seat_prefer = 2
    number_of_seats_dict = {f'car_{cabin}': [seat_no  for seat_no in range(CabinInfo.number_of_seats)]
                            for cabin in range(CabinInfo.number_of_cabin)}
    input_ticket_list = [TicketInfo(car_number=0) for _ in range(1)]
    seat_strategy = SeatStrategy(seat_prefer, input_ticket_list, number_of_seats_dict)
    assert seat_strategy.tickets[0].seat_number == 1

    for row_index in range(10):
        for col_index in range(1, 4):
            seat_number = (row_index * 5) + col_index
            seat_strategy = SeatStrategy(seat_prefer, input_ticket_list, number_of_seats_dict)
            assert seat_strategy.tickets[0].seat_number == seat_number
            number_of_seats_dict['car_0'].remove(seat_number)

    number_of_seats_dict['car_0'] = []
    with pytest.raises(Exception, match=r".* seat .*"):
        input_ticket_list = [TicketInfo(car_number=0) for _ in range(1)]
        SeatStrategy(seat_prefer, input_ticket_list, number_of_seats_dict)

def test_two_ticket_level_random_seat_strategy():
    seat_prefer = 0
    number_of_seats_dict = {f'car_{cabin}': [seat_no  for seat_no in range(CabinInfo.number_of_seats)]
                            for cabin in range(CabinInfo.number_of_cabin)}
    input_ticket_list = [TicketInfo(car_number=0) for _ in range(2)]

    for row_index in range(10):
        for col_index in [0, 2]:
            seat_strategy = SeatStrategy(seat_prefer, input_ticket_list, number_of_seats_dict)
            for revise_no, ticket in enumerate(seat_strategy.tickets):
                assert ticket.seat_number == (row_index * 5) + (col_index + revise_no)
                number_of_seats_dict['car_0'].remove(ticket.seat_number)

    number_of_seats_dict['car_0'] = []
    with pytest.raises(Exception, match=r".* seat .*"):
        input_ticket_list = [TicketInfo(car_number=0) for _ in range(2)]
        SeatStrategy(seat_prefer, input_ticket_list, number_of_seats_dict)

def test_two_ticket_level_window_seat_strategy():
    seat_prefer = 1
    number_of_seats_dict = {f'car_{cabin}': [seat_no  for seat_no in range(CabinInfo.number_of_seats)]
                            for cabin in range(CabinInfo.number_of_cabin)}
    input_ticket_list = [TicketInfo(car_number=0) for _ in range(2)]

    for col_index in [0, 3]:
        for row_index in range(10):
            seat_strategy = SeatStrategy(seat_prefer, input_ticket_list, number_of_seats_dict)
            for revise_no, ticket in enumerate(seat_strategy.tickets):
                assert ticket.seat_number == (row_index * 5) + (col_index + revise_no)
                number_of_seats_dict['car_0'].remove(ticket.seat_number)

    number_of_seats_dict['car_0'] = []
    with pytest.raises(Exception, match=r".* seat .*"):
        SeatStrategy(seat_prefer, input_ticket_list, number_of_seats_dict)

def test_two_ticket_level_aisle_seat_strategy():
    seat_prefer = 2
    number_of_seats_dict = {f'car_{cabin}': [seat_no  for seat_no in range(CabinInfo.number_of_seats)]
                            for cabin in range(CabinInfo.number_of_cabin)}
    input_ticket_list = [TicketInfo(car_number=0) for _ in range(2)]

    for row_index in range(10):
        col_index = 1
        seat_strategy = SeatStrategy(seat_prefer, input_ticket_list, number_of_seats_dict)
        for revise_no, ticket in enumerate(seat_strategy.tickets):
            assert ticket.seat_number == (row_index * 5) + (col_index + revise_no)
            number_of_seats_dict['car_0'].remove(ticket.seat_number)

    number_of_seats_dict['car_0'] = []
    with pytest.raises(Exception, match=r".* seat .*"):
        SeatStrategy(seat_prefer, input_ticket_list, number_of_seats_dict)

def test_three_ticket_level_random_seat_strategy():
    seat_prefer = 0
    number_of_seats_dict = {f'car_{cabin}': [seat_no  for seat_no in range(CabinInfo.number_of_seats)]
                            for cabin in range(CabinInfo.number_of_cabin)}
    input_ticket_list = [TicketInfo(car_number=0) for _ in range(3)]

    for row_index in range(10):
        col_index = 0
        seat_strategy = SeatStrategy(seat_prefer, input_ticket_list, number_of_seats_dict)
        for revise_no, ticket in enumerate(seat_strategy.tickets):
            assert ticket.seat_number == (row_index * 5) + (col_index + revise_no)
            number_of_seats_dict['car_0'].remove(ticket.seat_number)

    number_of_seats_dict['car_0'] = []
    with pytest.raises(Exception, match=r".* seat .*"):
        SeatStrategy(seat_prefer, input_ticket_list, number_of_seats_dict)

def test_four_ticket_level_random_seat_strategy():
    seat_prefer = 0
    number_of_seats_dict = {f'car_{cabin}': [seat_no  for seat_no in range(CabinInfo.number_of_seats)]
                            for cabin in range(CabinInfo.number_of_cabin)}
    input_ticket_list = [TicketInfo(car_number=0) for _ in range(4)]

    for row_index in range(10):
        col_index = 0
        seat_strategy = SeatStrategy(seat_prefer, input_ticket_list, number_of_seats_dict)
        for revise_no, ticket in enumerate(seat_strategy.tickets):
            assert ticket.seat_number == (row_index * 5) + (col_index + revise_no)
            number_of_seats_dict['car_0'].remove(ticket.seat_number)

    number_of_seats_dict['car_0'] = []
    with pytest.raises(Exception, match=r".* seat .*"):
        SeatStrategy(seat_prefer, input_ticket_list, number_of_seats_dict)



