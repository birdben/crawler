from abc import abstractmethod, ABCMeta


class BaseQueue(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def push(self, requestId, message):
        """Abstract Method push"""

    @abstractmethod
    def pull(self, requestId):
        """Abstract Method pull"""

    @abstractmethod
    def size(self):
        """Abstract Method size"""
