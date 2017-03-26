from dao.biz.UserDao import UserDao
from dao.support.MongoDaoSupport import MongoDaoSupport
from dao.config.MongoConfig import DB_ZHIHU, TABLE_USER, KEY_LIMIT, VALUE_LIMIT
from logger.LoggingRoot import rootLogger


class UserMongoDaoImpl(MongoDaoSupport, UserDao):
    def _deleteUserById(self, userId):
        pass

    def _saveOrUpdateUser(self, userInfo):
        pass

    def _findUserById(self, userId):
        pass

    def _saveOrUpdateUsers(self, userInfoList):
        pass

    def _updateUser(self, userInfo):
        pass

    def __init__(self):
        super().__init__()

    def _saveUser(self, requestId, userInfo):
        rootLogger.debug(requestId + "UserMongoDaoImpl saveUser start")
        try:
            conn = self.getConn()
            db = conn[DB_ZHIHU]
            users = db[TABLE_USER]
            users.insert_one(userInfo)
        except Exception as e:
            rootLogger.error(requestId + "UserMongoDaoImpl saveUser error")
            rootLogger.error(e)
        rootLogger.debug(requestId + "UserMongoDaoImpl saveUser end")

    def _saveUsers(self, userInfoList):
        rootLogger.debug("UserMongoDaoImpl saveUsers start")
        try:
            conn = self._getConn()
            db = conn[DB_ZHIHU]
            users = db[TABLE_USER]
            users.insert_many(userInfoList)
        except Exception as e:
            rootLogger.error("UserMongoDaoImpl saveUsers error")
            rootLogger.error(e)
        rootLogger.debug("UserMongoDaoImpl saveUsers end")

    def _findUserByCondition(self, param):
        rootLogger.debug("UserMongoDaoImpl findUserByCondition start")
        try:
            conn = self.getConn()
            db = conn[DB_ZHIHU]
            users = db[TABLE_USER]
            # 检查参数
            limit = KEY_LIMIT in param if param[KEY_LIMIT] else VALUE_LIMIT
            cursor = users.find().limit(limit)
            for doc in cursor:
                print(doc)
        except Exception as e:
            rootLogger.error("UserMongoDaoImpl findUserByCondition error")
            rootLogger.error(e)
        rootLogger.debug("UserMongoDaoImpl findUserByCondition end")
