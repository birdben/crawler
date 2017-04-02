import threading

import time


class RedisConsumer(threading.Thread):
    def __init__(self, redisConn, queue):
        threading.Thread.__init__(self)
        self.redisConn = redisConn
        self.queue = queue

    def run(self):
        while True:
            time.sleep(5)
            task = self.redisConn.blpop(self.queue, 0)[1]
            print("Task get", task)
