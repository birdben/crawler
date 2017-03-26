#!/usr/bin/python3
#coding=utf-8

import http.client

from core.HttpCore import HttpCore, HttpClientResponse
from logger.LoggingRoot import rootLogger


# 方式一：使用http.client
class HttpClientImpl(HttpCore):

    def __init__(self):
        pass

    def buildUrl(self, requestId, request):
        url = request["url"] + self.buildParamsUrl(request["params"])
        rootLogger.debug(requestId + "HttpClientImpl buildUrl:" + url)
        return url

    def doGetRequestHandler(self, requestId, httpClientRequest):
        conn = http.client.HTTPSConnection(httpClientRequest["host"])
        conn.connect()
        conn.request(HttpCore.GET, self.buildUrl(requestId, httpClientRequest), None, httpClientRequest["headers"])
        response = conn.getresponse()
        httpClientResponse = HttpClientResponse().getDefaultResponse()
        httpClientResponse["status"] = response.status
        httpClientResponse["reason"] = response.reason
        httpClientResponse["data"] = response.read().decode("utf-8")
        # rootLogger.debug("status:" + str(httpClientResponse["status"]))
        # rootLogger.debug("reason:" + httpClientResponse["reason"])
        # rootLogger.debug("data:" + httpClientResponse["data"])
        conn.close()
        return httpClientResponse

    def doPostRequestHandler(self, requestId, httpClientRequest):
        conn = http.client.HTTPSConnection(httpClientRequest["host"])
        conn.connect()
        conn.request(HttpCore.POST, self.buildUrl(requestId, httpClientRequest), None, httpClientRequest["headers"])
        response = conn.getresponse()
        httpClientResponse = HttpClientResponse().getDefaultResponse()
        httpClientResponse["status"] = response.status
        httpClientResponse["reason"] = response.reason
        httpClientResponse["data"] = response.read().decode("utf-8")
        # rootLogger.debug("status:" + str(httpClientResponse["status"]))
        # rootLogger.debug("reason:" + httpClientResponse["reason"])
        # rootLogger.debug("data:" + httpClientResponse["data"])
        conn.close()
        return httpClientResponse

if __name__ == "__main__":
    httpClient = HttpClientImpl()

    # 客户端api接口，通过用户id获取user信息
    userRequest = {
        "host": "api.zhihu.com",
        "method": "GET",
        "url": "/people/bafadeef906dcdc5b6b37397d7091665",
        "params": {},
        "headers": {
            "Host": "api.zhihu.com",
            "Authorization": "Bearer Mi4wQUFBQU9qRWdBQUFBQU1MZThYVndDeGNBQUFCaEFsVk5VbzNzV0FESHZyN1FkdU53bllZOE5tRUtMZHRXTWNEcmRB|1489305735|7b00a5eb2137cfae4ad342e47322d92e18d1d3d6",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0",
            # "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "x-udid": "AADC3vF1cAuPTkgQezG76kgARvc5TuxQdrE=",
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "X-API-Version": "3.0.52"
        }
    }

    # 客户端api接口，通过用户id获取follower信息，可以与userId关联
    followerRequest = {
        "host": "api.zhihu.com",
        "method": "GET",
        "url": "/people/bafadeef906dcdc5b6b37397d7091665/followers?limit=20&offset=0",
        "params": {},
        "headers": {
            "Host": "api.zhihu.com",
            "Authorization": "Bearer Mi4wQUFBQU9qRWdBQUFBQU1MZThYVndDeGNBQUFCaEFsVk5VbzNzV0FESHZyN1FkdU53bllZOE5tRUtMZHRXTWNEcmRB|1489305735|7b00a5eb2137cfae4ad342e47322d92e18d1d3d6",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0",
            # "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "x-udid": "AADC3vF1cAuPTkgQezG76kgARvc5TuxQdrE=",
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "X-API-Version": "3.0.52"
        }
    }

    # web接口，通过用户name获取follower信息，不能与userId关联，所以使用客户端的api接口替换
    """
    followerRequest = {
        "host": "www.zhihu.com",
        "method": "GET",
        "url": "/api/v4/members/zhang-jia-wei/followers",
        "params": {
            "offset": 0,
            "limit": 20
        },
        "headers": {
            "Host": "www.zhihu.com",
            "Authorization": "Bearer Mi4wQUFBQU9qRWdBQUFBQU1MZThYVndDeGNBQUFCaEFsVk5VbzNzV0FESHZyN1FkdU53bllZOE5tRUtMZHRXTWNEcmRB|1489305735|7b00a5eb2137cfae4ad342e47322d92e18d1d3d6",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            # 告知服务器采用何种压缩方式
            # "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "origin": "https://www.zhihu.com",
            "x-udid": "AADC3vF1cAuPTkgQezG76kgARvc5TuxQdrE=",
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"
        }
    }
    """

    # 测试抓取User信息
    userResponse = httpClient.doRequest(userRequest)
    rootLogger.debug("HttpClientImpl User response:" + str(userResponse))

    # 测试抓取Follower信息
    followerResponse = httpClient.doRequest(followerRequest)
    rootLogger.debug("HttpClientImpl Follower response:" + str(followerResponse))
