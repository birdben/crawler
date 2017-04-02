import json
import threading

import time


class RedisConsumer(threading.Thread):
    def __init__(self, redisConn, queue):
        threading.Thread.__init__(self)
        self.redisConn = redisConn
        self.queue = queue

    def run(self):
        while True:
            time.sleep(2)
            message = self.redisConn.blpop(self.queue, 0)[1]
            print("RedisConsumer get", message)
            jsonMsg = bytes.decode(message)
            print("jsonMsg:" + jsonMsg)
            msgObj = eval(jsonMsg)
            print(msgObj["userId"])
            print(msgObj["userName"])
