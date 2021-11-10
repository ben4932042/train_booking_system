from flask_restful import Resource
import endpoints.request_validator.store_order as store_order_validator

class Order(Resource):
    def get(self, uuid):
        return uuid
    
    def post(self):
        params = store_order_validator.vaildator().parse_args()
        
        return params