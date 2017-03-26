from dao.support.DaoSupport import DaoSupport
from logger.LoggingRoot import rootLogger


class FileDaoSupport(DaoSupport):
    def __init__(self):
        super().__init__()

    def _getConn(self):
        rootLogger.debug("FileDaoSupport _getConn start")
        rootLogger.debug("FileDaoSupport _getConn end")
