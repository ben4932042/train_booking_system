from typing import List
from src.model.cabin_info import CabinInfo
from src.model.ticket_info import TicketInfo


class SeatStrategyHandle:
    def __init__(self, tickets: List[TicketInfo], cabin_seat_dict: dict):
        self.tickets = tickets
        self.ticket_number = len(tickets)

        self.cabin_seat_dict = self.__get_tickets_seat_dict(
            self.__get_tickets_cabin_no_set(),
            cabin_seat_dict)

    def __get_tickets_cabin_no_set(self) -> set:
        """[summary]

        Returns:
            set: car no of tickets.
        """
        return {ticket.car_number for ticket in self.tickets}

    def __get_tickets_seat_dict(self, cabin_no_set: set, cabin_seat_dict) -> dict:
        """[summary]

        Args:
            cabin_no_set (int): car no of tickets.
            cabin_seat_dict (dict): available seat no list of cabin.

        Returns:
            dict: seat status list of cabin.

        """

        default_seats_list = [0 for seat_no in range(CabinInfo.number_of_seats)]
        return_cabin_seat_dict = {}
        for cabin_no in cabin_no_set:
            seats_list = default_seats_list[:]
            for seat_no in cabin_seat_dict[f'car_{cabin_no}']:
                seats_list[seat_no] = 1
            return_cabin_seat_dict[f'car_{cabin_no}'] = [seats_list[i:i + 5] for i in range(0, len(seats_list), 5)]

        return return_cabin_seat_dict

    def check_have_seats(self, seat_list: list) -> bool:
        """[summary]

        Args:
            seat_list (list): check have any seats in required car no.

        Returns:
            bool: have any seat or not

        """
        check = True
        if sum(seat_list) != len(seat_list):
            check = False
        return check
