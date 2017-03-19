import logging
from logger.LoggingBase import LOG_LEVEL

followerCrawlerLogger = logging.getLogger('followerCrawlerLogger')
followerCrawlerLogger.setLevel(LOG_LEVEL)

fileHandler = logging.FileHandler('logs/followerCrawler.log')
fileHandler.setLevel(LOG_LEVEL)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(LOG_LEVEL)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fileHandler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)

followerCrawlerLogger.addHandler(fileHandler)
followerCrawlerLogger.addHandler(consoleHandler)
