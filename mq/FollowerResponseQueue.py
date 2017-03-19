import queue
from logger.LoggingRoot import rootLogger


class FollowerResponseQueue:

    def __init__(self):
        self.followerResponseQueue = queue.Queue(maxsize=10000)
        pass

    def push(self, response):
        rootLogger.debug("push FollowerResponseQueue size:" + str(self.followerResponseQueue.qsize()))
        self.followerResponseQueue.put(response)

    def pull(self):
        rootLogger.debug("pull FollowerResponseQueue size:" + str(self.followerResponseQueue.qsize()))
        return self.followerResponseQueue.get()
