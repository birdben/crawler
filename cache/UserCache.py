from logger.LoggingRoot import rootLogger

class UserCache:

    __userInfoMap = {}

    def put(self, userId, userInfo):
        if userId not in self.__userInfoMap:
            self.__userInfoMap[userId] = userInfo

    def get(self, userId):
        if userId in self.__userInfoMap:
            return self.__userInfoMap[userId]
        return None

    def exists(self, userId):
        if userId not in self.__userInfoMap:
            return False
        else:
            return True

    def printAll(self):
        rootLogger.debug("UserCache:" + str(self.__userInfoMap))
