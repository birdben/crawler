from abc import abstractmethod, ABCMeta


class DaoSupport(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def getConn(self):
        """Abstract Method getConn"""
