#!/usr/bin/python3
# coding=utf-8

from cache.impl.rds.UserRedisCache import UserRedisCache
from dao.DaoFactory import DaoFactory
from mq.impl.rds.FollowerRequestRedisQueue import FollowerRequestRedisQueue
from mq.impl.rds.FollowerResponseRedisQueue import FollowerResponseRedisQueue
from mq.impl.rds.UserDuplicateRedisQueue import UserDuplicateRedisQueue
from mq.impl.rds.UserRequestRedisQueue import UserRequestRedisQueue
from mq.impl.rds.UserResponseRedisQueue import UserResponseRedisQueue
from mq.monitor.DatabaseMonitor import DatabaseMonitor
from mq.monitor.FollowerRequestQMonitor import FollowerRequestQMonitor
from mq.monitor.FollowerResponseQMonitor import FollowerResponseQMonitor
from mq.monitor.UserDuplicateQMonitor import UserDuplicateQMonitor
from mq.monitor.UserRequestQMonitor import UserRequestQMonitor
from mq.monitor.UserResponseQMonitor import UserResponseQMonitor


class Monitor:

    def __init__(self):

        self.userCache = UserRedisCache()

        self.userDuplicateQueue = UserDuplicateRedisQueue()

        self.userRequestQueue = UserRequestRedisQueue()

        self.userResponseQueue = UserResponseRedisQueue()

        self.followerRequestQueue = FollowerRequestRedisQueue()

        self.followerResponseQueue = FollowerResponseRedisQueue()

        daoFactory = DaoFactory()
        self.dao = daoFactory.createUserDao(DaoFactory.MONGO)

        pass

if __name__ == "__main__":
    monitor = Monitor()

    # 启动Queue的监控日志
    monitor.followerRequestQMonitor = FollowerRequestQMonitor(monitor.followerRequestQueue).start()
    monitor.followerResponseQMonitor = FollowerResponseQMonitor(monitor.followerResponseQueue).start()
    monitor.userDuplicateQMonitor = UserDuplicateQMonitor(monitor.userDuplicateQueue).start()
    monitor.userRequestQMonitor = UserRequestQMonitor(monitor.userRequestQueue).start()
    monitor.userResponseQMonitor = UserResponseQMonitor(monitor.userResponseQueue).start()

    # 启动DB的监控日志
    monitor.databaseMonitor = DatabaseMonitor(monitor.dao).start()
