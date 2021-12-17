from src.api_util import APIUtil
from src.ticket_service import TicketService
from src.exception import *

import logging
import config
import requests

if __name__ == "__main__":
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s: %(message)s',
        level=logging.INFO
    )

    api_util = APIUtil(config.api_util_setting)

    while True:
        try:
            order_info = api_util.get_order_info()

            api_util.post_ticket_order(
                order_info.uuid,
                TicketService(order_info, api_util.get_cabin_available_seat_number_dict(),
                              api_util.get_available_seat_no_dict()).get_tickets_info()
            )

        except requests.exceptions.ConnectionError as err_msg:
            logging.error(f'API Server Error.')
            raise ConnectionRefusedError from err_msg
        except ResultError as err_msg:
            logging.info(f"{err_msg}")
        except SeatError as err_msg:
            logging.error(f"{err_msg}")
        except PageError as err_msg:
            logging.warning(f"{err_msg}")
            raise
        except ParamsError as err_msg:
            logging.warning(f"{err_msg}")
            raise
        else:
            logging.info(f'Success store tickets info with order for uuid: {order_info.uuid}')