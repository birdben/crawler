import threading

import time

from logger.monitor.LoggingUserDuplicateQMonitor import userDuplicateQMonitorLogger
from mq.monitor.MonitorConfig import SLEEP_TIME


class UserDuplicateQMonitor(threading.Thread):
    def __init__(self, userDuplicateQueue):
        threading.Thread.__init__(self)
        self.userDuplicateQueue = userDuplicateQueue
        pass

    def run(self):
        while True:
            time.sleep(SLEEP_TIME)
            userDuplicateQMonitorLogger.debug(self.userDuplicateQueue.size())
