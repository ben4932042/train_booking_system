# fake pop method

import time
import redis
import pickle
r = redis.StrictRedis(host='localhost', port=6379, db=0)
def auto_pop_redis_message(topic_name='waiting_list'):
    global r
    try:
        order_dict = pickle.loads(r.rpop('waiting_list'))
        print(order_dict)
        print('*'*20)
        uuid = order_dict.get('uuid')
        r.set(f'{uuid}', pickle.dumps(order_dict))
        # set timeout
        r.expire(f'{uuid}',60)
        
    except TypeError:
        print("topic is empty, try to pop topic message after 5's ")
        time.sleep(5)

while True:
    auto_pop_redis_message()