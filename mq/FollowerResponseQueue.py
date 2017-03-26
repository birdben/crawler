import queue
from logger.LoggingRoot import rootLogger


class FollowerResponseQueue:

    def __init__(self):
        self.followerResponseQueue = queue.Queue(maxsize=10000)
        pass

    def push(self, requestId, response):
        rootLogger.debug(requestId + "FollowerResponseQueue push:" + str(response))
        self.followerResponseQueue.put(response)

    def pull(self, requestId):
        response = self.followerResponseQueue.get()
        rootLogger.debug(requestId + "FollowerResponseQueue pull:" + str(response))
        return response
