from common.rds.RedisUtils import RedisUtils
from common.rds.RedisConfig import USER_RESP_QUEUE_NAME
from logger.LoggingRoot import rootLogger
from mq.impl.rds.RedisQueue import RedisQueue


class UserResponseRedisQueue(RedisQueue):

    def __init__(self):
        pass

    def push(self, requestId, response):
        rootLogger.debug(requestId + "UserResponseRedisQueue push:" + str(response))
        RedisUtils.lpush(USER_RESP_QUEUE_NAME, response)

    def pull(self, requestId):
        response = RedisUtils.blpop(USER_RESP_QUEUE_NAME)
        rootLogger.debug(requestId + "UserResponseRedisQueue pull:" + str(response))
        return self.convertStr2Dict(response)

    def size(self):
        return RedisUtils.llen(USER_RESP_QUEUE_NAME)
