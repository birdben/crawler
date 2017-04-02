import queue
from logger.LoggingRoot import rootLogger
from mq.BaseQueue import BaseQueue


class FollowerRequestMemoryQueue(BaseQueue):

    def __init__(self):
        self.followerRequestMemoryQueue = queue.Queue()
        pass

    def push(self, requestId, request):
        rootLogger.debug(requestId + "FollowerRequestMemoryQueue push:" + str(request))
        self.followerRequestMemoryQueue.put(request)

    def pull(self, requestId):
        request = self.followerRequestMemoryQueue.get()
        rootLogger.debug(requestId + "FollowerRequestMemoryQueue pull:" + str(request))
        return request

    def size(self):
        return self.followerRequestMemoryQueue.qsize()
