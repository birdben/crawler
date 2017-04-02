from common.rds.RedisUtils import RedisUtils
from common.rds.RedisConfig import USER_DUPLICATE_QUEUE_NAME
from logger.LoggingRoot import rootLogger
from mq.impl.rds.RedisQueue import RedisQueue


class UserDuplicateRedisQueue(RedisQueue):

    def __init__(self):
        pass

    def push(self, requestId, message):
        rootLogger.debug(requestId + "UserDuplicateRedisQueue push:" + str(message))
        RedisUtils.lpush(USER_DUPLICATE_QUEUE_NAME, message)

    def pull(self, requestId):
        message = RedisUtils.blpop(USER_DUPLICATE_QUEUE_NAME)
        rootLogger.debug(requestId + "UserDuplicateRedisQueue pull:" + str(message))
        return self.convertStr2Dict(message)

    def size(self):
        return RedisUtils.llen(USER_DUPLICATE_QUEUE_NAME)
