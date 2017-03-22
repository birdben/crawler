from dao.biz.UserDao import UserDao
from dao.support.MysqlDaoSupport import MysqlDaoSupport


class UserMysqlDaoImpl(MysqlDaoSupport, UserDao):
    def __init__(self):
        pass
