import threading

from logger.LoggingRoot import rootLogger


class BaseCache:

    __cacheMap = {}

    def __init__(self):
        pass

    def put(self, key, value):
        if key not in self.__cacheMap.keys():
            self.__cacheMap[key] = value
            return True
        return False

    def get(self, key):
        if key in self.__cacheMap.keys():
            value = self.__cacheMap[key]
        return value

    def exists(self, key):
        if key not in self.__cacheMap.keys():
            exists = False
        else:
            exists = True
        return exists

    def printAll(self):
        rootLogger.debug("BaseCache:" + str(self.__cacheMap))
        rootLogger.debug("BaseCache count:" + str(len(self.__cacheMap.keys())))
