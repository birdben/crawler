import queue
from logger.LoggingRoot import rootLogger


class UserRequestQueue:

    def __init__(self):
        self.userRequestQueue = queue.Queue(maxsize=10000)
        pass

    def push(self, request):
        rootLogger.debug("push UserRequestQueue size:" + str(self.userRequestQueue.qsize()))
        self.userRequestQueue.put(request)

    def pull(self):
        rootLogger.debug("pull UserRequestQueue size:" + str(self.userRequestQueue.qsize()))
        return self.userRequestQueue.get()
