#!/usr/bin/python3
# coding=utf-8
import json
import time

from parser.BaseParser import BaseParser
from logger.LoggingFollowerParser import followerParserLogger


class FollowerParser(BaseParser):

    SLEEP_TIME = 2

    def __init__(self, threadName, dao, followerRequestQueue, followerResponseQueue, userDuplicateQueue):
        BaseParser.__init__(self, threadName)
        self.dao = dao
        self.followerRequestQueue = followerRequestQueue
        self.followerResponseQueue = followerResponseQueue
        self.userDuplicateQueue = userDuplicateQueue
        pass

    def parse(self):
        while True:
            time.sleep(FollowerParser.SLEEP_TIME)
            followerParserLogger.debug("threadName_" + self.threadName + ": start FollowerParser.parse...")
            response = self.followerResponseQueue.pull()
            try:
                if response["status"] == BaseParser.SUCCESS_CODE:
                    responseData = json.loads(response["data"])
                    # followerParserLogger.debug("threadName_" + self.threadName + ": responseData:" + str(responseData))
                    paging = responseData["paging"]
                    if paging is not None:
                        if not paging["is_end"]:
                            nextFollowerPageRequestUrl = paging["next"]
                            followerParserLogger.info("threadName_" + self.threadName + ": nextFollowerPageRequestUrl:" + str(nextFollowerPageRequestUrl))
                            self.followerRequestQueue.push(nextFollowerPageRequestUrl)

                    followerList = responseData["data"]
                    for follower in followerList:
                        followerId = follower["id"]
                        followerUrlToken = follower["url_token"]
                        followerInfo = {
                            "userId": followerId,
                            "urlToken": followerUrlToken
                        }
                        followerParserLogger.info("threadName_" + self.threadName + ": followerInfo:" + str(followerInfo))
                        self.dao.saveUser(followerInfo)
                        self.userDuplicateQueue.push(followerInfo)
                else:
                    followerParserLogger.debug("Response Error:" + response["reason"])
                followerParserLogger.debug("threadName_" + self.threadName + ": end FollowerParser.parse...")
            except Exception as e:
                followerParserLogger.error("解析Response出错")
                followerParserLogger.error(e)
