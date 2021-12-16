from src.api_util import APIUtil, StatusError
from src.ticket_service import TicketService

import logging
import config
import requests

if __name__ == "__main__":
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s: %(message)s',
        level = logging.INFO
    )

    api_util = APIUtil(config.api_util_setting)
    order_info = api_util.get_order_info()

    while True:
        try:
            order_info = api_util.get_order_info()

            api_util.post_ticket_order(
                    order_info.uuid,
                    TicketService(
                        order_info,
                        api_util.get_cabin_available_seat_number_dict(),
                        api_util.get_available_seat_no_dict(),
                    ).get_tickets_info()
            )

        except requests.exceptions.ConnectionError as err_msg:
            logging.error(f'API Server Error.')
            raise ConnectionRefusedError from err_msg

        except StatusError as err_msg:
            logging.warning(f"{err_msg}")

        else:
            logging.info(f'Success store tickets info with order for uuid: {order_info.uuid}')