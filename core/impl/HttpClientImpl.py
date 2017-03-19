#!/usr/bin/python3
#coding=utf-8

import http.client

from core.HttpCore import HttpCore
from logger.LoggingRoot import rootLogger


# 方式一：使用http.client
class HttpClientImpl(HttpCore):

    def __init__(self):
        pass

    def buildUrl(self, request):
        url = request["url"] + self.buildParamsUrl(request["params"])
        rootLogger.info("buildUrl:" + url)
        return url

    def doGetRequestHandler(self, httpClientRequest):
        request = self.defaultRequest(httpClientRequest)
        conn = http.client.HTTPSConnection(HttpCore.HOST)
        conn.connect()
        conn.request(HttpCore.GET, self.buildUrl(httpClientRequest), None, request["headers"])
        response = conn.getresponse()
        self.httpClientResponse["status"] = response.status
        self.httpClientResponse["reason"] = response.reason
        self.httpClientResponse["data"] = response.read().decode("utf-8")
        # rootLogger.debug("status:" + str(self.httpClientResponse["status"]))
        # rootLogger.debug("reason:" + self.httpClientResponse["reason"])
        # rootLogger.debug("data:" + self.httpClientResponse["data"])
        conn.close()
        return self.httpClientResponse

    def doPostRequestHandler(self, httpClientRequest):
        request = self.defaultRequest(httpClientRequest)
        conn = http.client.HTTPSConnection(HttpCore.HOST)
        conn.connect()
        conn.request(HttpCore.POST, self.buildUrl(httpClientRequest), None, request["headers"])
        response = conn.getresponse()
        self.httpClientResponse["status"] = response.status
        self.httpClientResponse["reason"] = response.reason
        self.httpClientResponse["data"] = response.read().decode("utf-8")
        # rootLogger.debug("status:" + str(self.httpClientResponse["status"]))
        # rootLogger.debug("reason:" + self.httpClientResponse["reason"])
        # rootLogger.debug("data:" + self.httpClientResponse["data"])
        conn.close()
        return self.httpClientResponse

if __name__ == "__main__":
    httpClient = HttpClientImpl()
    request = {
        "method": "GET",
        "url": "/api/v4/members/zhang-jia-wei/followers"
    }
    response = httpClient.doRequest(request)
    rootLogger.debug("HttpClientImpl response:" + str(response))
