#!/usr/bin/python3
#coding=utf-8

from core.impl.HttpClientImpl import HttpClientImpl
from core.impl.HttpUrllibImpl import HttpUrllibImpl
from logger.LoggingRoot import rootLogger


class HttpCoreFactory:

    HTTP_CLIENT = "HttpClient"
    HTTP_URLLIB = "HttpUrllib"
    client = None

    def createHttpCore(self, type):
        if type == HttpCoreFactory.HTTP_CLIENT:
            self.client = HttpClientImpl()
        if type == HttpCoreFactory.HTTP_URLLIB:
            self.client = HttpUrllibImpl()
        return self.client

if __name__ == "__main__":

    httpClientRequest = {
        "method": "GET",
        "url": "/api/v4/members/zhang-jia-wei/followers"
    }

    factory = HttpCoreFactory()
    client = factory.createHttpCore(HttpCoreFactory.HTTP_CLIENT)
    response = client.doRequest(httpClientRequest)
    rootLogger.debug("HTTP_CLIENT response:" + str(response))
    client = factory.createHttpCore(HttpCoreFactory.HTTP_URLLIB)
    response = client.doRequest(httpClientRequest)
    rootLogger.debug("HTTP_URLLIB response:" + str(response))
