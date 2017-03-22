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
            time.sleep(UserParser.SLEEP_TIME)
            userParserLogger.debug("threadName_" + self.threadName + ": start UserParser.parse...")
            response = self.userResponseQueue.pull()
            try:
                if response["status"] == BaseParser.SUCCESS_CODE:
                    responseData = json.loads(response["data"])
                    # userParserLogger.debug("threadName_" + self.threadName + ": responseData:" + str(responseData))
                    paging = responseData["paging"]
                    if paging is not None:
                        if not paging["is_end"]:
                            nextFollowerPageRequestUrl = paging["next"]
                            userParserLogger.info("threadName_" + self.threadName + ": nextFollowerPageRequestUrl:" + str(nextFollowerPageRequestUrl))
                            self.followerRequestQueue.push(nextFollowerPageRequestUrl)

                    followerList = responseData["data"]
                    self.dao.saveUsers(followerList)
                    for follower in followerList:
                        followerId = follower["id"]
                        followerUrlToken = follower["url_token"]
                        followerInfo = {
                            "userId": followerId,
                            "urlToken": followerUrlToken
                        }
                        userParserLogger.info("threadName_" + self.threadName + ": followerInfo:" + str(followerInfo))
                        self.userDuplicateQueue.push(followerInfo)
                else:
                    userParserLogger.debug("Response Error:" + response["reason"])
                userParserLogger.debug("threadName_" + self.threadName + ": end UserParser.parse...")
            except Exception as e:
                userParserLogger.error("解析Response出错")
                userParserLogger.error(e)
