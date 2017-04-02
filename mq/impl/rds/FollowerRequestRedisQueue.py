from common.rds.RedisUtils import RedisUtils
from common.rds.RedisConfig import FOLLOWER_REQ_QUEUE_NAME
from logger.LoggingRoot import rootLogger
from mq.impl.rds.RedisQueue import RedisQueue


class FollowerRequestRedisQueue(RedisQueue):

    def __init__(self):
        pass

    def push(self, requestId, request):
        rootLogger.debug(requestId + "FollowerRequestRedisQueue push:" + str(request))
        RedisUtils.lpush(FOLLOWER_REQ_QUEUE_NAME, request)

    def pull(self, requestId):
        request = RedisUtils.blpop(FOLLOWER_REQ_QUEUE_NAME)
        rootLogger.debug(requestId + "FollowerRequestRedisQueue pull:" + str(request))
        return self.convertStr2Dict(request)

    def size(self):
        return RedisUtils.llen(FOLLOWER_REQ_QUEUE_NAME)
