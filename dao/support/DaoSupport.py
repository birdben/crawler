from abc import abstractmethod, ABCMeta


class DaoSupport(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def _getConn(self):
        """Abstract Method _getConn"""
