import threading
import re
import time
from logger.LoggingFollowerCrawler import followerCrawlerLogger
from urllib import request


class FollowerCrawler(threading.Thread):

    SLEEP_TIME = 2

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
            time.sleep(FollowerCrawler.SLEEP_TIME)
            followerCrawlerLogger.debug("threadName_" + self.threadName + ": start FollowerCrawler.fetch...")
            nextFollowerPageRequestUrl = self.followerRequestQueue.pull()
            followerCrawlerLogger.info("threadName_" + self.threadName + ": nextFollowerPageRequestUrl:" + str(nextFollowerPageRequestUrl))
            followerObj = self.parseFollowerUrl(nextFollowerPageRequestUrl)
            followerCrawlerLogger.info("threadName_" + self.threadName + ": followerObj:" + str(followerObj))
            request = {
                "method": "GET",
                "url": "/api/v4/members/" + followerObj["urlToken"] + "/followers",
                "params": followerObj["params"]
            }
            response = self.client.doRequest(request)
            # followerCrawlerLogger.debug("threadName_" + self.threadName + ": response:" + str(response))
            self.followerResponseQueue.push(response)
            followerCrawlerLogger.debug("threadName_" + self.threadName + ": end FollowerCrawler.fetch...")

    def parseFollowerUrl(self, url):
        # url = request.unquote(url)
        # print(url)
        followerObj = {
            "urlToken": "",
            "params": {}
        }
        urlTokenPattern = "http://www.zhihu.com/api/v4/members/(.+?)/followers\?(.*)"
        urlToken = re.search(urlTokenPattern, url).group(1)
        paramsString = re.search(urlTokenPattern, url).group(2)
        followerCrawlerLogger.info("urlToken:" + urlToken + ", paramsString:" + paramsString)
        params = paramsString.split("&")
        paramObj = {}
        for param in params:
            kvObj = param.split("=")
            paramName = kvObj[0]
            paramValue = kvObj[1]
            paramObj[paramName] = paramValue
        followerObj["urlToken"] = urlToken
        followerObj["params"] = paramObj
        return followerObj

if __name__ == "__main__":
    url = "http://www.zhihu.com/api/v4/members/zhang-jia-wei/followers?include=data%5B%2A%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=1300660"
    # followerObj = parseFollowerUrl(url)
    # followerCrawlerLogger.debug("followerObj:" + str(followerObj))
