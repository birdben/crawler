import redis

from cache.impl.rds import RedisConfig

RedisClient = redis.Redis(RedisConfig.HOST, RedisConfig.PORT, RedisConfig.DB, RedisConfig.PWD)


class RedisUtils:
    @staticmethod
    def hexists(name, key):
        return RedisClient.hexists(name, key)

    @staticmethod
    def hget(name, key):
        return RedisClient.hget(name, key)

    @staticmethod
    def getset(name, value):
        return RedisClient.getset(name, value)

    @staticmethod
    def hdel(name, *keys):
        return RedisClient.hdel(name, *keys)

    @staticmethod
    def hgetall(name):
        return RedisClient.hgetall(name)

    @staticmethod
    def hkeys(name):
        return RedisClient.hkeys(name)

    @staticmethod
    def hlen(name):
        return RedisClient.hlen(name)

    @staticmethod
    def hset(name, key, value):
        return RedisClient.hset(name, key, value)

    @staticmethod
    def setex(name, time, value):
        return RedisClient.setex(name, time, value)

    @staticmethod
    def get(name):
        return RedisClient.get(name)

    @staticmethod
    def exists(name):
        return RedisClient.exists(name)

    @staticmethod
    def set(name, value):
        return RedisClient.set(name, value)


if __name__ == "__main__":
    RedisUtils.set("111111", """{"userId":"111111", "userName":"birdben1"}""")
    RedisUtils.set("222222", """{"userId":"222222", "userName":"birdben2"}""")
    RedisUtils.set("333333", """{"userId":"333333", "userName":"birdben3"}""")
    print(RedisUtils.exists("111111"))
    print(RedisUtils.exists("222222"))
    print(RedisUtils.exists("333333"))
    print(RedisUtils.exists("444444"))

    print(RedisUtils.get("111111"))
    print(RedisUtils.get("222222"))
    print(RedisUtils.get("333333"))
    print(RedisUtils.get("444444"))
