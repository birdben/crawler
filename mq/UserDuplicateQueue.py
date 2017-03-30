import queue
from logger.LoggingRoot import rootLogger
from mq.BaseQueue import BaseQueue


class UserDuplicateQueue(BaseQueue):

    def __init__(self):
        self.userDuplicateQueue = queue.Queue()
        pass

    def push(self, requestId, message):
        rootLogger.debug(requestId + "UserDuplicateQueue push:" + str(message))
        self.userDuplicateQueue.put(message)

    def pull(self, requestId):
        message = self.userDuplicateQueue.get()
        rootLogger.debug(requestId + "UserDuplicateQueue pull:" + str(message))
        return message

    def size(self):
        return self.userDuplicateQueue.qsize()
