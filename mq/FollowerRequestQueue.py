import queue
from logger.LoggingRoot import rootLogger


class FollowerRequestQueue:

    def __init__(self):
        self.followerRequestQueue = queue.Queue(maxsize=10000)
        pass

    def push(self, request):
        rootLogger.debug("push FollowerRequestQueue size:" + str(self.followerRequestQueue.qsize()))
        self.followerRequestQueue.put(request)

    def pull(self):
        rootLogger.debug("pull FollowerRequestQueue size:" + str(self.followerRequestQueue.qsize()))
        return self.followerRequestQueue.get()
