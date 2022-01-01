import pytest
from src.model.cabin_info import *
from src.model.ticket_info import TicketInfo
from src.seat_strategy_factory.seat_strategy_factory import SeatStrategyFactory


def test_level_random_seat_strategy():
    seat_prefer = 0
    number_of_seats_dict = {f'car_{cabin}': [seat_no for seat_no in range(CabinInfo.number_of_seats)]
                            for cabin in range(CabinInfo.number_of_cabin)}

    # one tickets level random seat strategy
    input_ticket_list = [TicketInfo(car_number=0) for _ in range(1)]

    for row_index in range(10):
        for col_index in range(5):
            seat_strategy = SeatStrategyFactory(seat_prefer, input_ticket_list, number_of_seats_dict)
            for revise_no, ticket in enumerate(seat_strategy.tickets):
                assert ticket.seat_number == (row_index * 5) + (col_index + revise_no)
                number_of_seats_dict['car_0'].remove(ticket.seat_number)

    number_of_seats_dict['car_0'] = []
    with pytest.raises(Exception, match=r".* seat .*"):
        SeatStrategyFactory(seat_prefer, input_ticket_list, number_of_seats_dict)

    # two tickets level random seat strategy
    input_ticket_list = [TicketInfo(car_number=1) for _ in range(2)]

    for row_index in range(10):
        for col_index in [0, 2]:
            seat_strategy = SeatStrategyFactory(seat_prefer, input_ticket_list, number_of_seats_dict)
            for revise_no, ticket in enumerate(seat_strategy.tickets):
                assert ticket.seat_number == (row_index * 5) + (col_index + revise_no)
                number_of_seats_dict['car_1'].remove(ticket.seat_number)

    number_of_seats_dict['car_1'] = []
    with pytest.raises(Exception, match=r".* seat .*"):
        SeatStrategyFactory(seat_prefer, input_ticket_list, number_of_seats_dict)

    # three tickets level random seat strategy
    input_ticket_list = [TicketInfo(car_number=2) for _ in range(3)]

    for row_index in range(10):
        col_index = 0
        seat_strategy = SeatStrategyFactory(seat_prefer, input_ticket_list, number_of_seats_dict)

        for revise_no, ticket in enumerate(seat_strategy.tickets):
            assert ticket.seat_number == (row_index * 5) + (col_index + revise_no)
            number_of_seats_dict['car_2'].remove(ticket.seat_number)

    number_of_seats_dict['car_2'] = []
    with pytest.raises(Exception, match=r".* seat .*"):
        SeatStrategyFactory(seat_prefer, input_ticket_list, number_of_seats_dict)

    # four tickets level random seat strategy
    input_ticket_list = [TicketInfo(car_number=3) for _ in range(4)]

    for row_index in range(10):
        col_index = 0
        seat_strategy = SeatStrategyFactory(seat_prefer, input_ticket_list, number_of_seats_dict)
        for revise_no, ticket in enumerate(seat_strategy.tickets):
            assert ticket.seat_number == (row_index * 5) + (col_index + revise_no)
            number_of_seats_dict['car_3'].remove(ticket.seat_number)

    number_of_seats_dict['car_3'] = []
    with pytest.raises(Exception, match=r".* seat .*"):
        SeatStrategyFactory(seat_prefer, input_ticket_list, number_of_seats_dict)

def test_level_window_seat_strategy():
    seat_prefer = 1
    number_of_seats_dict = {f'car_{cabin}': [seat_no for seat_no in range(CabinInfo.number_of_seats)]
                            for cabin in range(CabinInfo.number_of_cabin)}

    # one tickets level window seat strategy
    input_ticket_list = [TicketInfo(car_number=0) for _ in range(1)]

    for col_index in [0, 4]:
        for row_index in range(10):
            seat_number = (row_index * 5) + col_index
            seat_strategy = SeatStrategyFactory(seat_prefer, input_ticket_list, number_of_seats_dict)
            assert seat_strategy.tickets[0].seat_number == seat_number
            number_of_seats_dict['car_0'].remove(seat_number)

    number_of_seats_dict['car_0'] = []
    with pytest.raises(Exception, match=r".* seat .*"):
        SeatStrategyFactory(seat_prefer, input_ticket_list, number_of_seats_dict)

    # two tickets level window seat strategy
    input_ticket_list = [TicketInfo(car_number=1) for _ in range(2)]

    for col_index in [0, 3]:
        for row_index in range(10):
            seat_strategy = SeatStrategyFactory(seat_prefer, input_ticket_list, number_of_seats_dict)
            print(seat_strategy.tickets)
            for revise_no, ticket in enumerate(seat_strategy.tickets):
                assert ticket.seat_number == (row_index * 5) + (col_index + revise_no)
                number_of_seats_dict['car_1'].remove(ticket.seat_number)

    number_of_seats_dict['car_1'] = []
    with pytest.raises(Exception, match=r".* seat .*"):
        SeatStrategyFactory(seat_prefer, input_ticket_list, number_of_seats_dict)

def test_level_aisle_seat_strategy():
    seat_prefer = 2
    number_of_seats_dict = {f'car_{cabin}': [seat_no for seat_no in range(CabinInfo.number_of_seats)]
                            for cabin in range(CabinInfo.number_of_cabin)}

    # one tickets level aisle seat strategy
    input_ticket_list = [TicketInfo(car_number=0) for _ in range(1)]

    for row_index in range(10):
        for col_index in range(1, 4):
            seat_number = (row_index * 5) + col_index
            seat_strategy = SeatStrategyFactory(seat_prefer, input_ticket_list, number_of_seats_dict)
            assert seat_strategy.tickets[0].seat_number == seat_number
            number_of_seats_dict['car_0'].remove(seat_number)

    number_of_seats_dict['car_0'] = []
    with pytest.raises(Exception, match=r".* seat .*"):
        SeatStrategyFactory(seat_prefer, input_ticket_list, number_of_seats_dict)

    # two tickets level aisle seat strategy
    input_ticket_list = [TicketInfo(car_number=1) for _ in range(2)]

    for row_index in range(10):
        col_index = 1
        seat_strategy = SeatStrategyFactory(seat_prefer, input_ticket_list, number_of_seats_dict)
        for revise_no, ticket in enumerate(seat_strategy.tickets):
            assert ticket.seat_number == (row_index * 5) + (col_index + revise_no)
            number_of_seats_dict['car_1'].remove(ticket.seat_number)

    number_of_seats_dict['car_1'] = []
    with pytest.raises(Exception, match=r".* seat .*"):
        SeatStrategyFactory(seat_prefer, input_ticket_list, number_of_seats_dict)