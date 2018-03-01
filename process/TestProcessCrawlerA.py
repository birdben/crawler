import multiprocessing
import time


class TestProcessCrawlerA(multiprocessing.Process):

    def __init__(self, processName):
        multiprocessing.Process.__init__(self)
        self.processName = processName
        pass

    def run(self):
        while True:
            print(self.processName + "开始执行")
            time.sleep(random.randint(1, 5))
            print(self.processName + "结束执行")
