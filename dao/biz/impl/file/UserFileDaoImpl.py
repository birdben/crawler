from dao.biz.UserDao import UserDao
from dao.support.FileDaoSupport import FileDaoSupport
from logger.LoggingRoot import rootLogger


class UserFileDaoImpl(FileDaoSupport, UserDao):
    def __init__(self):
        pass

    def saveUsers(self, userInfoList):
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

    def saveUser(self, userInfo):
        pass
