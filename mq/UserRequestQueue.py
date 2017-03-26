import queue
from logger.LoggingRoot import rootLogger


class UserRequestQueue:

    def __init__(self):
        self.userRequestQueue = queue.Queue(maxsize=10000)
        pass

    def push(self, requestId, request):
        rootLogger.debug(requestId + "UserRequestQueue push:" + str(request))
        self.userRequestQueue.put(request)

    def pull(self, requestId):
        request = self.userRequestQueue.get()
        rootLogger.debug(requestId + "UserRequestQueue pull:" + str(request))
        return request
