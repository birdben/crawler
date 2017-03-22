from logger.LoggingRoot import rootLogger


class DaoSupport:
    def __init__(self):
        pass

    def getConn(self):
        rootLogger.debug("DaoSupport getConn start")
        rootLogger.debug("DaoSupport getConn end")
