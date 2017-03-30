#!/usr/bin/python3
#coding=utf-8
from dao.biz.impl.mysql.UserMysqlDaoImpl import UserMysqlDaoImpl
from dao.biz.impl.file.UserFileDaoImpl import UserFileDaoImpl
from dao.biz.impl.mongo.UserMongoDaoImpl import UserMongoDaoImpl


class DaoFactory:

    FILE = "File"
    MYSQL = "Mysql"
    MONGO = "MongoDB"
    ES = "ES"

    def createUserDao(self, type):
        if type == DaoFactory.FILE:
            self.dao = UserFileDaoImpl()
        if type == DaoFactory.MYSQL:
            self.dao = UserMysqlDaoImpl()
        if type == DaoFactory.MONGO:
            self.dao = UserMongoDaoImpl()
        return self.dao

if __name__ == "__main__":

    factory = DaoFactory()
    mysqlDao = factory.createUserDao(DaoFactory.MYSQL)
    mongoDao = factory.createUserDao(DaoFactory.MONGO)
    fileDao = factory.createUserDao(DaoFactory.FILE)
    userInfoList = [{
      "is_followed": False,
      "avatar_url_template": "https://pic4.zhimg.com/v2-83783203a87d7d38d67a359df5049b0f_{size}.jpg",
      "badge": [],
      "name": "是shei",
      "headline": "",
      "gender": 1,
      "user_type": "people",
      "answer_count": 0,
      "is_advertiser": False,
      "avatar_url": "https://pic4.zhimg.com/v2-83783203a87d7d38d67a359df5049b0f_is.jpg",
      "is_following": False,
      "is_org": False,
      "type": "people",
      "url": "http://www.zhihu.com/api/v4/people/546582be0707a61afb4472b00923fbdf",
      "follower_count": 7,
      "url_token": "shirley-008123",
      "id": "546582be0707a61afb4472b00923fbdf",
      "articles_count": 0
    },
    {
      "is_followed": False,
      "avatar_url_template": "https://pic3.zhimg.com/dc89486785e4ddc870c4442bb050c6ce_{size}.jpg",
      "badge": [],
      "name": "万能的岩哥哥",
      "headline": "来生再做英语狗",
      "gender": 0,
      "user_type": "people",
      "answer_count": 0,
      "is_advertiser": False,
      "avatar_url": "https://pic3.zhimg.com/dc89486785e4ddc870c4442bb050c6ce_is.jpg",
      "is_following": False,
      "is_org": False,
      "type": "people",
      "url": "http://www.zhihu.com/api/v4/people/25c96207b652a4a50fb4fa2e23790a84",
      "follower_count": 1,
      "url_token": "xu-yan-1-94",
      "id": "25c96207b652a4a50fb4fa2e23790a84",
      "articles_count": 0
    }]
    response = mongoDao.saveUsers(userInfoList)
    response = mysqlDao.saveUsers(userInfoList)
    response = fileDao.saveUsers(userInfoList)
