from logger.LoggingRoot import rootLogger

class FileDao:

    FILE_PATH = "/Users/yunyu/Downloads/zhihu.txt"

    def __init__(self):
        pass

    def saveFile(self, str):
        # rootLogger.debug("FileDao save...")
        self.file = open(FileDao.FILE_PATH, "a")
        self.file.write(str + "\n")
        self.file.flush()
        self.file.close()
