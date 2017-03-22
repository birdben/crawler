from dao.support.DaoSupport import DaoSupport
from logger.LoggingRoot import rootLogger


class FileDaoSupport(DaoSupport):
    def __init__(self):
        pass

    def getConn(self):
        rootLogger.debug("FileDaoSupport getConn start")
        rootLogger.debug("FileDaoSupport getConn end")
