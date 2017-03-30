### 环境搭建

#### 持久化存储

##### MongoDB

安装pymongo

```
$ python3 -m pip install pymongo
```

检查爬取的用户信息是否有重复

```
$ db.users.aggregate([
    { $group: { _id: "$id", count: { $sum: 1 } } },
    { $sort: { count: -1 } },
    { $limit: 10},
    { $match: { count: { $gt: 1 } } }
]);
```

参考文章：

- http://api.mongodb.com/python/current/installation.html
- http://api.mongodb.com/python/current/api/pymongo/mongo_client.html#pymongo.mongo_client.MongoClient
- http://api.mongodb.com/python/current/faq.html#multiprocessing
- http://api.mongodb.com/python/current/faq.html#writes-and-ids

##### MySQL

暂不支持

##### Elasticsearch

暂不支持

### Feature

##### 2.x Feature

1. 支持MySQL，Elasticsearch等持久化存储

##### 1.0.3 Feature

1. 处理线程的调优
2. 挂载多个代理IP，不至于被封
3. 补充组件图

### Relase Note

##### 1.0.2:

1. 使用RedisCache代替MemoryCache实现去重
2. 实现抽象类BaseCache，使用不同的缓存方式来进行去重
3. 处理从Queue中拉取出来的消息为空的情况
4. 统一规范方法命名规则
5. 支持Mongo指定用户名和密码创建连接
6. 使用Docker容器提供Redis和Mongo服务
7. 通过日志监控Queue的堆积情况，不限制Queue的大小

##### 1.0.1:

1. 更换爬取接口，使用客户端抓取到的api接口，替换原来的web api接口
2. 爬取下来的数据只保存去重后的User信息，不保存Follower信息，Follower的信息要经过DuplicateChecker去重过滤后才可以保存到DB
3. 强制校验https参数
4. 实现MemoryCache去重，验证多线程MemoryCache的线程安全性
5. 补充组件图，由于更换爬取接口，所以重新定义各个组件的数据结构
6. 随机线程等待时间，控制爬虫的执行频率，模拟人的行为操作，防止被封杀
7. 解决User和Follower的Response共用（非线程安全），导致Parser没有解析到对应的Response（UserParser解析到了FollowerResponse或者FollowerParser解析到了UserResponse），导致解析出错的问题
8. 给每个抓取，解析，去重线程添加一个requestId，并且写入到log日志文件中，方便debug检查错误
9. 实现抽象类Dao，使用不同持久化存储必须实现该抽象类Dao中的方法，来进行持久化操作

##### 1.0.0:

1. 使用内存Queue解耦用户数据去重，用户爬取，用户解析，关注者爬取，关注者解析功能模块（Python内置的Queue是线程安全的，数据量过大可以考虑替换成第三方MQ）
2. 可以设置开启多个线程执行用户数据去重，爬取用户数据，解析用户数据，爬取关注者数据，解析关注者数据
3. 使用内存Map处理抓取用户数据重复问题（如果抓取的用户数据过大，考虑替换成Redis去重）
4. 已经支持将爬取的用户数据持久化存储到MongoDB中（后续会支持MySQL，Elasticsearch等其他持久化存储）
5. 将抓取的关键日志输出到日志文件中，方便debug
