import logging
from logger.monitor.LoggingMonitor import MONITOR_LOG_LEVEL, MONITOR_LOG_BASE_PATH

userRequestQMonitorLogger = logging.getLogger('userRequestQMonitorLogger')
userRequestQMonitorLogger.setLevel(MONITOR_LOG_LEVEL)

fileHandler = logging.FileHandler(MONITOR_LOG_BASE_PATH + '/logs/userRequestQMonitor.log')
fileHandler.setLevel(MONITOR_LOG_LEVEL)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(MONITOR_LOG_LEVEL)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fileHandler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)

userRequestQMonitorLogger.addHandler(fileHandler)
userRequestQMonitorLogger.addHandler(consoleHandler)
