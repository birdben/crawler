from logger.LoggingMain import mainLogger
from cache.UserCache import UserCache
from checker.UserDuplicateChecker import UserDuplicateChecker
from core.HttpCoreFactory import HttpCoreFactory
from crawler.FollowerCrawler import FollowerCrawler
from crawler.UserCrawler import UserCrawler
from dao.DaoFactory import DaoFactory
from mq.FollowerRequestQueue import FollowerRequestQueue
from mq.FollowerResponseQueue import FollowerResponseQueue
from parser.FollowerParser import FollowerParser
from parser.UserParser import UserParser
from mq.UserDuplicateQueue import UserDuplicateQueue
from mq.UserRequestQueue import UserRequestQueue
from mq.UserResponseQueue import UserResponseQueue


class Main:

    def __init__(self):

        self.userCache = UserCache()

        self.userDuplicateQueue = UserDuplicateQueue()

        self.userRequestQueue = UserRequestQueue()

        self.userResponseQueue = UserResponseQueue()

        self.followerRequestQueue = FollowerRequestQueue()

        self.followerResponseQueue = FollowerResponseQueue()

        httpCoreFactory = HttpCoreFactory()
        self.client = httpCoreFactory.createHttpCore(HttpCoreFactory.HTTP_URLLIB)

        daoFactory = DaoFactory()
        self.dao = daoFactory.createUserDao(DaoFactory.FILE)

        pass

if __name__ == "__main__":
    main = Main()

    userList = [
        {"userId": "6a297a7a0fab18009e3dcd0add13fa9a", "urlToken": "chenlinux"},
        {"userId": "0c53915891637302da2599ff75af6b8c", "urlToken": "xiao-qu-69"},
        {"userId": "7bb609d065bab68b97c413181763bb71", "urlToken": "wo-pang"},
        {"userId": "2b6d37fa721f5d25153662b7e3a80a0d", "urlToken": "ding-dang-71-16"},
        {"userId": "6fad38c728e560c15a5c64b2e283be3e", "urlToken": "hong-liang-808-624"}
    ]

    # 设置各个处理器的线程数
    UserDuplicateCheckerThreadCount = 2
    UserParserThreadCount = 2
    UserCrawlerThreadCount = 2
    FollowerParserThreadCount = 2
    FollowerCrawlerThreadCount = 2

    for user in userList:
        main.userDuplicateQueue.push(user)

    for i in range(0, UserDuplicateCheckerThreadCount):
        threadName = "UserDuplicateChecker[" + str(i) + "]"
        # mainLogger.debug(threadName)
        main.userDuplicateChecker = UserDuplicateChecker(threadName, main.userCache, main.userDuplicateQueue, main.userRequestQueue).start()

    for i in range(0, UserParserThreadCount):
        threadName = "UserParser[" + str(i) + "]"
        # mainLogger.debug(threadName)
        main.userParser = UserParser(threadName, main.dao, main.userResponseQueue, main.followerRequestQueue, main.userDuplicateQueue).start()

    for i in range(0, UserCrawlerThreadCount):
        threadName = "UserCrawler[" + str(i) + "]"
        # mainLogger.debug(threadName)
        main.userCrawler = UserCrawler(threadName, main.userRequestQueue, main.userResponseQueue, main.client).start()

    for i in range(0, FollowerParserThreadCount):
        threadName = "FollowerParser[" + str(i) + "]"
        # mainLogger.debug(threadName)
        main.followerParser = FollowerParser(threadName, main.dao, main.followerRequestQueue, main.followerResponseQueue, main.userDuplicateQueue).start()

    for i in range(0, FollowerCrawlerThreadCount):
        threadName = "FollowerCrawler[" + str(i) + "]"
        # mainLogger.debug(threadName)
        main.followerCrawler = FollowerCrawler(threadName, main.followerRequestQueue, main.followerResponseQueue, main.client).start()
