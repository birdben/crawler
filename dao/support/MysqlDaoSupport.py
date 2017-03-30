from dao.support.DaoSupport import DaoSupport
from logger.LoggingRoot import rootLogger


class MysqlDaoSupport(DaoSupport):
    def __init__(self):
        super().__init__()

    def getConn(self):
        rootLogger.debug("MysqlDaoSupport _getConn start")
        rootLogger.debug("MysqlDaoSupport _getConn end")
