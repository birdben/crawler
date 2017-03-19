#!/usr/bin/python3
#coding=utf-8
from dao.impl.UserFileDaoImpl import UserFileDaoImpl
from dao.impl.UserMySQLDaoImpl import UserMySQLDaoImpl


class DaoFactory:

    FILE = "File"
    MYSQL = "MySQL"
    MONGODB = "MongoDB"
    ES = "ES"

    def createUserDao(self, type):
        if type == DaoFactory.FILE:
            self.dao = UserFileDaoImpl()
        if type == DaoFactory.MYSQL:
            self.dao = UserMySQLDaoImpl()
        return self.dao

if __name__ == "__main__":

    factory = DaoFactory()
    dao = factory.createUserDao(DaoFactory.FILE)
    response = dao.saveUser("123")
