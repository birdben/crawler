import queue
from logger.LoggingRoot import rootLogger
from mq.BaseQueue import BaseQueue


class FollowerResponseMemoryQueue(BaseQueue):

    def __init__(self):
        self.followerResponseMemoryQueue = queue.Queue()
        pass

    def push(self, requestId, response):
        rootLogger.debug(requestId + "FollowerResponseMemoryQueue push:" + str(response))
        self.followerResponseMemoryQueue.put(response)

    def pull(self, requestId):
        response = self.followerResponseMemoryQueue.get()
        rootLogger.debug(requestId + "FollowerResponseMemoryQueue pull:" + str(response))
        return response

    def size(self):
        return self.followerResponseMemoryQueue.qsize()
