from typing import List

from src.model.ticket import TicketInfo
from src.model.cabin_info import *

class CabinStrategy:
    def __init__(self, car_type: int, tickets: List[TicketInfo], number_of_seats_dict: dict) -> None:
        self.tickets = tickets
        if car_type == 0:
            self.business_cabin_strategy(self.__get_cabin_dict_with_car_type(BusinessCabin.cabin_no_list, number_of_seats_dict))
        else:
            self.economy_cabin_strategy(self.__get_cabin_dict_with_car_type(EconomyCabin.cabin_no_list, number_of_seats_dict))

    def business_cabin_strategy(self, number_of_seats_dict: dict)-> None:
        
        """[summary]

        Args:            
            number_of_seats_dict (dict): number of seats in cabin.
            cabin range: 0-9
            Example: {'car_0': 50, 'car_1': 50, 'car_2': 50}

        Raises:
            Exception: "all seat are booked."
            Exception: "No seat availble."
            Exception: "Unknown logic error happened."

        Returns:
            List[TicketInfo]: ticket info with car no.
        """    
        self.__check_available_number_of_seat(sum(number_of_seats_dict.values()))
        self.__check_number_of_tickets_and_seats(len(self.tickets), sum(number_of_seats_dict.values()))

        cabin_sort_index_dict = self.__sorte_cabin_dict_by_number_of_seats(number_of_seats_dict)
        cabin_sort_index_key_list = self.__get_cabin_no_list(cabin_sort_index_dict)
        
        self.__get_tickets_cabin_no(cabin_sort_index_dict, cabin_sort_index_key_list)
        
    def economy_cabin_strategy(self, number_of_seats_dict: dict) -> None:
        """[summary]

        Args:
            number_of_seats_dict (dict): number of seats in cabin.
            cabin range: 0-9
            Example: {'car_3': 50, 'car_4': 50, 'car_5': 50}

        Raises:
            Exception: "all seat are booked."
            Exception: "No seat availble."
            Exception: "Unknown logic error happened."

        Returns:
            List[TicketInfo]: ticket info with car no.
        """
        
        self.__check_available_number_of_seat(sum(number_of_seats_dict.values()))
        self.__check_number_of_tickets_and_seats(len(self.tickets), sum(number_of_seats_dict.values()))

        cabin_sort_index_dict = self.__sorte_cabin_dict_by_number_of_seats(number_of_seats_dict)
        cabin_sort_index_key_list = self.__get_cabin_no_list(cabin_sort_index_dict)
        
        self.__get_tickets_cabin_no(cabin_sort_index_dict, cabin_sort_index_key_list)
    
    def __get_cabin_dict_with_car_type(self, cabin_no_list: list, number_of_seats_dict):
        return { f'car_{cabin_no}': number_of_seats_dict.get(f'car_{cabin_no}', 0) for cabin_no in cabin_no_list}

    def __check_available_number_of_seat(self, number_of_seat: int):
        if number_of_seat == 0:
            raise Exception("all seat are booked.")

    def __check_number_of_tickets_and_seats(self, number_of_ticket: int, seat_number: int):  
        if seat_number < number_of_ticket:
            raise Exception("No seat availble.")
    
    def __sorte_cabin_dict_by_number_of_seats(self, number_of_seats_dict):
        return {k: v for k, v in sorted(number_of_seats_dict.items(), key=lambda item: item[1], reverse=True)}
    
    def __get_cabin_no_list(self, cabin_sort_index_dict):
        return [ _ for _ in cabin_sort_index_dict.keys()]
    
    def __get_tickets_cabin_no(self, cabin_sort_index_dict, cabin_sort_index_key_list):
        cabin_no = cabin_sort_index_key_list.pop(0)
        for ticket in self.tickets:
            if cabin_sort_index_dict[cabin_no] == 0:
                cabin_no = cabin_sort_index_key_list.pop(0)
            if cabin_sort_index_dict[cabin_no] == 0:
                raise Exception("Unknown logic error happened.")
            else:
                ticket.car_number = int(cabin_no[4:])
                cabin_sort_index_dict[cabin_no] -= 1
        