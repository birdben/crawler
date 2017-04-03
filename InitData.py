#!/usr/bin/python3
# coding=utf-8

import time

from mq.impl.rds.UserDuplicateRedisQueue import UserDuplicateRedisQueue


class InitData:

    def __init__(self):
        self.userDuplicateQueue = UserDuplicateRedisQueue()
        pass

if __name__ == "__main__":
    initData = InitData()

    userList = [
        {"userId": "6a297a7a0fab18009e3dcd0add13fa9a", "urlToken": "chenlinux"},
        {"userId": "0c53915891637302da2599ff75af6b8c", "urlToken": "xiao-qu-69"},
        {"userId": "7bb609d065bab68b97c413181763bb71", "urlToken": "wo-pang"},
        {"userId": "2b6d37fa721f5d25153662b7e3a80a0d", "urlToken": "ding-dang-71-16"},
        {"userId": "6fad38c728e560c15a5c64b2e283be3e", "urlToken": "hong-liang-808-624"}
    ]

    requestId = "threadName_" + "Main" + "_" + str(time.time()) + ": "
    for user in userList:
        initData.userDuplicateQueue.push(requestId, user)
