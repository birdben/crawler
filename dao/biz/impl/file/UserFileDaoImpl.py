from dao.biz.UserDao import UserDao
from dao.support.FileDaoSupport import FileDaoSupport
from logger.LoggingRoot import rootLogger


class UserFileDaoImpl(FileDaoSupport, UserDao):
    def __init__(self):
        pass

    def _saveUsers(self, userInfoList):
        pass

    def _deleteUserById(self, userId):
        pass

    def _saveOrUpdateUser(self, userInfo):
        pass

    def _findUserById(self, userId):
        pass

    def _saveOrUpdateUsers(self, userInfoList):
        pass

    def _findUserByCondition(self, param):
        pass

    def _updateUser(self, userInfo):
        pass

    def _saveUser(self, userInfo):
        pass
