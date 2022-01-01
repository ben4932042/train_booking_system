from typing import List
from src.model.ticket_info import TicketInfo
from src.seat_strategy_factory.seat_strategy_handle import SeatStrategyHandle


class LevelRandomSeatStrategy(SeatStrategyHandle):
    def __init__(self, tickets: List[TicketInfo], cabin_seat_dict: dict):
        super(LevelRandomSeatStrategy, self).__init__(tickets, cabin_seat_dict)

    def __call__(self):
        if self.ticket_number == 1:
            self.one_ticket_level_random_seat_strategy(self.tickets)
        elif self.ticket_number == 2:
            self.two_ticket_level_random_seat_strategy(self.tickets)
        elif self.ticket_number == 3:
            self.three_ticket_level_random_seat_strategy(self.tickets)
        elif self.ticket_number == 4:
            self.four_ticket_level_random_seat_strategy(self.tickets)

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
                    if self.check_have_seats(first_seat):
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index] = False
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index + 1] = False
                        for revise_no, ticket in enumerate(tickets):
                            ticket.seat_number = (row_index * 5) + (col_index + revise_no)
                        return

        for ticket in tickets:
            self.one_ticket_level_random_seat_strategy([ticket])

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
                    if self.check_have_seats(first_seat):
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index] = 0
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index + 1] = 0
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index + 2] = 0
                        for revise_no, ticket in enumerate(tickets):
                            ticket.seat_number = (row_index * 5) + (col_index + revise_no)
                        return

        self.two_ticket_level_random_seat_strategy(tickets[:2])
        self.one_ticket_level_random_seat_strategy(tickets[2:])

    def four_ticket_level_random_seat_strategy(self, tickets: List[TicketInfo]) -> None:
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
                    if self.check_have_seats(first_seat):
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index] = 0
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index + 1] = 0
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index + 2] = 0
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index + 3] = 0
                        for revise_no, ticket in enumerate(tickets):
                            ticket.seat_number = (row_index * 5) + (col_index + revise_no)
                        return

        self.two_ticket_level_random_seat_strategy(tickets[:2])
        self.two_ticket_level_random_seat_strategy(tickets[2:])
