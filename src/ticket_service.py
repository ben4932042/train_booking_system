from src.model.order_info import OrderInfo
from src.model.ticket_info import TicketsOrder, TicketInfo
from src.cabin_strategy import CabinStrategy

from src.exception import SeatError
from src.seat_strategy_factory.seat_strategy_factory import SeatStrategyFactory


class TicketService:
    def __init__(self, order_info: OrderInfo, number_of_seats_dict: dict, cabin_seat_dict: dict):
        self.ticket_order = TicketsOrder(uuid=order_info.uuid)

        if order_info.autoticket:
            self.ticket_order.tickets = SeatStrategyFactory(
                order_info.prefer,
                CabinStrategy(
                    order_info.car_type,
                    [TicketInfo() for _ in range(order_info.number)],
                    number_of_seats_dict
                ).tickets,
                cabin_seat_dict
            ).tickets
        else:
            self.__check_seat_status(order_info.chosen_seats_list, cabin_seat_dict)
            self.ticket_order.tickets = [
                TicketInfo(car_number=ticket_info['car_no'], seat_number=ticket_info['seat_no']) for ticket_info in
                order_info.chosen_seats_list]

    def get_tickets_info(self) -> list:
        return [{'car_no': ticket.car_number, 'seat_no': ticket.seat_number} for ticket in self.ticket_order.tickets]

    def __check_seat_status(self, chosen_seats_list: list, cabin_seat_dict: dict):
        for ticket in chosen_seats_list:
            if ticket['seat_no'] not in cabin_seat_dict[f"car_{ticket['car_no']}"]:
                raise Exception(f'Not available seats for chosen seats list')
