from process.TestProcessCrawlerA import TestProcessCrawlerA
from process.TestProcessCrawlerB import TestProcessCrawlerB


class TestProcessMain:

    def __init__(self):
        pass

if __name__ == "__main__":
    main = TestProcessMain()

    for i in range(0, 20):
        processName = "TestProcessCrawlerA[" + str(i) + "]"
        main.testProcessCrawlerA = TestProcessCrawlerA(processName).start()

    for i in range(0, 20):
        processName = "TestProcessCrawlerB[" + str(i) + "]"
        main.testProcessCrawlerB = TestProcessCrawlerB(processName).start()
