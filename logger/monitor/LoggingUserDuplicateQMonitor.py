import logging
from logger.LoggingBase import LOG_LEVEL
from logger.LoggingBase import LOG_BASE_PATH

userDuplicateQMonitorLogger = logging.getLogger('userDuplicateQMonitorLogger')
userDuplicateQMonitorLogger.setLevel(LOG_LEVEL)

fileHandler = logging.FileHandler(LOG_BASE_PATH + '/logs/userDuplicateQMonitor.log')
fileHandler.setLevel(LOG_LEVEL)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(LOG_LEVEL)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fileHandler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)

userDuplicateQMonitorLogger.addHandler(fileHandler)
userDuplicateQMonitorLogger.addHandler(consoleHandler)
