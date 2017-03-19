import threading
import time
from logger.LoggingUserCrawler import userCrawlerLogger


class UserCrawler(threading.Thread):

    SLEEP_TIME = 2

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
            time.sleep(UserCrawler.SLEEP_TIME)
            userCrawlerLogger.debug("threadName_" + self.threadName + ": start UserCrawler.fetch...")
            urlToken = self.userRequestQueue.pull()
            userCrawlerLogger.info("threadName_" + self.threadName + ": urlToken:" + str(urlToken))
            request = {
                "method": "GET",
                "url": "/api/v4/members/" + urlToken + "/followers"
            }
            response = self.client.doRequest(request)
            # userCrawlerLogger.debug("threadName_" + self.threadName + ": response:" + str(response))
            self.userResponseQueue.push(response)
            userCrawlerLogger.debug("threadName_" + self.threadName + ": end UserCrawler.fetch...")
