import queue
from logger.LoggingRoot import rootLogger
from mq.BaseQueue import BaseQueue


class UserResponseMemoryQueue(BaseQueue):

    def __init__(self):
        self.userResponseMemoryQueue = queue.Queue()
        pass

    def push(self, requestId, response):
        rootLogger.debug(requestId + "UserResponseMemoryQueue push:" + str(response))
        self.userResponseMemoryQueue.put(response)

    def pull(self, requestId):
        response = self.userResponseMemoryQueue.get()
        rootLogger.debug(requestId + "UserResponseMemoryQueue pull:" + str(response))
        return response

    def size(self):
        return self.userResponseMemoryQueue.qsize()
