import threading
import time


class TestThreadCrawlerB(threading.Thread):

    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName
        pass

    def run(self):
        while True:
            print(self.threadName + "开始执行")
            time.sleep(100)
            print(self.threadName + "结束执行")
