import multiprocessing
import time


class TestProcessCrawlerB(multiprocessing.Process):

    def __init__(self, processName):
        multiprocessing.Process.__init__(self)
        self.processName = processName
        pass

    def run(self):
        while True:
            print(self.processName + "开始执行")
            time.sleep(10)
            print(self.processName + "结束执行")
