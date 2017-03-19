import logging
from logger.LoggingBase import LOG_LEVEL

followerParserLogger = logging.getLogger('followerParserLogger')
followerParserLogger.setLevel(LOG_LEVEL)

fileHandler = logging.FileHandler('logs/followerParser.log')
fileHandler.setLevel(LOG_LEVEL)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(LOG_LEVEL)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fileHandler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)

followerParserLogger.addHandler(fileHandler)
followerParserLogger.addHandler(consoleHandler)
