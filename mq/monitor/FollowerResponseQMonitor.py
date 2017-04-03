import threading

import time

from logger.monitor.LoggingFollowerResponseQMonitor import followerResponseQMonitorLogger
from mq.monitor.MonitorConfig import SLEEP_TIME


class FollowerResponseQMonitor(threading.Thread):
    def __init__(self, followerResponseQueue):
        threading.Thread.__init__(self)
        self.followerResponseQueue = followerResponseQueue
        pass

    def run(self):
        while True:
            time.sleep(SLEEP_TIME)
            followerResponseQMonitorLogger.debug(self.followerResponseQueue.size())
