from abc import abstractmethod, ABCMeta


class BaseCache(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def put(self, key, value):
        """Abstract Method put"""

    @abstractmethod
    def get(self, key):
        """Abstract Method get"""

    @abstractmethod
    def exists(self, key):
        """Abstract Method exists"""
