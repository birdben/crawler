import threading
from logger.LoggingRoot import rootLogger


class UserThreadTask:
    def startUserTask(self):
        rootLogger.debug("startUserTask...")
        t = threading.Timer(5, self.doUserTask)
        t.start()
        rootLogger.debug("do not wait user task done")

    def doUserTask(self):
        rootLogger.debug("doUserTask...")


if __name__ == "__main__":
    userThreadTask = UserThreadTask()
    userThreadTask.startUserTask()
