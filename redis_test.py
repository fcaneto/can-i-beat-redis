import time
import random
import uuid
import redis

def timefunc(f):
    def f_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f.__name__ + ' took', end - start, 'seconds')
        return result
    return f_timer

redis_server = redis.StrictRedis(host='localhost', port=6379, db=0)
pipe = redis_server.pipeline(transaction=False)

KEY = "load_test"

SIZE_SAMPLE = 10000
MAX_SCORE = 100
NUM_RANGES = 10
ranges = []
for i in range(NUM_RANGES):
    ranges.append(int(i * MAX_SCORE / NUM_RANGES)) 

@timefunc
def clean():
    redis_server.zremrangebyrank(KEY, 0, 10000)

@timefunc
def run():
    with open("write.test") as sample:
        for line in sample:
            member, score = line.split()
            pipe.zadd(KEY, score, member)
    pipe.execute()

@timefunc
def query_ranges():
    for i in range(len(ranges) - 1):
        query = redis_server.zrange(KEY, ranges[i]+1, ranges[i+1])
        print("Range %s %s = %s" % (ranges[i]+1, ranges[i+1], len(query)))        

clean()
run()
query_ranges()


        



