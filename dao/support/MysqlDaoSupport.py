from dao.support.DaoSupport import DaoSupport
from logger.LoggingRoot import rootLogger


class MysqlDaoSupport(DaoSupport):
    def __init__(self):
        pass

    def getConn(self):
        rootLogger.debug("MysqlDaoSupport getConn start")
        rootLogger.debug("MysqlDaoSupport getConn end")
