from logger.LoggingRoot import rootLogger


class UserDao:
    def __init__(self):
        pass

    def saveUser(self, userInfo):
        rootLogger.debug("UserDao saveUser...")

    def saveUsers(self, userInfoList):
        rootLogger.debug("UserDao saveUsers...")

    def updateUser(self, userInfo):
        rootLogger.debug("UserDao updateUser...")

    def deleteUserById(self, userId):
        rootLogger.debug("UserDao deleteUserById...")

    def findUserById(self, userId):
        rootLogger.debug("UserDao findUserById...")

    def findUserByCondition(self, param):
        rootLogger.debug("UserDao findUserByCondition...")
