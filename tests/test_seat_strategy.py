import os
import sys
import pytest

from src.model.ticket import TicketInfo
from src.seat_strategy import one_ticket_level_random_seat_strategy
from src.seat_strategy import one_ticket_level_window_seat_strategy
from src.seat_strategy import one_ticket_level_aisle_seat_strategy
from src.seat_strategy import two_ticket_level_random_seat_strategy
from src.seat_strategy import two_ticket_level_window_seat_strategy
from src.seat_strategy import two_ticket_level_aisle_seat_strategy
from src.seat_strategy import three_ticket_level_random_seat_strategy
from src.seat_strategy import four_ticket_level_random_seat_strategy



def test_one_ticket_level_random_seat_strategy(monkeypatch):
    monkeypatch.setattr(
            'src.seat_strategy.seat_list_list',
            [[1 for i in range(5)] for j in range(10)],
            )
    input_ticket_list = [TicketInfo(car_number=1)]
    for row_no in range(10):
        for col_no in range(5):
            ticket_list = one_ticket_level_random_seat_strategy(input_ticket_list)
            ticket = ticket_list[0]
            assert ticket.col_no == col_no
            assert ticket.row_no == row_no


    monkeypatch.setattr(
            'src.seat_strategy.seat_list_list',
            [[0 for i in range(5)] for j in range(10)],
            )

    with pytest.raises(Exception, match=r".* seat .*"):
        one_ticket_level_random_seat_strategy(input_ticket_list)


def test_one_ticket_level_window_seat_strategy(monkeypatch):
    monkeypatch.setattr(
            'src.seat_strategy.seat_list_list',
            [[1 for i in range(5)] for j in range(10)],
            )
    input_ticket_list = [TicketInfo(car_number=1)]
    for row_no in range(10):
        ticket_list = one_ticket_level_window_seat_strategy(input_ticket_list)
        for col_no, ticket in enumerate(ticket_list):
            assert ticket.col_no == col_no
            assert ticket.row_no == row_no

    for row_no in range(10):
        ticket_list = one_ticket_level_window_seat_strategy(input_ticket_list)
        for col_no, ticket in enumerate(ticket_list):
            assert ticket.col_no == 4-col_no
            assert ticket.row_no == row_no    

    monkeypatch.setattr(
            'src.seat_strategy.seat_list_list',
            [[0 for i in range(5)] for j in range(10)],
            )

    with pytest.raises(Exception, match=r".* seat .*"):
        one_ticket_level_window_seat_strategy(input_ticket_list)


def test_one_ticket_level_aisle_seat_strategy(monkeypatch):
    monkeypatch.setattr(
            'src.seat_strategy.seat_list_list',
            [[1 for i in range(5)] for j in range(10)],
            )
    input_ticket_list = [TicketInfo(car_number=1)]
    for row_no in range(10):
        for col_no in [1, 2, 3]:
            print(col_no)
            ticket_list = one_ticket_level_aisle_seat_strategy(input_ticket_list)
            ticket = ticket_list[0]
            print(ticket_list)
            print(col_no, row_no)
            assert ticket.col_no == col_no
            assert ticket.row_no == row_no

    monkeypatch.setattr(
            'src.seat_strategy.seat_list_list',
            [[0 for i in range(5)] for j in range(10)],
            )

    with pytest.raises(Exception, match=r".* seat .*"):
        one_ticket_level_aisle_seat_strategy(input_ticket_list)


def test_two_ticket_level_random_seat_strategy(monkeypatch):
    monkeypatch.setattr(
            'src.seat_strategy.seat_list_list',
            [[1 for i in range(5)] for j in range(10)],
            )
    input_ticket_list = [TicketInfo(car_number=1) for _ in range(2)]
    for row_no in range(10):
        for col_no in [0, 2]:
            ticket_list = two_ticket_level_random_seat_strategy(input_ticket_list)
            for revise_no, ticket in enumerate(ticket_list):
                assert ticket.col_no == col_no+revise_no
                assert ticket.row_no == row_no


    monkeypatch.setattr(
            'src.seat_strategy.seat_list_list',
            [[0 for i in range(5)] for j in range(10)],
            )

    with pytest.raises(Exception, match=r".* seat .*"):
        two_ticket_level_random_seat_strategy(input_ticket_list)

