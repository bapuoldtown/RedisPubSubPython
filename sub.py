import redis
import time
redis_subscribe_object = redis.Redis()
subscribe_object = redis_subscribe_object.pubsub()

subscribe_object.subscribe('GuruPublish')
print("Fetching latest message from GuruPublish Channel")

while True:
    message=subscribe_object.get_message()
    if message:
        if isinstance(message['data'],int):
            pass
        else:
            print("Getting New update")
            time.sleep(2)
            print(str(message['data'],'utf-8'))