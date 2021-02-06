import redis
import time
redis_obj=redis.Redis()
time.sleep(2)
with open('episodelist.txt','r') as f:
    for a in f.read().splitlines():
        print("Publishing message : {}".format(a))
        redis_obj.publish('GuruPublish',str(a))
        time.sleep(4)
        



