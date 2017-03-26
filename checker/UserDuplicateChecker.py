import threading

import time

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
            # 这里不涉及到爬虫时间控制，所以可以不用sleep提高效率
            requestId = "threadName_" + self.threadName + "_" + str(time.time()) + ": "
            checkerLogger.debug(requestId + "start UserDuplicateChecker.checkUserDuplicate...")
            userInfo = self.userDuplicateQueue.pull(requestId)
            checkerLogger.debug(requestId + "userInfo:" + str(userInfo))
            if userInfo is None:
                continue
            userId = userInfo["userId"]
            if self.userCache.put(requestId, userId, userInfo):
                # 添加到缓存返回True，说明缓存中用户信息不存在，要添加到requestQueue中
                self.userRequestQueue.push(requestId, userId)
            else:
                # 添加到缓存返回False，说明缓存中用户信息已经存在，继续读取其他DuplicateQueue的消息
                continue
            checkerLogger.debug(requestId + "end UserDuplicateChecker.checkUserDuplicate...")
