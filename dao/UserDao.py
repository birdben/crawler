from logger.LoggingRoot import rootLogger

class UserDao:
    def __init__(self):
        pass

    def saveUser(self, userInfo):
        rootLogger.debug("UserDao saveUser...")
