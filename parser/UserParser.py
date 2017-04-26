#!/usr/bin/python3
# coding=utf-8

import json
import time

from parser.BaseParser import BaseParser
from logger.LoggingUserParser import userParserLogger


class UserParser(BaseParser):

    SLEEP_TIME = 2

    def __init__(self, threadName, dao, userResponseQueue, followerRequestQueue, userDuplicateQueue):
        BaseParser.__init__(self, threadName)
        self.dao = dao
        self.userResponseQueue = userResponseQueue
        self.followerRequestQueue = followerRequestQueue
        self.userDuplicateQueue = userDuplicateQueue
        pass

    def parse(self):
        while True:
            # 这里不涉及到爬虫时间控制，所以可以不用sleep提高效率
            # time.sleep(UserParser.SLEEP_TIME)
            requestId = "threadName_" + self.threadName + "_" + str(time.time()) + ": "
            userParserLogger.debug(requestId + "start UserParser.parse...")
            response = self.userResponseQueue.pull(requestId)
            if response is None:
                continue
            try:
                if response["status"] == BaseParser.SUCCESS_CODE:
                    userInfo = json.loads(response["data"])
                    userId = userInfo["id"]
                    userParserLogger.debug(requestId + "userInfo:" + str(userInfo))
                    self.dao.saveUser(requestId, userInfo)

                    # 初始化follower接口参数，并且存储到followerRequestQueue中
                    followerUrl = "https://api.zhihu.com/people/" + userId + "/followers?limit=20&offset=0"
                    userParserLogger.debug(requestId + "followerUrl:" + str(followerUrl))
                    followerObj = {
                        "message": followerUrl
                    }
                    self.followerRequestQueue.push(requestId, followerObj)
                else:
                    userParserLogger.debug("Response Error:" + response["reason"])
                userParserLogger.debug(requestId + "end UserParser.parse...")
            except Exception as e:
                userParserLogger.error(requestId + "解析Response出错")
                userParserLogger.error(e)
