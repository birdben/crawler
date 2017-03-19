from dao.MySQLDao import MySQLDao
from dao.UserDao import UserDao
from logger.LoggingRoot import rootLogger


class UserMySQLDaoImpl(MySQLDao, UserDao):
    def __init__(self):
        pass

    def saveUser(self, userInfo):
        # rootLogger.debug("UserMySQLDaoImpl saveUser...")
        userInfoSql = str(userInfo)
        self.saveMySQL(userInfoSql)
