import queue
from logger.LoggingRoot import rootLogger


class UserResponseQueue:

    def __init__(self):
        self.userResponseQueue = queue.Queue(maxsize=10000)
        pass

    def push(self, response):
        rootLogger.debug("push UserResponseQueue size:" + str(self.userResponseQueue.qsize()))
        self.userResponseQueue.put(response)

    def pull(self):
        rootLogger.debug("pull UserResponseQueue size:" + str(self.userResponseQueue.qsize()))
        return self.userResponseQueue.get()
