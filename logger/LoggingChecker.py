import logging
from logger.LoggingBase import LOG_LEVEL

checkerLogger = logging.getLogger('checkerLogger')
checkerLogger.setLevel(LOG_LEVEL)

fileHandler = logging.FileHandler('logs/checker.log')
fileHandler.setLevel(LOG_LEVEL)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(LOG_LEVEL)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fileHandler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)

checkerLogger.addHandler(fileHandler)
checkerLogger.addHandler(consoleHandler)
