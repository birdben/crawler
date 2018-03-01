from process.TestThreadCrawlerA import TestThreadCrawlerA
from process.TestThreadCrawlerB import TestThreadCrawlerB


class TestThreadMain:

    def __init__(self):
        pass

if __name__ == "__main__":
    main = TestThreadMain()

    for i in range(0, 20):
        threadName = "TestThreadCrawlerA[" + str(i) + "]"
        main.testThreadCrawlerA = TestThreadCrawlerA(threadName).start()

    for i in range(0, 20):
        threadName = "TestThreadCrawlerB[" + str(i) + "]"
        main.testThreadCrawlerB = TestThreadCrawlerB(threadName).start()
