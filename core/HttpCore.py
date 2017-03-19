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
    httpClientResponse = {
        "status": 9999,
        "reason": "Unknown",
        "data": ""
    }
    httpClientRequest = {
        "url": "",
        "params": {
            "limit": 20,
            "offset": 0
        }
    }

    GET = "GET"
    POST = "POST"
    HOST = "www.zhihu.com"

    __DEFAULT_METHOD = "GET"
    __DEFAULT_PARAMS = {
        "limit": 20,
        "offset": 0
    }
    __DEFAULT_URL = "/api/v4/members/zhang-jia-wei/followers"
    # __DEFAULT_PARAMS = "?include=data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics"
    __DEFAULT_HEADERS = {
        'Host': 'www.zhihu.com',
        'Authorization': 'Bearer Mi4wQUFBQU9qRWdBQUFBQU1MZThYVndDeGNBQUFCaEFsVk5VbzNzV0FESHZyN1FkdU53bllZOE5tRUtMZHRXTWNEcmRB|1489305735|7b00a5eb2137cfae4ad342e47322d92e18d1d3d6',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        # 告知服务器采用何种压缩方式
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'origin': 'https://www.zhihu.com',
        'x-udid': 'AADC3vF1cAuPTkgQezG76kgARvc5TuxQdrE=',
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"
    }

    # https://www.zhihu.com/api/v4/members/zhang-jia-wei/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=60&limit=20
    # data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics
    # 定义http请求参数

    def __init__(self):
        pass

    def validatedRequest(self, httpClientRequest):
        reason = ""
        if "method" not in httpClientRequest:
            reason = "method can not be None"
            return reason
        if "url" not in httpClientRequest:
            reason = "url can not be None"
            return reason
        return reason

    def defaultRequest(self, httpClientRequest):
        if "headers" not in httpClientRequest:
            httpClientRequest["headers"] = HttpCore.__DEFAULT_HEADERS
        if "params" not in httpClientRequest:
            httpClientRequest["params"] = HttpCore.__DEFAULT_PARAMS
        return httpClientRequest

    def doGetRequestHandler(self, request):
        return self.httpClientResponse

    def doPostRequestHandler(self, request):
        return self.httpClientResponse

    def buildParamsUrl(self, params):
        paramsUrl = ""
        for key in params:
            value = str(params[key])
            if paramsUrl == "":
                paramsUrl += "?" + key + "=" + value
            else:
                paramsUrl += "&" + key + "=" + value
        return paramsUrl

    def doRequest(self, httpClientRequest):
        if self.validatedRequest(httpClientRequest) != "":
            self.httpClientResponse["reason"] = self.validatedRequest(httpClientRequest)
            return self.httpClientResponse

        request = self.defaultRequest(httpClientRequest)

        method = request["method"]
        if method == HttpCore.GET:
            self.doGetRequest(httpClientRequest)
        elif method == HttpCore.POST:
            self.doPostRequest(httpClientRequest)
        else:
            self.doGetRequest(httpClientRequest)
        # TODO: PUT
        # TODO: HEAD
        return self.httpClientResponse

    def doGetRequest(self, httpClientRequest):
        try:
            self.httpClientResponse = self.doGetRequestHandler(httpClientRequest)
        # TODO: HttpCoreRequestException
        except Exception as e:
            rootLogger.error("doGetRequest请求失败")
            rootLogger.error(e)
        return self.httpClientResponse

    def doPostRequest(self, httpClientRequest):
        try:
            self.httpClientResponse = self.doPostRequestHandler(httpClientRequest)
        # TODO: HttpCoreRequestException
        except Exception as e:
            rootLogger.error("doPostRequest请求失败")
            rootLogger.error(e)
        return self.httpClientResponse
