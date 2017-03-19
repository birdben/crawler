import queue
from logger.LoggingRoot import rootLogger


class UserDuplicateQueue:

    def __init__(self):
        self.userDuplicateQueue = queue.Queue(maxsize=10000)
        pass

    def push(self, message):
        rootLogger.debug("push UserDuplicateQueue size:" + str(self.userDuplicateQueue.qsize()))
        self.userDuplicateQueue.put(message)

    def pull(self):
        rootLogger.debug("pull UserDuplicateQueue size:" + str(self.userDuplicateQueue.qsize()))
        return self.userDuplicateQueue.get()
