from typing import List
from src.model.ticket_info import TicketInfo
from src.seat_strategy_factory.level_aisle_seat_strategy import LevelAisleSeatStrategy
from src.seat_strategy_factory.level_window_seat_strategy import LevelWindowSeatStrategy
from src.seat_strategy_factory.level_random_seat_strategy import LevelRandomSeatStrategy


class SeatStrategyFactory:
    def __init__(self, seat_prefer: int, tickets: List[TicketInfo], cabin_seat_dict: dict):
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

        if seat_prefer == 1:
            seat_strategy = LevelWindowSeatStrategy(tickets, cabin_seat_dict)
        elif seat_prefer == 2:
            seat_strategy = LevelAisleSeatStrategy(tickets, cabin_seat_dict)
        else:
            seat_strategy = LevelRandomSeatStrategy(tickets, cabin_seat_dict)

        seat_strategy()
        self.tickets = seat_strategy.tickets
