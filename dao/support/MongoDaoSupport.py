from pymongo.errors import ConnectionFailure

from dao.support.DaoSupport import DaoSupport
from dao.config import MongoConfig
from logger.LoggingRoot import rootLogger
from pymongo import mongo_client


class MongoDaoSupport(DaoSupport):
    def __init__(self):
        super().__init__()

    def getConn(self):
        rootLogger.debug("MongoDaoSupport getConn start")
        conn = mongo_client.MongoClient(
            host=MongoConfig.HOST,
            port=MongoConfig.PORT,
            document_class=MongoConfig.DOCUMENT_CLASS,
            tz_aware=MongoConfig.TZ_AWARE,
            connect=MongoConfig.CONNECT,
            maxPoolSize=MongoConfig.MAX_POOL_SIZE,
            minPoolSize=MongoConfig.MIN_POOL_SIZE
        )
        # 建立和数据库系统的连接,创建Connection时，指定host及port参数
        db_auth = conn.admin
        # admin 数据库有帐号，连接-认证-切换库
        db_auth.authenticate(MongoConfig.USER, MongoConfig.PWD)
        try:
            conn.admin.command('ismaster')
        except ConnectionFailure:
            print("Server not available")
        rootLogger.debug("MongoDaoSupport getConn end")
        return conn

if __name__ == "__main__":
    mongoDaoSupport = MongoDaoSupport()
    conn = mongoDaoSupport.getConn()
    print(conn.database_names())
    testDB = conn["test"]
    print(testDB)
    print(testDB.collection_names)
    usersCollection = testDB["users"]
    cursor = usersCollection.find().limit(10)
    for doc in cursor:
        print(doc)
    conn.close()
