import queue
from logger.LoggingRoot import rootLogger
from mq.BaseQueue import BaseQueue


class UserResponseQueue(BaseQueue):

    def __init__(self):
        self.userResponseQueue = queue.Queue()
        pass

    def push(self, requestId, response):
        rootLogger.debug(requestId + "UserResponseQueue push:" + str(response))
        self.userResponseQueue.put(response)

    def pull(self, requestId):
        response = self.userResponseQueue.get()
        rootLogger.debug(requestId + "UserResponseQueue pull:" + str(response))
        return response

    def size(self):
        return self.userResponseQueue.qsize()
