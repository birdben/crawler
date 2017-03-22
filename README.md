### 环境搭建

#### 持久化存储

##### MongoDB

安装pymongo

```
$ python3 -m pip install pymongo
```

参考文章：

- http://api.mongodb.com/python/current/installation.html
- http://api.mongodb.com/python/current/api/pymongo/mongo_client.html#pymongo.mongo_client.MongoClient
- http://api.mongodb.com/python/current/faq.html#multiprocessing

##### MySQL

暂不支持

##### Elasticsearch

暂不支持

### 爬虫功能

1. 使用内存Queue解耦用户数据去重，用户爬取，用户解析，关注者爬取，关注者解析功能模块
2. 可以设置开启多个线程执行用户数据去重，爬取用户数据，解析用户数据，爬取关注者数据，解析关注者数据
3. 使用内存Map处理抓取用户数据重复问题（如果抓取的用户数据过大，考虑替换成Redis去重）
4. 已经支持将爬取的用户数据持久化存储到MongoDB中（后续会支持MySQL，Elasticsearch等其他持久化存储）
5. 将抓取的关键日志输出到日志文件中，方便debug

### 待完成功能

1. 各个Queue和Cache的线程同步，否则会出现数据重复问题
2. 定时任务执行线程，可以控制爬虫的执行频率，而且不是while循环一直执行线程
3. 支持MySQL，Elasticsearch等持久化存储
4. 挂载多个代理IP，不至于被封
5. 补充组件图