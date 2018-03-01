#! -*- encoding:utf-8 -*-

from urllib import request

# 要访问的目标页面
import urllib3

targetUrl = "https://www.baidu.com"
# targetUrl = "http://proxy.abuyun.com/switch-ip"
# targetUrl = "http://proxy.abuyun.com/current-ip"

proxyMeta = "http://121.52.226.44:8080"

proxy_handler = request.ProxyHandler({
    "http": proxyMeta,
    "https": proxyMeta,
})

headers = urllib3.make_headers(proxy_basic_auth="username:password")

proxy = urllib3.ProxyManager(proxyMeta, proxy_headers=headers)
r = proxy.request("GET", targetUrl)
print("代理响应")
print(r.status)
