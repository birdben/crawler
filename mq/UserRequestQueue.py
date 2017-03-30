import queue
from logger.LoggingRoot import rootLogger
from mq.BaseQueue import BaseQueue


class UserRequestQueue(BaseQueue):

    def __init__(self):
        self.userRequestQueue = queue.Queue()
        pass

    def push(self, requestId, request):
        rootLogger.debug(requestId + "UserRequestQueue push:" + str(request))
        self.userRequestQueue.put(request)

    def pull(self, requestId):
        request = self.userRequestQueue.get()
        rootLogger.debug(requestId + "UserRequestQueue pull:" + str(request))
        return request

    def size(self):
        return self.userRequestQueue.qsize()
