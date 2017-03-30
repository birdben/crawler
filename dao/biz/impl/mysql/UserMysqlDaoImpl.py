from dao.biz.UserDao import UserDao
from dao.support.MysqlDaoSupport import MysqlDaoSupport


class UserMysqlDaoImpl(MysqlDaoSupport, UserDao):
    def __init__(self):
        pass

    def saveUsers(self, userInfoList):
        pass

    def saveUser(self, userInfo):
        pass

    def deleteUserById(self, userId):
        pass

    def saveOrUpdateUser(self, userInfo):
        pass

    def findUserById(self, userId):
        pass

    def saveOrUpdateUsers(self, userInfoList):
        pass

    def findUserByCondition(self, param):
        pass

    def updateUser(self, userInfo):
        pass
