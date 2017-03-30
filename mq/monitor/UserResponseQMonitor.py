import threading

import time

from logger.monitor.LoggingUserResponseQMonitor import userResponseQMonitorLogger


class UserResponseQMonitor(threading.Thread):
    def __init__(self, userResponseQueue):
        threading.Thread.__init__(self)
        self.userResponseQueue = userResponseQueue
        pass

    def run(self):
        while True:
            time.sleep(1)
            userResponseQMonitorLogger.debug(self.userResponseQueue.size())
