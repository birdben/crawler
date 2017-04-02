import random
import threading
import time
from logger.LoggingUserCrawler import userCrawlerLogger


class UserCrawler(threading.Thread):

    SLEEP_TIME_MIN = 1
    SLEEP_TIME_MAX = 5

    def __init__(self, threadName, userRequestQueue, userResponseQueue, client):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.userRequestQueue = userRequestQueue
        self.userResponseQueue = userResponseQueue
        self.client = client
        pass

    def run(self):
        # userCrawlerLogger.debug("开始线程：" + self.threadName)
        self.fetch()
        # userCrawlerLogger.debug("退出线程：" + self.threadName)

    def fetch(self):
        while True:
            # 这里涉及到爬虫时间控制，所以需要随机sleep时间
            time.sleep(random.randint(UserCrawler.SLEEP_TIME_MIN, UserCrawler.SLEEP_TIME_MAX))
            requestId = "threadName_" + self.threadName + "_" + str(time.time()) + ": "
            userCrawlerLogger.debug(requestId + "start UserCrawler.fetch...")
            userObj = self.userRequestQueue.pull(requestId)
            userCrawlerLogger.debug(requestId + "userId:" + str(userObj))
            if userObj is None:
                continue
            userId = userObj["message"]
            userRequest = {
                "host": "api.zhihu.com",
                "method": "GET",
                "url": "/people/" + userId,
                "params": {},
                "headers": {
                    "Host": "api.zhihu.com",
                    "Authorization": "Bearer Mi4wQUFBQU9qRWdBQUFBQU1MZThYVndDeGNBQUFCaEFsVk5VbzNzV0FESHZyN1FkdU53bllZOE5tRUtMZHRXTWNEcmRB|1489305735|7b00a5eb2137cfae4ad342e47322d92e18d1d3d6",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0",
                    # "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                    "x-udid": "AADC3vF1cAuPTkgQezG76kgARvc5TuxQdrE=",
                    "Content-type": "application/x-www-form-urlencoded",
                    "Accept": "*/*",
                    "X-API-Version": "3.0.52"
                }
            }
            response = self.client.doRequest(requestId, userRequest)
            userCrawlerLogger.debug(requestId + "response:" + str(response))
            self.userResponseQueue.push(requestId, response)
            userCrawlerLogger.debug(requestId + "end UserCrawler.fetch...")
