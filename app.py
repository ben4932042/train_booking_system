from flask import Flask
from flask_restful import Api
from endpoints.order import Order

app = Flask(__name__)
api = Api(app)
api.prefix = '/api'
api.add_resource(Order, '/order', '/order/<string:uuid>')

if __name__ == "__main__":
    app.run()