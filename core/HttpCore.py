#!/usr/bin/python3
# coding=utf-8

from logger.LoggingRoot import rootLogger

"""

请求头字段	    说明	                    响应头字段
Accept	        告知服务器发送何种媒体类型	Content-Type
Accept-Language	告知服务器发送何种语言	    Content-Language
Accept-Charset	告知服务器发送何种字符集	Content-Type
Accept-Encoding	告知服务器采用何种压缩方式	Content-Encoding

"""


class HttpCore:
    GET = "GET"
    POST = "POST"

    # 抓取Follower信息
    # https://www.zhihu.com/api/v4/members/zhang-jia-wei/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=60&limit=20
    # data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics
    # 定义http请求参数

    # 抓取User信息
    # https://api.zhihu.com/people/bafadeef906dcdc5b6b37397d7091665

    def __init__(self):
        pass

    def validatedRequest(self, httpClientRequest):
        reason = ""
        if "host" not in httpClientRequest:
            reason = "host can not be None"
            return reason
        if "method" not in httpClientRequest:
            reason = "method can not be None"
            return reason
        if "url" not in httpClientRequest:
            reason = "url can not be None"
            return reason
        if "params" not in httpClientRequest:
            reason = "params can not be None"
            return reason
        if "headers" not in httpClientRequest:
            reason = "headers can not be None"
            return reason
        return reason

    def doGetRequestHandler(self, requestId, request):
        return HttpClientResponse().getDefaultResponse()

    def doPostRequestHandler(self, requestId, request):
        return HttpClientResponse().getDefaultResponse()

    def buildParamsUrl(self, params):
        paramsUrl = ""
        for key in params:
            value = str(params[key])
            if paramsUrl == "":
                paramsUrl += "?" + key + "=" + value
            else:
                paramsUrl += "&" + key + "=" + value
        return paramsUrl

    def doRequest(self, requestId, httpClientRequest):
        rootLogger.debug(requestId + "doRequest request: " + str(httpClientRequest))
        if self.validatedRequest(httpClientRequest) != "":
            httpClientResponse = HttpClientResponse().getDefaultResponse()
            httpClientResponse["reason"] = self.validatedRequest(httpClientRequest)
            return httpClientResponse

        method = httpClientRequest["method"]
        if method == HttpCore.GET:
            httpClientResponse = self.doGetRequest(requestId, httpClientRequest)
        elif method == HttpCore.POST:
            httpClientResponse = self.doPostRequest(requestId, httpClientRequest)
        else:
            httpClientResponse = self.doGetRequest(requestId, httpClientRequest)
        # TODO: PUT
        # TODO: HEAD
        rootLogger.debug(requestId + "doRequest response: " + str(httpClientResponse))
        return httpClientResponse

    def doGetRequest(self, requestId, httpClientRequest):
        try:
            httpClientResponse = self.doGetRequestHandler(requestId, httpClientRequest)
        # TODO: HttpCoreRequestException
        except Exception as e:
            rootLogger.error(requestId + "doGetRequest请求失败")
            rootLogger.error(e)
        return httpClientResponse

    def doPostRequest(self, requestId, httpClientRequest):
        try:
            httpClientResponse = self.doPostRequestHandler(requestId, httpClientRequest)
        # TODO: HttpCoreRequestException
        except Exception as e:
            rootLogger.error(requestId + "doPostRequest请求失败")
            rootLogger.error(e)
        return httpClientResponse


class HttpClientResponse:

    def __init__(self):
        pass

    def getDefaultResponse(self):
        httpClientResponse = {
            "status": 9999,
            "reason": "Unknown",
            "data": ""
        }
        return httpClientResponse
