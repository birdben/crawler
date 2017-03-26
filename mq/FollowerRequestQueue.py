import queue
from logger.LoggingRoot import rootLogger


class FollowerRequestQueue:

    def __init__(self):
        self.followerRequestQueue = queue.Queue(maxsize=10000)
        pass

    def push(self, requestId, request):
        rootLogger.debug(requestId + "FollowerRequestQueue push:" + str(request))
        self.followerRequestQueue.put(request)

    def pull(self, requestId):
        request = self.followerRequestQueue.get()
        rootLogger.debug(requestId + "FollowerRequestQueue pull:" + str(request))
        return request
