import logging
from logger.monitor.LoggingMonitor import MONITOR_LOG_LEVEL, MONITOR_LOG_BASE_PATH

userDuplicateQMonitorLogger = logging.getLogger('userDuplicateQMonitorLogger')
userDuplicateQMonitorLogger.setLevel(MONITOR_LOG_LEVEL)

fileHandler = logging.FileHandler(MONITOR_LOG_BASE_PATH + '/logs/userDuplicateQMonitor.log')
fileHandler.setLevel(MONITOR_LOG_LEVEL)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(MONITOR_LOG_LEVEL)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fileHandler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)

userDuplicateQMonitorLogger.addHandler(fileHandler)
userDuplicateQMonitorLogger.addHandler(consoleHandler)
