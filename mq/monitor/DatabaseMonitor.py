import threading

import time

from logger.monitor.LoggingDatabaseMonitor import databaseMonitorLogger
from mq.monitor.MonitorConfig import SLEEP_TIME


class DatabaseMonitor(threading.Thread):
    def __init__(self, dao):
        threading.Thread.__init__(self)
        self.dao = dao
        pass

    def run(self):
        while True:
            time.sleep(SLEEP_TIME)
            databaseMonitorLogger.debug(self.dao.countAllUsers())
