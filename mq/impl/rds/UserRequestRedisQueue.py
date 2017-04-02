from common.rds.RedisUtils import RedisUtils
from common.rds.RedisConfig import USER_REQ_QUEUE_NAME
from logger.LoggingRoot import rootLogger
from mq.impl.rds.RedisQueue import RedisQueue


class UserRequestRedisQueue(RedisQueue):

    def __init__(self):
        pass

    def push(self, requestId, request):
        rootLogger.debug(requestId + "UserRequestRedisQueue push:" + str(request))
        RedisUtils.lpush(USER_REQ_QUEUE_NAME, request)

    def pull(self, requestId):
        request = RedisUtils.blpop(USER_REQ_QUEUE_NAME)
        rootLogger.debug(requestId + "UserRequestRedisQueue pull:" + str(request))
        return self.convertStr2Dict(request)

    def size(self):
        return RedisUtils.llen(USER_REQ_QUEUE_NAME)
