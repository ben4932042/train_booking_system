from src.model.order_info import OrderInfo
from src.model.ticket_info import TicketsOrder, TicketInfo
from src.cabin_strategy import CabinStrategy
from src.seat_strategy import SeatStrategy


class TicketService:
    def __init__(self, order_info: OrderInfo, number_of_seats_dict: dict, cabin_seat_dict: dict):
        self.ticket_order = TicketsOrder(uuid=order_info.uuid)

        self.ticket_order.tickets = SeatStrategy(
                order_info.prefer,
                CabinStrategy(
                        order_info.car_type,
                        [TicketInfo() for _ in range(order_info.number)],
                        number_of_seats_dict
                ).tickets,
                cabin_seat_dict
        ).tickets

    def get_tickets_info(self) -> list:
        return [{'car_no': ticket.car_number, 'seat_no': ticket.seat_number} for ticket in self.ticket_order.tickets]