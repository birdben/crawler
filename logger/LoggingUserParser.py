import logging
from logger.LoggingBase import LOG_LEVEL

userParserLogger = logging.getLogger('userParserLogger')
userParserLogger.setLevel(LOG_LEVEL)

fileHandler = logging.FileHandler('logs/userParser.log')
fileHandler.setLevel(LOG_LEVEL)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(LOG_LEVEL)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fileHandler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)

userParserLogger.addHandler(fileHandler)
userParserLogger.addHandler(consoleHandler)
