import random
import threading
import time

from cache.BaseCache import BaseCache
from common.rds.RedisUtils import RedisUtils
from logger.LoggingRoot import rootLogger


class UserRedisCache(BaseCache):
    def __init__(self):
        pass

    def put(self, requestId, userId, userInfo):
        if RedisUtils.exists(userId) is False:
            RedisUtils.set(userId, userInfo)
            rootLogger.debug(requestId + "UserRedisCache put:" + str(userInfo))
            return True
        return False

    def get(self, requestId, userId):
        if RedisUtils.exists(userId) is True:
            userInfo = self.__userInfoMap[userId]
            RedisUtils.set(userId, userInfo)
            rootLogger.debug(requestId + "UserRedisCache get:" + str(userInfo))
        return userInfo

    def exists(self, userId):
        if RedisUtils.exists(userId) is False:
            exists = False
        else:
            exists = True
        return exists


class ThreadA(threading.Thread):
    def __init__(self, threadName, cache, userIdMap):
        threading.Thread.__init__(self, name=threadName)
        self.cache = cache
        self.userIdMap = userIdMap

    def run(self):
        for userId in userIdMap:
            success = self.cache.put("", userId, userIdMap[userId])
            rootLogger.debug("%s put in cache %s %s" % (threading.currentThread().getName(), userId, str(success)))
            time.sleep(random.randint(0, 10) / 10)


class ThreadB(threading.Thread):
    def __init__(self, threadName, cache, userIdMap):
        threading.Thread.__init__(self, name=threadName)
        self.cache = cache
        self.userIdMap = userIdMap

    def run(self):
        for userId in userIdMap:
            success = self.cache.put("", userId, userIdMap[userId])
            rootLogger.debug("%s put in cache %s %s" % (threading.currentThread().getName(), userId, str(success)))
            time.sleep(random.randint(0, 10) / 10)


if __name__ == "__main__":

    startTimestamp = time.time()

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

    cache = UserRedisCache()

    threadAList = []
    for x in range(0, 10):
        thread = ThreadA("UserRedisCache ThreadA" + str(x), cache, userIdMap)
        threadAList.append(thread)

    threadBList = []
    for x in range(0, 10):
        thread = ThreadB("UserRedisCache ThreadB" + str(x), cache, userIdMap)
        threadBList.append(thread)

    for thread in threadAList:
        thread.start()

    for thread in threadBList:
        thread.start()

    for thread in threadAList:
        thread.join()

    for thread in threadBList:
        thread.join()

    endTimestamp = time.time()

    # 转换成localtime
    startTimeLocal = time.localtime(startTimestamp)
    endTimeLocal = time.localtime(endTimestamp)
    # 转换成新的时间格式(2016-05-09 18:59:20)
    startTime = time.strftime("%Y-%m-%d %H:%M:%S", startTimeLocal)
    endTime = time.strftime("%Y-%m-%d %H:%M:%S", endTimeLocal)

    cost = endTimestamp - startTimestamp

    rootLogger.debug("UserRedisCache 开始时间：" + startTime)
    rootLogger.debug("UserRedisCache 结束时间：" + endTime)
    rootLogger.debug("UserMemoryCache 耗时：" + str(cost) + "秒")

    rootLogger.debug("执行完毕")
