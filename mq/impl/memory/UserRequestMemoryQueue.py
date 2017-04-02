import queue
from logger.LoggingRoot import rootLogger
from mq.BaseQueue import BaseQueue


class UserRequestMemoryQueue(BaseQueue):

    def __init__(self):
        self.userRequestMemoryQueue = queue.Queue()
        pass

    def push(self, requestId, request):
        rootLogger.debug(requestId + "UserRequestMemoryQueue push:" + str(request))
        self.userRequestMemoryQueue.put(request)

    def pull(self, requestId):
        request = self.userRequestMemoryQueue.get()
        rootLogger.debug(requestId + "UserRequestMemoryQueue pull:" + str(request))
        return request

    def size(self):
        return self.userRequestMemoryQueue.qsize()
