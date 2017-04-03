import logging
from logger.monitor.LoggingMonitor import MONITOR_LOG_LEVEL, MONITOR_LOG_BASE_PATH

userResponseQMonitorLogger = logging.getLogger('userResponseQMonitorLogger')
userResponseQMonitorLogger.setLevel(MONITOR_LOG_LEVEL)

fileHandler = logging.FileHandler(MONITOR_LOG_BASE_PATH + '/logs/userResponseQMonitor.log')
fileHandler.setLevel(MONITOR_LOG_LEVEL)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(MONITOR_LOG_LEVEL)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fileHandler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)

userResponseQMonitorLogger.addHandler(fileHandler)
userResponseQMonitorLogger.addHandler(consoleHandler)
