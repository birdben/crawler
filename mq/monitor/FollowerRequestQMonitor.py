import threading

import time

from logger.monitor.LoggingFollowerRequestQMonitor import followerRequestQMonitorLogger
from mq.monitor.MonitorConfig import SLEEP_TIME


class FollowerRequestQMonitor(threading.Thread):
    def __init__(self, followerRequestQueue):
        threading.Thread.__init__(self)
        self.followerRequestQueue = followerRequestQueue
        pass

    def run(self):
        while True:
            time.sleep(SLEEP_TIME)
            followerRequestQMonitorLogger.debug(self.followerRequestQueue.size())
