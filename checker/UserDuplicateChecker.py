import threading
from logger.LoggingChecker import checkerLogger


class UserDuplicateChecker(threading.Thread):
    def __init__(self, threadName, userCache, userDuplicateQueue, userRequestQueue):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.userCache = userCache
        self.userDuplicateQueue = userDuplicateQueue
        self.userRequestQueue = userRequestQueue
        pass

    def run(self):
        # checkerLogger.debug("开始线程：" + self.threadName)
        self.checkUserDuplicate()
        # checkerLogger.debug("退出线程：" + self.threadName)

    def checkUserDuplicate(self):
        while True:
            checkerLogger.debug("threadName_" + self.threadName + ": start UserDuplicateChecker.checkUserDuplicate...")
            userInfo = self.userDuplicateQueue.pull()
            checkerLogger.info("threadName_" + self.threadName + ": userInfo:" + str(userInfo))
            if userInfo is None:
                continue
            userId = userInfo["userId"]
            urlToken = userInfo["urlToken"]
            if self.userCache.exists(userId):
                # 用户信息已经存在，继续读取其他DuplicateQueue的消息
                continue
            else:
                # 用户信息不存在，则添加到Cache中，也要添加到requestQueue中
                self.userCache.put(userId, userInfo)
                self.userRequestQueue.push(urlToken)
            checkerLogger.debug("threadName_" + self.threadName + ": end UserDuplicateChecker.checkUserDuplicate...")
