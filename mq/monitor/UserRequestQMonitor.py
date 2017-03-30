import threading

import time

from logger.monitor.LoggingUserRequestQMonitor import userRequestQMonitorLogger


class UserRequestQMonitor(threading.Thread):
    def __init__(self, userRequestQueue):
        threading.Thread.__init__(self)
        self.userRequestQueue = userRequestQueue
        pass

    def run(self):
        while True:
            time.sleep(1)
            userRequestQMonitorLogger.debug(self.userRequestQueue.size())
