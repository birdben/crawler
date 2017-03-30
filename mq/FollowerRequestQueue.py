import queue
from logger.LoggingRoot import rootLogger
from mq.BaseQueue import BaseQueue


class FollowerRequestQueue(BaseQueue):

    def __init__(self):
        self.followerRequestQueue = queue.Queue()
        pass

    def push(self, requestId, request):
        rootLogger.debug(requestId + "FollowerRequestQueue push:" + str(request))
        self.followerRequestQueue.put(request)

    def pull(self, requestId):
        request = self.followerRequestQueue.get()
        rootLogger.debug(requestId + "FollowerRequestQueue pull:" + str(request))
        return request

    def size(self):
        return self.followerRequestQueue.qsize()
