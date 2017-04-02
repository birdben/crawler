import redis
from sample.redis.mq.RedisProducer import RedisProducer
from sample.redis.mq.RedisConsumer import RedisConsumer

if __name__ == '__main__':
    redisConn = redis.StrictRedis(host="localhost", db=5, password="root")
    queue = "zhihu_test:queue"

    # 启动生产者和消费者
    # 在Redis中使用命令"llen zhihu_test:queue"查看消息队列的堆积程度
    RedisProducer(redisConn=redisConn, queue=queue).start()
    RedisConsumer(redisConn=redisConn, queue=queue).start()

