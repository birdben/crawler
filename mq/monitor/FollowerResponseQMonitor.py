import threading

import time

from logger.monitor.LoggingFollowerResponseQMonitor import followerResponseQMonitorLogger


class FollowerResponseQMonitor(threading.Thread):
    def __init__(self, followerResponseQueue):
        threading.Thread.__init__(self)
        self.followerResponseQueue = followerResponseQueue
        pass

    def run(self):
        while True:
            time.sleep(1)
            followerResponseQMonitorLogger.debug(self.followerResponseQueue.size())
