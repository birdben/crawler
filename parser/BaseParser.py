import threading
from logger.LoggingRoot import rootLogger


class BaseParser(threading.Thread):

    SUCCESS_CODE = 200

    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName
        pass

    def parse(self):
        rootLogger.debug("BaseParser response...")

    def run(self):
        # rootLogger.debug("开始线程：" + self.threadName)
        self.parse()
        # rootLogger.debug("退出线程：" + self.threadName)
