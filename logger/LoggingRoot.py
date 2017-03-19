import logging
from logger.LoggingBase import LOG_LEVEL

rootLogger = logging.getLogger('rootLogger')
rootLogger.setLevel(LOG_LEVEL)

fileHandler = logging.FileHandler('logs/root.log')
fileHandler.setLevel(LOG_LEVEL)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(LOG_LEVEL)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fileHandler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)

rootLogger.addHandler(fileHandler)
rootLogger.addHandler(consoleHandler)
