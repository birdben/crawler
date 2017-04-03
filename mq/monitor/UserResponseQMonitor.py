import threading

import time

from logger.monitor.LoggingUserResponseQMonitor import userResponseQMonitorLogger
from mq.monitor.MonitorConfig import SLEEP_TIME


class UserResponseQMonitor(threading.Thread):
    def __init__(self, userResponseQueue):
        threading.Thread.__init__(self)
        self.userResponseQueue = userResponseQueue
        pass

    def run(self):
        while True:
            time.sleep(SLEEP_TIME)
            userResponseQMonitorLogger.debug(self.userResponseQueue.size())
