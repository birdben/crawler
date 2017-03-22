from dao.biz.UserDao import UserDao
from dao.support.FileDaoSupport import FileDaoSupport
from logger.LoggingRoot import rootLogger


class UserFileDaoImpl(FileDaoSupport, UserDao):

    def __init__(self):
        pass

    def saveUser(self, userInfo):
        rootLogger.debug("UserFileDaoImpl saveUser start")
        rootLogger.debug("UserFileDaoImpl saveUser end")

