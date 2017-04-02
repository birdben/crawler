from mq.BaseQueue import BaseQueue


class RedisQueue(BaseQueue):

    def __init__(self):
        pass

    def convertStr2Dict(self, message):
        msgObj = eval(bytes.decode(message))
        return msgObj