def test_two_ticket_level_window_seat_strategy(monkeypatch):
    monkeypatch.setattr(
            'src.seat_strategy.seat_list_list',
            [[1 for i in range(5)] for j in range(10)],
            )
    input_ticket_list = [TicketInfo(car_number=1) for _ in range(2)]
    for col_no in [0, 3]:
        for row_no in range(10):
            ticket_list = two_ticket_level_window_seat_strategy(input_ticket_list)
            for revise_no, ticket in enumerate(ticket_list):
                assert ticket.col_no == col_no+revise_no
                assert ticket.row_no == row_no


    monkeypatch.setattr(
            'src.seat_strategy.seat_list_list',
            [[0 for i in range(5)] for j in range(10)],
            )

    with pytest.raises(Exception, match=r".* seat .*"):
        two_ticket_level_window_seat_strategy(input_ticket_list)


def test_two_ticket_level_aisle_seat_strategy(monkeypatch):
    monkeypatch.setattr(
            'src.seat_strategy.seat_list_list',
            [[1 for i in range(5)] for j in range(10)],
            )
    input_ticket_list = [TicketInfo(car_number=1) for _ in range(2)]
    col_no = 1
    for row_no in range(10):
        ticket_list = two_ticket_level_aisle_seat_strategy(input_ticket_list)
        for revise_no, ticket in enumerate(ticket_list):
            assert ticket.col_no == col_no+revise_no
            assert ticket.row_no == row_no

    assert two_ticket_level_aisle_seat_strategy(input_ticket_list)

    monkeypatch.setattr(
            'src.seat_strategy.seat_list_list',
            [[0 for i in range(5)] for j in range(10)],
            )

    with pytest.raises(Exception, match=r".* seat .*"):
        two_ticket_level_aisle_seat_strategy(input_ticket_list)


def test_three_ticket_level_random_seat_strategy(monkeypatch):
    monkeypatch.setattr(
            'src.seat_strategy.seat_list_list',
            [[1 for i in range(5)] for j in range(10)],
            )
    input_ticket_list = [TicketInfo(car_number=1) for _ in range(3)]
    col_no = 0
    for row_no in range(10):
        ticket_list = three_ticket_level_random_seat_strategy(input_ticket_list)
        for revise_no, ticket in enumerate(ticket_list):
            assert ticket.col_no == col_no+revise_no
            assert ticket.row_no == row_no

    assert three_ticket_level_random_seat_strategy(input_ticket_list)

    monkeypatch.setattr(
            'src.seat_strategy.seat_list_list',
            [[0 for i in range(5)] for j in range(10)],
            )

    with pytest.raises(Exception, match=r".* seat .*"):
        three_ticket_level_random_seat_strategy(input_ticket_list)


def test_four_ticket_level_random_seat_strategy(monkeypatch):
    monkeypatch.setattr(
            'src.seat_strategy.seat_list_list',
            [[1 for i in range(5)] for j in range(10)],
            )
    input_ticket_list = [TicketInfo(car_number=1) for _ in range(4)]
    col_no = 0
    for row_no in range(10):
        ticket_list = four_ticket_level_random_seat_strategy(input_ticket_list)
        for revise_no, ticket in enumerate(ticket_list):
            assert ticket.col_no == col_no+revise_no
            assert ticket.row_no == row_no

    assert four_ticket_level_random_seat_strategy(input_ticket_list)

    monkeypatch.setattr(
            'src.seat_strategy.seat_list_list',
            [[0 for i in range(5)] for j in range(10)],
            )

    with pytest.raises(Exception, match=r".* seat .*"):
        four_ticket_level_random_seat_strategy(input_ticket_list)



