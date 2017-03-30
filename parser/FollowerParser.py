#!/usr/bin/python3
# coding=utf-8
import json
import time

from parser.BaseParser import BaseParser
from logger.LoggingFollowerParser import followerParserLogger


class FollowerParser(BaseParser):

    SLEEP_TIME = 2

    def __init__(self, threadName, followerRequestQueue, followerResponseQueue, userDuplicateQueue):
        BaseParser.__init__(self, threadName)
        self.followerRequestQueue = followerRequestQueue
        self.followerResponseQueue = followerResponseQueue
        self.userDuplicateQueue = userDuplicateQueue
        pass

    def parse(self):
        while True:
            # 不涉及到爬虫时间控制，所以可以不用sleep提高效率
            # time.sleep(FollowerParser.SLEEP_TIME)
            requestId = "threadName_" + self.threadName + "_" + str(time.time()) + ": "
            followerParserLogger.debug(requestId + "start FollowerParser.parse...")
            response = self.followerResponseQueue.pull(requestId)
            if response is None:
                continue
            try:
                if response["status"] == BaseParser.SUCCESS_CODE:
                    responseData = json.loads(response["data"])
                    followerParserLogger.debug(requestId + "responseData:" + str(responseData))
                    paging = responseData["paging"]
                    if paging is not None:
                        if not paging["is_end"]:
                            nextFollowerPageRequestUrl = paging["next"]
                            followerParserLogger.debug(requestId + "nextFollowerPageRequestUrl:" + str(nextFollowerPageRequestUrl))
                            self.followerRequestQueue.push(requestId, nextFollowerPageRequestUrl)

                    followerList = responseData["data"]
                    # 这里不能直接存储follower信息，因为不能保证唯一性，需要先解析followerId然后存入DuplicateQueue验证唯一后，在通过UserParser存储到DB
                    # self.dao.saveUsers(followerList)
                    for follower in followerList:
                        followerId = follower["id"]
                        followerName = follower["name"]
                        followerInfo = {
                            "userId": followerId,
                            "userName": followerName
                        }
                        followerParserLogger.debug(requestId + "followerInfo:" + str(followerInfo))
                        self.userDuplicateQueue.push(requestId, followerInfo)
                else:
                    followerParserLogger.debug("Response Error:" + response["reason"])
                followerParserLogger.debug(requestId + ": end FollowerParser.parse...")
            except Exception as e:
                followerParserLogger.error(requestId + "解析Response出错")
                followerParserLogger.error(e)
