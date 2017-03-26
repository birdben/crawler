from abc import abstractmethod, ABCMeta


class UserDao(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def _saveUser(self, userInfo):
        """Abstract Method _saveUser"""

    @abstractmethod
    def _saveUsers(self, userInfoList):
        """Abstract Method _saveUsers"""

    @abstractmethod
    def _saveOrUpdateUser(self, userInfo):
        """Abstract Method _saveOrUpdateUser"""

    @abstractmethod
    def _saveOrUpdateUsers(self, userInfoList):
        """Abstract Method _saveOrUpdateUsers"""

    @abstractmethod
    def _updateUser(self, userInfo):
        """Abstract Method _updateUser"""

    @abstractmethod
    def _deleteUserById(self, userId):
        """Abstract Method _deleteUserById"""

    @abstractmethod
    def _findUserById(self, userId):
        """Abstract Method _findUserById"""

    @abstractmethod
    def _findUserByCondition(self, param):
        """Abstract Method _findUserByCondition"""
