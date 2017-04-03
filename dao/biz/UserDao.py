from abc import abstractmethod, ABCMeta


class UserDao(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def saveUser(self, userInfo):
        """Abstract Method saveUser"""

    @abstractmethod
    def saveUsers(self, userInfoList):
        """Abstract Method saveUsers"""

    @abstractmethod
    def saveOrUpdateUser(self, userInfo):
        """Abstract Method saveOrUpdateUser"""

    @abstractmethod
    def saveOrUpdateUsers(self, userInfoList):
        """Abstract Method saveOrUpdateUsers"""

    @abstractmethod
    def updateUser(self, userInfo):
        """Abstract Method updateUser"""

    @abstractmethod
    def deleteUserById(self, userId):
        """Abstract Method deleteUserById"""

    @abstractmethod
    def findUserById(self, userId):
        """Abstract Method findUserById"""

    @abstractmethod
    def findUserByCondition(self, param):
        """Abstract Method findUserByCondition"""

    @abstractmethod
    def countAllUsers(self):
        """Abstract Method countAllUsers"""
