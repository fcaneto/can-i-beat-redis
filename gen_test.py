import time
import random
import uuid

def timefunc(f):
    def f_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        return result
    return f_timer


with open("write.test", 'w') as sample:
    for _ in range(10000):
        sample.write("%s %s\n" % (random.randint(1000000, 9999999), random.randint(1, 99)))


# redis_server = redis.StrictRedis(host='localhost', port=6379, db=0)
# pipe = redis_server.pipeline(transaction=False)


