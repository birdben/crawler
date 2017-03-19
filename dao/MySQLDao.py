from logger.LoggingRoot import rootLogger

class MySQLDao:

    FILE_PATH = "/Users/yunyu/Downloads/zhihu.txt"

    def __init__(self):
        pass

    def getConn(self):
        # TODO:实现MySQL
        conn = ""
        return conn

    def saveMySQL(self, sql):
        rootLogger.debug("MySQLDao save...")
