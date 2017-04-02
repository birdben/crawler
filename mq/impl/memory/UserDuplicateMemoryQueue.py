import queue
from logger.LoggingRoot import rootLogger
from mq.BaseQueue import BaseQueue


class UserDuplicateMemoryQueue(BaseQueue):

    def __init__(self):
        self.userDuplicateMemoryQueue = queue.Queue()
        pass

    def push(self, requestId, message):
        rootLogger.debug(requestId + "UserDuplicateMemoryQueue push:" + str(message))
        self.userDuplicateMemoryQueue.put(message)

    def pull(self, requestId):
        message = self.userDuplicateMemoryQueue.get()
        rootLogger.debug(requestId + "UserDuplicateMemoryQueue pull:" + str(message))
        return message

    def size(self):
        return self.userDuplicateMemoryQueue.qsize()
