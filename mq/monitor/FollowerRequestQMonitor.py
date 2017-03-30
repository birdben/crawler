import threading

import time

from logger.monitor.LoggingFollowerRequestQMonitor import followerRequestQMonitorLogger


class FollowerRequestQMonitor(threading.Thread):
    def __init__(self, followerRequestQueue):
        threading.Thread.__init__(self)
        self.followerRequestQueue = followerRequestQueue
        pass

    def run(self):
        while True:
            time.sleep(1)
            followerRequestQMonitorLogger.debug(self.followerRequestQueue.size())
