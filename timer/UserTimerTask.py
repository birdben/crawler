#!/usr/bin/python3
# coding=utf-8

import time
from logger.LoggingRoot import rootLogger


class UserTimerTask:
    def startUserTask(self, n):
        while True:
            rootLogger.debug(time.strftime('%Y-%m-%d %X', time.localtime()))
            self.doUserTask()
            time.sleep(n)
            rootLogger.debug("done user task")

    def doUserTask(self):
        rootLogger.debug("doUserTask ...")


if __name__ == '__main__':
    userTask = UserTimerTask()
    userTask.startUserTask(5)
