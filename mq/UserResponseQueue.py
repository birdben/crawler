import queue
from logger.LoggingRoot import rootLogger


class UserResponseQueue:

    def __init__(self):
        self.userResponseQueue = queue.Queue(maxsize=10000)
        pass

    def push(self, requestId, response):
        rootLogger.debug(requestId + "UserResponseQueue push:" + str(response))
        self.userResponseQueue.put(response)

    def pull(self, requestId):
        response = self.userResponseQueue.get()
        rootLogger.debug(requestId + "UserResponseQueue pull:" + str(response))
        return response
