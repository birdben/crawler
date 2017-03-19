from dao.FileDao import FileDao
from dao.UserDao import UserDao
from logger.LoggingRoot import rootLogger


class UserFileDaoImpl(FileDao, UserDao):

    def __init__(self):
        FileDao.__init__(self)
        UserDao.__init__(self)
        pass

    def saveUser(self, userInfo):
        # rootLogger.debug("UserFileDaoImpl saveUser...")
        userInfoString = str(userInfo)
        self.saveFile(userInfoString)

