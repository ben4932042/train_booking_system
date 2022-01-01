from pydantic import BaseSettings

class APIUtilSettings(BaseSettings):
    API_URL: str = '127.0.0.1:9487'
    ORDER_ROUTE: str = '/api/queue/order_queue'
    TICKET_ORDER_ROUTE: str = '/api/seat_strategy/order'
    CABIN_AVAILABLE_SEAT_NO_ROUTE: str = '/api/seat_strategy/available_seat_no'
    CABIN_AVAILABLE_SEAT_NUMBER_ROUTE: str = '/api/seat_strategy/available_seat_number'
    class Config:
        env_file = '.env'
       
api_util_setting = APIUtilSettings()    
    