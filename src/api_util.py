import requests
from typing import List
from src.model.order_info import OrderInfo
from src.exception import ResultError, PageError, ParamsError


class APIUtil:
    def __init__(self, config) -> None:
        self.api_url = config.API_URL
        self.order_route = config.ORDER_ROUTE
        self.ticket_order_route = config.TICKET_ORDER_ROUTE
        self.cabin_available_seat_no_route = config.CABIN_AVAILABLE_SEAT_NO_ROUTE
        self.cabin_available_seat_number_route = config.CABIN_AVAILABLE_SEAT_NUMBER_ROUTE

    def check_http_status_code(self, response, route):
        if response.status_code == 204:
            raise ResultError(f'Request success but result error. route: {route}. Error message: {response.text}')
        elif response.status_code == 404:
            raise PageError(f'Invalid api request. route: {route}. Error message: {response.text}')
        elif response.status_code == 422:
            raise ParamsError(f'Api request params error. route: {route}. Error message: {response.text}')

    def get_order_info(self) -> OrderInfo:
        response = requests.get(self.api_url + self.order_route)
        self.check_http_status_code(response, self.order_route)
        return OrderInfo(**response.json())

    def get_available_seat_no_dict(self) -> dict:
        response = requests.get(self.api_url + self.cabin_available_seat_no_route)
        self.check_http_status_code(response, self.cabin_available_seat_no_route)
        return response.json()

    def get_cabin_available_seat_number_dict(self) -> dict:
        response = requests.get(self.api_url + self.cabin_available_seat_number_route)
        self.check_http_status_code(response, self.cabin_available_seat_number_route)
        return response.json()

    def post_ticket_order(self, uuid: str, cabin_no_with_seat_no_list_dict: List[dict]):
        response = requests.post(
            self.api_url + self.ticket_order_route,
            params={'uuid': uuid},
            json=cabin_no_with_seat_no_list_dict)
        self.check_http_status_code(response, self.ticket_order_route)
