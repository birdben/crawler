import random
import threading

import time

from cache.BaseCache import BaseCache
from logger.LoggingRoot import rootLogger


class UserMemoryCache(BaseCache):
    __userInfoMap = {}

    def __init__(self):
        pass

    def put(self, requestId, userId, userInfo):
        if userId not in self.__userInfoMap.keys():
            self.__userInfoMap[userId] = userInfo
            rootLogger.debug(requestId + "UserMemoryCache put:" + str(userInfo))
            return True
        return False

    def get(self, requestId, userId):
        if userId in self.__userInfoMap.keys():
            userInfo = self.__userInfoMap[userId]
            rootLogger.debug(requestId + "UserMemoryCache get:" + str(userInfo))
        return userInfo

    def exists(self, userId):
        if userId not in self.__userInfoMap.keys():
            exists = False
        else:
            exists = True
        return exists

    def printAll(self):
        rootLogger.debug("UserMemoryCache:" + str(self.__userInfoMap))
        rootLogger.debug("UserMemoryCache count:" + str(len(self.__userInfoMap.keys())))


class ThreadA(threading.Thread):
    def __init__(self, threadName, cache, userIdMap):
        threading.Thread.__init__(self, name=threadName)
        self.cache = cache
        self.userIdMap = userIdMap

    def run(self):
        for userId in userIdMap:
            success = self.cache.put(userId, userIdMap[userId])
            rootLogger.debug("%s put in cache %s %s" % (threading.currentThread().getName(), userId, str(success)))
            time.sleep(random.randint(0, 10) / 10)


class ThreadB(threading.Thread):
    def __init__(self, threadName, cache, userIdMap):
        threading.Thread.__init__(self, name=threadName)
        self.cache = cache
        self.userIdMap = userIdMap

    def run(self):
        for userId in userIdMap:
            success = self.cache.put(userId, userIdMap[userId])
            rootLogger.debug("%s put in cache %s %s" % (threading.currentThread().getName(), userId, str(success)))
            time.sleep(random.randint(0, 10) / 10)


if __name__ == "__main__":

    userIdMap = {}
    for x in range(0, 1000):
        userId = "userId" + str(x)
        userName = "userName" + str(x)
        userInfo = {
            "userId": userId,
            "userName": userName
        }
        userIdMap[userId] = userInfo

    rootLogger.debug(userIdMap)

    cache = UserMemoryCache()

    threadAList = []
    for x in range(0, 10):
        thread = ThreadA("ThreadA" + str(x), cache, userIdMap)
        threadAList.append(thread)

    threadBList = []
    for x in range(0, 10):
        thread = ThreadB("ThreadB" + str(x), cache, userIdMap)
        threadBList.append(thread)

    for thread in threadAList:
        thread.start()

    for thread in threadBList:
        thread.start()

    for thread in threadAList:
        thread.join()

    for thread in threadBList:
        thread.join()

    cache.printAll()
