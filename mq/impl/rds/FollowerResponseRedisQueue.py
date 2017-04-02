from common.rds.RedisUtils import RedisUtils
from common.rds.RedisConfig import FOLLOWER_RESP_QUEUE_NAME
from logger.LoggingRoot import rootLogger
from mq.impl.rds.RedisQueue import RedisQueue


class FollowerResponseRedisQueue(RedisQueue):

    def __init__(self):
        pass

    def push(self, requestId, response):
        rootLogger.debug(requestId + "FollowerResponseRedisQueue push:" + str(response))
        RedisUtils.lpush(FOLLOWER_RESP_QUEUE_NAME, response)

    def pull(self, requestId):
        response = RedisUtils.blpop(FOLLOWER_RESP_QUEUE_NAME)
        rootLogger.debug(requestId + "FollowerResponseRedisQueue pull:" + str(response))
        return self.convertStr2Dict(response)

    def size(self):
        return RedisUtils.llen(FOLLOWER_RESP_QUEUE_NAME)
