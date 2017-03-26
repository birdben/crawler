import queue
from logger.LoggingRoot import rootLogger


class UserDuplicateQueue:

    def __init__(self):
        self.userDuplicateQueue = queue.Queue(maxsize=10000)
        pass

    def push(self, requestId, message):
        rootLogger.debug(requestId + "UserDuplicateQueue push:" + str(message))
        self.userDuplicateQueue.put(message)

    def pull(self, requestId):
        message = self.userDuplicateQueue.get()
        rootLogger.debug(requestId + "UserDuplicateQueue pull:" + str(message))
        return message
