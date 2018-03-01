import random
import threading
import time


class TestThreadCrawlerA(threading.Thread):

    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName
        pass

    def run(self):
        while True:
            print(self.threadName + "开始执行")
            sleepTime = random.randint(1, 100)
            print(self.threadName + "休眠" + str(sleepTime) + "秒")
            time.sleep(sleepTime)
            print(self.threadName + "结束执行")
