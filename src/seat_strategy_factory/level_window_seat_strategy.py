from typing import List
from src.model.ticket_info import TicketInfo
from src.seat_strategy_factory.level_random_seat_strategy import LevelRandomSeatStrategy


class LevelWindowSeatStrategy(LevelRandomSeatStrategy):
    def __init__(self, tickets: List[TicketInfo], cabin_seat_dict: dict):
        super(LevelWindowSeatStrategy, self).__init__(tickets, cabin_seat_dict)

    def __call__(self):
        if self.ticket_number == 1:
            self.one_ticket_level_window_seat_strategy(self.tickets)
        elif self.ticket_number == 2:
            self.two_ticket_level_window_seat_strategy(self.tickets)

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

        self.one_ticket_level_random_seat_strategy(self.tickets)

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
                    if self.check_have_seats(first_seat):
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index] = 0
                        self.cabin_seat_dict[f'car_{cabin_no}'][row_index][col_index + 1] = 0
                        for revise_no, ticket in enumerate(tickets):
                            ticket.seat_number = (row_index * 5) + (col_index + revise_no)
                        return

        self.two_ticket_level_random_seat_strategy(tickets)
