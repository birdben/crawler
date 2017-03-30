import queue
from logger.LoggingRoot import rootLogger
from mq.BaseQueue import BaseQueue


class FollowerResponseQueue(BaseQueue):

    def __init__(self):
        self.followerResponseQueue = queue.Queue()
        pass

    def push(self, requestId, response):
        rootLogger.debug(requestId + "FollowerResponseQueue push:" + str(response))
        self.followerResponseQueue.put(response)

    def pull(self, requestId):
        response = self.followerResponseQueue.get()
        rootLogger.debug(requestId + "FollowerResponseQueue pull:" + str(response))
        return response

    def size(self):
        return self.followerResponseQueue.qsize()
