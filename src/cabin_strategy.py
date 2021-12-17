from typing import List

from src.model.ticket_info import TicketInfo
from src.model.cabin_info import *


class CabinStrategy:
    def __init__(self, car_type: int, tickets: List[TicketInfo], number_of_seats_dict: dict) -> None:
        """[summary]

        Args:
            car type (int): cabin strategy type.
                0 is business cabin strategy.
                1 is economy cabin strategy.

            tickets (List[TicketInfo]): ticket info with seat no.
            number_of_seats_dict (dict): number of seats in cabin.

        Returns:
            None

        """

        self.tickets = tickets

        if car_type == 0:
            cabin_no_list = BusinessCabin.cabin_no_list
            cabin_strategy = self.business_cabin_strategy
        else:
            cabin_no_list = EconomyCabin.cabin_no_list
            cabin_strategy = self.business_cabin_strategy

        cabin_strategy(self.__get_cabin_dict_with_car_type(cabin_no_list, number_of_seats_dict))

    def business_cabin_strategy(self, number_of_seats_dict: dict) -> None:
        """[summary]

        Args:
            number_of_seats_dict (dict): number of seats in cabin with car type.

        Returns:
            None

        """
        self.__check_available_number_of_seat(sum(number_of_seats_dict.values()))
        self.__check_number_of_tickets_and_seats(len(self.tickets), sum(number_of_seats_dict.values()))

        cabin_sort_index_dict = self.__sorte_cabin_dict_by_number_of_seats(number_of_seats_dict)
        cabin_sort_index_key_list = self.__get_cabin_no_list(cabin_sort_index_dict)

        self.__get_tickets_cabin_no(cabin_sort_index_dict, cabin_sort_index_key_list)

    def economy_cabin_strategy(self, number_of_seats_dict: dict) -> None:
        """[summary]

        Args:
            number_of_seats_dict (dict): number of seats in cabin with car type.

        Returns:
            None

        """

        self.__check_available_number_of_seat(sum(number_of_seats_dict.values()))
        self.__check_number_of_tickets_and_seats(len(self.tickets), sum(number_of_seats_dict.values()))

        cabin_sort_dict = self.__sorte_cabin_dict_by_number_of_seats(number_of_seats_dict)
        cabin_sort_key_list = self.__get_cabin_no_list(cabin_sort_dict)

        self.__get_tickets_cabin_no(cabin_sort_dict, cabin_sort_key_list)

    def __get_cabin_dict_with_car_type(self, cabin_no_list: list, number_of_seats_dict: dict) -> dict:
        """[summary]

        Args:
            cabin_no_list (list): cabin list with car type.
            number_of_seats_dict (dict): number_of_seats_dict (dict): number of seats in cabin.

        Returns:
            dict: cabin dict with car type.

        """
        return {f'car_{cabin_no}': number_of_seats_dict.get(f'car_{cabin_no}', 0) for cabin_no in cabin_no_list}

    def __check_available_number_of_seat(self, number_of_seat: int) -> None:
        """[summary]

        Args:
            number_of_seat (int): number of seat.

        Raises:
            Exception: all seat are booked.

        Returns:
            None

        """
        if number_of_seat == 0:
            raise Exception("All seat are booked.")

    def __check_number_of_tickets_and_seats(self, number_of_ticket: int, number_of_seat: int) -> None:
        """[summary]

        Args:
            number_of_seat (int): number of seat.
            number_of_ticket (int): number of ticket.

        Raises:
            Exception: No seat availble.

        Returns:
            None

        """

        if number_of_seat < number_of_ticket:
            raise Exception("No seat availble.")

    def __sorte_cabin_dict_by_number_of_seats(self, number_of_seats_dict: dict) -> dict:
        """[summary]

        Args:
            number_of_seats_dict (dict): cabin dict with car type.

        Returns:
            None

        """
        return {k: v for k, v in sorted(number_of_seats_dict.items(), key=lambda item: item[1], reverse=True)}

    def __get_cabin_no_list(self, cabin_sort_dict: dict) -> list:
        """[summary]

        Args:
            cabin_sort_dict (dict): cabin dict with car type sort by number of seats.

        Returns:
            list: cabin no list

        """
        return [_ for _ in cabin_sort_dict.keys()]

    def __get_tickets_cabin_no(self, cabin_sort_dict: dict, cabin_sort_key_list: list) -> None:
        """[summary]

        Args:
            cabin_sort_dict (dict): cabin dict with car type sort by number of seats.
            cabin_sort_key_list (list): cabin no list with car type sort by number of seats.

         Raises:
            Exception: Unknown logic error happened.

        Returns:
            None
        """

        cabin_no = cabin_sort_key_list.pop(0)
        for ticket in self.tickets:
            if cabin_sort_dict[cabin_no] == 0:
                cabin_no = cabin_sort_key_list.pop(0)
            if cabin_sort_dict[cabin_no] == 0:
                raise Exception("Unknown logic error happened.")
            else:
                ticket.car_number = int(cabin_no[4:])
                cabin_sort_dict[cabin_no] -= 1
