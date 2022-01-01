from typing import List
from src.model.ticket_info import TicketInfo
from src.model.cabin_info import *
from src.exception import SeatError


class SeatStrategy:
    def __init__(self, seat_prefer: int, tickets: List[TicketInfo], cabin_seat_dict: dict) -> None:
        """[summary]

        Args:
            seat_prefer (int): seat prefer type.
                0 is level random seat strategy.
                1 is level window seat strategy.
                2 is level aisle seat strategy.

            tickets (List[TicketInfo]): ticket info with car no.
            cabin_seat_dict (dict): available seat no list of cabin.

        Returns:
            None

        """
        self.tickets = tickets
        self.cabin_seat_dict = self.__transform_seat_list(self.__get_cabin_no_set(), cabin_seat_dict)
        seat_strategy = self.__get_prefer_seat_strategy(seat_prefer, len(tickets))
        seat_strategy(self.tickets)

    def __get_cabin_no_set(self) -> set:
        """[summary]

        Returns:
            set: car no of tickets.
        """
        return {ticket.car_number for ticket in self.tickets}

    def __transform_seat_list(self, cabin_no_set: set, cabin_seat_dict) -> dict:
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

    def __get_prefer_seat_strategy(self, seat_prefer: int, tickets_number: int):
        """[summary]

        Args:
            seat_prefer (int): seat prefer type.
            tickets_number (int): number of ticket.

        Returns:
            object: seat strategy method

        """
        if tickets_number == 4:
            number = 'four'
        elif tickets_number == 3:
            number = 'three'
        elif tickets_number == 2:
            number = 'two'
        else:
            number = 'one'

        if seat_prefer == 1:
            prefer = 'window'
        elif seat_prefer == 2:
            prefer = 'aisle'
        else:
            prefer = 'random'

        return eval(f'self.{number}_ticket_level_{prefer}_seat_strategy')

    def __check_have_seats(self, seat_list: list) -> bool:
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

    # one ticket
    def one_ticket_level_random_seat_strategy(self, tickets: List[TicketInfo]) -> None:
        """[summary]

        Args:
            tickets (List[TicketInfo]): ticket info with car no.

        Raises:
            SeatError: No seat availble.

        Returns:
            None

        """
        for ticket in tickets:
            cabin_no = ticket.car_number
            for row_index, row in enumerate(self.cabin_seat_dict[f'car_{cabin_no}']):
                for col_index, col in enumerate(row):
                    if col:
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index] = 0
                        ticket.seat_number = (row_index * 5) + col_index
                        return

        raise Exception("No seat availble.")

    def one_ticket_level_window_seat_strategy(self, tickets: List[TicketInfo]) -> None:
        """[summary]

        Args:
            tickets (List[TicketInfo]): ticket info with car no.

        Returns:
            None

        """
        for ticket in tickets:
            cabin_no = ticket.car_number
            for col_index in [0, 4]:
                for row_index in range(10):
                    if self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index]:
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index] = 0
                        ticket.seat_number = (row_index * 5) + col_index
                        return

        self.one_ticket_level_random_seat_strategy(tickets)

    def one_ticket_level_aisle_seat_strategy(self, tickets: List[TicketInfo]) -> None:
        """[summary]

        Args:
            tickets (List[TicketInfo]): ticket info with car no

        Returns:
            None

        """
        for ticket in tickets:
            cabin_no = ticket.car_number
            for row_index in range(10):
                for col_index in range(1, 4):
                    if self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index]:
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index] = 0
                        ticket.seat_number = (row_index * 5) + col_index
                        return

        self.one_ticket_level_random_seat_strategy(tickets)

    def two_ticket_level_random_seat_strategy(self, tickets: List[TicketInfo]) -> None:
        """[summary]

        Args:
            tickets (List[TicketInfo]): ticket info with car no.

        Returns:
           None

        """

        if tickets[0].car_number == tickets[1].car_number:
            cabin_no = tickets[0].car_number
            for row_index in range(10):
                for col_index in range(4):
                    first_seat = self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index:col_index + 2]
                    if self.__check_have_seats(first_seat):
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index] = False
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index + 1] = False
                        for revise_no, ticket in enumerate(tickets):
                            ticket.seat_number = (row_index * 5) + (col_index + revise_no)
                        return

        for ticket in tickets:
            self.one_ticket_level_random_seat_strategy([ticket])

    def two_ticket_level_window_seat_strategy(self, tickets: List[TicketInfo]) -> None:
        """[summary]

        Args:
            tickets (List[TicketInfo]): ticket info with car no.

        Returns:
            None

        """

        if tickets[0].car_number == tickets[1].car_number:
            cabin_no = tickets[0].car_number
            for col_index in [0, 3]:
                for row_index in range(10):
                    first_seat = self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index: col_index + 2]
                    if self.__check_have_seats(first_seat):
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index] = 0
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index + 1] = 0
                        for revise_no, ticket in enumerate(tickets):
                            ticket.seat_number = (row_index * 5) + (col_index + revise_no)
                        return

        self.two_ticket_level_random_seat_strategy(tickets)

    def two_ticket_level_aisle_seat_strategy(self, tickets: List[TicketInfo]) -> None:
        """[summary]

        Args:
            tickets (List[TicketInfo]): ticket info with car no.

        Returns:
            None

        """

        if tickets[0].car_number == tickets[1].car_number:
            cabin_no = tickets[0].car_number
            for row_index in range(10):
                for col_index in [1, 2]:
                    first_seat = self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index: col_index + 2]
                    if first_seat[1] == 0:
                        break
                    if self.__check_have_seats(first_seat):
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index] = 0
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index + 1] = 0
                        for revise_no, ticket in enumerate(tickets):
                            ticket.seat_number = (row_index * 5) + (col_index + revise_no)
                        return

        self.two_ticket_level_random_seat_strategy(tickets)

    def three_ticket_level_random_seat_strategy(self, tickets: List[TicketInfo]) -> None:
        """[summary]

        Args:
            tickets (List[TicketInfo]): ticket info with car no.

        Returns:
            None
        """
        if tickets[0].car_number == tickets[1].car_number == tickets[2].car_number:
            cabin_no = tickets[0].car_number
            for row_index in range(10):
                for col_index in range(3):
                    first_seat = self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index: col_index + 3]
                    if first_seat[1] == 0:
                        break
                    if self.__check_have_seats(first_seat):
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index] = 0
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index + 1] = 0
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index + 2] = 0
                        for revise_no, ticket in enumerate(tickets):
                            ticket.seat_number = (row_index * 5) + (col_index + revise_no)
                        return

        self.two_ticket_level_random_seat_strategy(tickets[:2])
        self.one_ticket_level_random_seat_strategy(tickets[2:])

    def four_ticket_level_random_seat_strategy(self, tickets: List[TicketInfo]) -> List[TicketInfo]:
        """[summary]

        Args:
            tickets (List[TicketInfo]): ticket info with car no

        Returns:
            None
        """

        if tickets[0].car_number == tickets[1].car_number == tickets[2].car_number == tickets[3].car_number:
            cabin_no = tickets[0].car_number
            for row_index in range(10):
                for col_index in range(2):
                    first_seat = self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index: col_index + 4]
                    if self.__check_have_seats(first_seat):
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index] = 0
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index + 1] = 0
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index + 2] = 0
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index + 3] = 0
                        for revise_no, ticket in enumerate(tickets):
                            ticket.seat_number = (row_index * 5) + (col_index + revise_no)
                        return

        self.two_ticket_level_random_seat_strategy(tickets[:2])
        self.two_ticket_level_random_seat_strategy(tickets[2:])
