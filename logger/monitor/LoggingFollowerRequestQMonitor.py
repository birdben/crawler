import logging
from logger.LoggingBase import LOG_LEVEL
from logger.LoggingBase import LOG_BASE_PATH

followerRequestQMonitorLogger = logging.getLogger('followerRequestQMonitorLogger')
followerRequestQMonitorLogger.setLevel(LOG_LEVEL)

fileHandler = logging.FileHandler(LOG_BASE_PATH + '/logs/followerRequestQMonitor.log')
fileHandler.setLevel(LOG_LEVEL)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(LOG_LEVEL)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fileHandler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)

followerRequestQMonitorLogger.addHandler(fileHandler)
followerRequestQMonitorLogger.addHandler(consoleHandler)
