#!/usr/bin/python3
# coding=utf-8

from cache.impl.rds.UserRedisCache import UserRedisCache
from checker.UserDuplicateChecker import UserDuplicateChecker
from core.HttpCoreFactory import HttpCoreFactory
from crawler.FollowerCrawler import FollowerCrawler
from crawler.UserCrawler import UserCrawler
from dao.DaoFactory import DaoFactory
from mq.impl.rds.FollowerRequestRedisQueue import FollowerRequestRedisQueue
from mq.impl.rds.FollowerResponseRedisQueue import FollowerResponseRedisQueue
from mq.impl.rds.UserDuplicateRedisQueue import UserDuplicateRedisQueue
from mq.impl.rds.UserRequestRedisQueue import UserRequestRedisQueue
from mq.impl.rds.UserResponseRedisQueue import UserResponseRedisQueue
from parser.FollowerParser import FollowerParser
from parser.UserParser import UserParser


class Main:

    def __init__(self):

        self.userCache = UserRedisCache()

        self.userDuplicateQueue = UserDuplicateRedisQueue()

        self.userRequestQueue = UserRequestRedisQueue()

        self.userResponseQueue = UserResponseRedisQueue()

        self.followerRequestQueue = FollowerRequestRedisQueue()

        self.followerResponseQueue = FollowerResponseRedisQueue()

        httpCoreFactory = HttpCoreFactory()
        self.client = httpCoreFactory.createHttpCore(HttpCoreFactory.HTTP_URLLIB)

        daoFactory = DaoFactory()
        self.dao = daoFactory.createUserDao(DaoFactory.MONGO)

        pass

if __name__ == "__main__":
    main = Main()

    # 设置各个处理器的线程数
    UserDuplicateCheckerThreadCount = 5
    UserParserThreadCount = 5
    UserCrawlerThreadCount = 5
    FollowerParserThreadCount = 5
    FollowerCrawlerThreadCount = 5

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
        main.followerParser = FollowerParser(threadName, main.followerRequestQueue, main.followerResponseQueue, main.userDuplicateQueue).start()

    for i in range(0, FollowerCrawlerThreadCount):
        threadName = "FollowerCrawler[" + str(i) + "]"
        # mainLogger.debug(threadName)
        main.followerCrawler = FollowerCrawler(threadName, main.followerRequestQueue, main.followerResponseQueue, main.client).start()
