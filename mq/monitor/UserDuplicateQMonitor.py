import threading

import time

from logger.monitor.LoggingUserDuplicateQMonitor import userDuplicateQMonitorLogger


class UserDuplicateQMonitor(threading.Thread):
    def __init__(self, userDuplicateQueue):
        threading.Thread.__init__(self)
        self.userDuplicateQueue = userDuplicateQueue
        pass

    def run(self):
        while True:
            time.sleep(1)
            userDuplicateQMonitorLogger.debug(self.userDuplicateQueue.size())
