from flask import Flask, request, jsonify, abort, Response, redirect, url_for
import random
import time
from dataclasses import dataclass, field
import redis
import pickle

@dataclass
class ChoiseSeat:
    autoticket: bool
    uuid: str
    prefer: int = ''
    car_type: int = ''
    number: int = ''
    chosen_seats_list: list = ''
    
    def __post_init__(self):
        if self.autoticket and self.chosen_seats_list:
            raise TypeError("auto choice ticket do not need chosen_seats_list.")
        elif not self.autoticket and not self.chosen_seats_list:
            raise TypeError("lost chosen_seats_list.")
        if not self.autoticket:
            if not (self.prefer or self.car_type or self.number):
                raise TypeError("unuse param exist.")
        if self.prefer not in [1, 2]:
            raise TypeError('unknown prefer mode')
        if self.car_type not in [0, 1]:
            raise TypeError('unknown car_type mode')
        if self.number not in [1, 2, 3, 4]:
            raise TypeError('unknown ticket number.')        
            
app = Flask(__name__)
r = redis.StrictRedis(host='localhost', port=6379, db=0)
@app.route("/test", methods=['GET'])
def test():
    global r
    try:
        order = ChoiseSeat(
                    autoticket=True,
                    uuid=request.args.get('uuid'),
                    prefer = random.choice([1, 2, 3]),
                    car_type = random.choice([0, 1, 2]),
                    number = random.choice([1, 2, 3, 4, 5]),
                    )
    except TypeError:
        abort(403)
    else:
        r.lpush('waiting_list', pickle.dumps(vars(order)))
        return  redirect(url_for(f'wait', uuid=order.uuid))      

@app.route("/wait", methods=['GET'])
def wait():
    uuid = request.args.get('uuid')
    result = None
    timeout_start = time.time()
    timeout = 20
    while time.time() < timeout_start + timeout:
        result = r.get(str(uuid))
        if result:
            break
    if result:
        return jsonify(pickle.loads(result))
    else:
        abort(500) 

if __name__ == "__main__":
    app.run()