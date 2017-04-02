import random
import threading
import re
import time
from logger.LoggingFollowerCrawler import followerCrawlerLogger
from urllib import request


class FollowerCrawler(threading.Thread):

    SLEEP_TIME_MIN = 1
    SLEEP_TIME_MAX = 5

    def __init__(self, threadName, followerRequestQueue, followerResponseQueue, client):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.followerRequestQueue = followerRequestQueue
        self.followerResponseQueue = followerResponseQueue
        self.client = client
        pass

    def run(self):
        # userFollowerLogger.debug("开始线程：" + self.threadName)
        self.fetch()
        # userFollowerLogger.debug("退出线程：" + self.threadName)

    def fetch(self):
        while True:
            # 这里涉及到爬虫时间控制，所以需要随机sleep时间
            time.sleep(random.randint(FollowerCrawler.SLEEP_TIME_MIN, FollowerCrawler.SLEEP_TIME_MAX))
            requestId = "threadName_" + self.threadName + "_" + str(time.time()) + ": "
            followerCrawlerLogger.debug(requestId + "start FollowerCrawler.fetch...")
            nextFollowerPageRequestObj = self.followerRequestQueue.pull(requestId)
            followerCrawlerLogger.debug(requestId + "nextFollowerPageRequestUrl:" + str(nextFollowerPageRequestObj))
            if nextFollowerPageRequestObj is None:
                continue
            nextFollowerPageRequestUrl = nextFollowerPageRequestObj["message"]
            followerObj = self.parseFollowerUrl(nextFollowerPageRequestUrl)
            followerCrawlerLogger.debug(requestId + "followerObj:" + str(followerObj))
            followerRequest = {
                "host": "api.zhihu.com",
                "method": "GET",
                "url": "/people/" + followerObj["userId"] + "/followers",
                "params": followerObj["params"],
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
            response = self.client.doRequest(requestId, followerRequest)
            followerCrawlerLogger.debug(requestId + "response:" + str(response))
            self.followerResponseQueue.push(requestId, response)
            followerCrawlerLogger.debug(requestId + "end FollowerCrawler.fetch...")

    # 抓取的不是web接口，可以不需要该方法解析url参数了
    def parseFollowerUrl(self, url):
        # url = request.unquote(url)
        # print(url)
        followerObj = {
            "userId": "",
            "params": {}
        }
        urlPattern = "https://api.zhihu.com/people/(.+?)/followers\?(.*)"
        userId = re.search(urlPattern, url).group(1)
        paramsString = re.search(urlPattern, url).group(2)
        followerCrawlerLogger.debug("userId:" + userId + ", paramsString:" + paramsString)
        params = paramsString.split("&")
        paramObj = {}
        for param in params:
            kvObj = param.split("=")
            paramName = kvObj[0]
            paramValue = kvObj[1]
            paramObj[paramName] = paramValue
        followerObj["userId"] = userId
        followerObj["params"] = paramObj
        return followerObj

if __name__ == "__main__":
    url = "https://api.zhihu.com/people/bafadeef906dcdc5b6b37397d7091665/followers?limit=20&offset=20"
    # followerObj = parseFollowerUrl(url)
    # followerCrawlerLogger.debug("followerObj:" + str(followerObj))
