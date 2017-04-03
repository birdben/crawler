import threading

import time

from logger.monitor.LoggingUserRequestQMonitor import userRequestQMonitorLogger
from mq.monitor.MonitorConfig import SLEEP_TIME


class UserRequestQMonitor(threading.Thread):
    def __init__(self, userRequestQueue):
        threading.Thread.__init__(self)
        self.userRequestQueue = userRequestQueue
        pass

    def run(self):
        while True:
            time.sleep(SLEEP_TIME)
            userRequestQMonitorLogger.debug(self.userRequestQueue.size())
