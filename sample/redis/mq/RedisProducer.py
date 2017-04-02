import threading

import time


class RedisProducer(threading.Thread):
    def __init__(self, redisConn, queue):
        threading.Thread.__init__(self)
        self.redisConn = redisConn
        self.queue = queue

    def run(self):
        while True:
            time.sleep(2)
            timestamp = time.time()
            self.redisConn.lpush(self.queue, timestamp)
