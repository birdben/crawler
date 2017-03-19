import logging
from logger.LoggingBase import LOG_LEVEL

userCrawlerLogger = logging.getLogger('userCrawlerLogger')
userCrawlerLogger.setLevel(LOG_LEVEL)

fileHandler = logging.FileHandler('logs/userCrawler.log')
fileHandler.setLevel(LOG_LEVEL)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(LOG_LEVEL)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fileHandler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)

userCrawlerLogger.addHandler(fileHandler)
userCrawlerLogger.addHandler(consoleHandler)
