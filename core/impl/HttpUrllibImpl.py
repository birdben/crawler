#!/usr/bin/python3
#coding=utf-8

import urllib3

from core.HttpCore import HttpCore
from logger.LoggingRoot import rootLogger


# 方式二：使用urllib3
class HttpUrllibImpl(HttpCore):

    def __init__(self):
        pass

    def buildUrl(self, request):
        url = HttpCore.HOST + request["url"] + self.buildParamsUrl(request["params"])
        rootLogger.info("buildUrl:" + url)
        return url

    def doGetRequestHandler(self, httpClientRequest):
        request = self.defaultRequest(httpClientRequest)
        http = urllib3.PoolManager()
        response = http.request(HttpCore.GET, self.buildUrl(httpClientRequest), None, request["headers"])
        self.httpClientResponse["status"] = response.status
        self.httpClientResponse["reason"] = response.reason
        self.httpClientResponse["data"] = response.data.decode("utf-8")
        # rootLogger.debug("status:" + str(self.httpClientResponse["status"]))
        # rootLogger.debug("reason:" + self.httpClientResponse["reason"])
        # rootLogger.debug("data:" + self.httpClientResponse["data"])
        return self.httpClientResponse

    def doPostRequestHandler(self, httpClientRequest):
        request = self.defaultRequest(httpClientRequest)
        http = urllib3.PoolManager()
        response = http.request(HttpCore.POST, self.buildUrl(httpClientRequest), None, request["headers"])
        self.httpClientResponse["status"] = response.status
        self.httpClientResponse["reason"] = response.reason
        self.httpClientResponse["data"] = response.data.decode("utf-8")
        # rootLogger.debug("status:" + str(self.httpClientResponse["status"]))
        # rootLogger.debug("reason:" + self.httpClientResponse["reason"])
        # rootLogger.debug("data:" + self.httpClientResponse["data"])
        return self.httpClientResponse

if __name__ == "__main__":
    httpClient = HttpUrllibImpl()
    request = {
        "method": "GET",
        "url": "/api/v4/members/zhang-jia-wei/followers"
    }
    response = httpClient.doRequest(request)
    rootLogger.debug("HttpUrllibImpl response:" + str(response))
