### Mongo容器配置

```
# 下载Mongo的镜像
$ docker pull mongo:3.2

# 运行Mongo的容器（不需要登录验证）
$ docker run -v /Users/yunyu/Downloads/zhihu/mongo/data:/data/db -v /Users/yunyu/Downloads/zhihu/mongo/conf:/data/configdb -p 27017:27017 --name zhihu_mongo -d mongo:3.2 mongod

# 客户端连接Mongo容器
$ mongo 127.0.0.1:27017
> show dbs;
local  0.000GB

# 使用admin数据库
> use admin

# 在admin数据库下创建admin用户
> db.createUser({ user: 'admin', pwd: 'admin_password', roles: [ { role: "readWriteAnyDatabase", db: "admin" }, { role: "userAdminAnyDatabase", db: "admin" }, { role: "clusterMonitor", db:"admin" } ] });

# 使用zhihu数据库
> use zhihu

# 在zhihu数据库下创建zhihu用户
> db.createUser({ user: 'zhihu', pwd: 'zhihu_password', roles: [ { role: "readWrite", db: "zhihu" }, { role: "dbAdmin", db: "zhihu" }, { role: "backup", db:"admin" }, { role: "restore", db:"admin" } ] });

# 查看admin数据库下的collection表
> show tables;
system.users
system.version

# 运行Mongo的容器（需要登录验证）
$ docker run -v /Users/yunyu/Downloads/zhihu/mongo/data:/data/db -v /Users/yunyu/Downloads/zhihu/mongo/conf:/data/configdb -p 27017:27017 --name zhihu_mongo -d mongo:3.2 mongod --auth

# 客户端连接Mongo容器
$ mongo 127.0.0.1:27017 -u admin -p admin_password --authenticationDatabase admin

```

说明：MongoDB默认是不需要输入用户名和密码，客户就可以登录的。但是出于安全性的考虑，我们还是要为其设置用户名和密码。

参考文章：

- https://hub.docker.com/_/mongo/
- https://github.com/docker-library/mongo/blob/1047c0e9975a32102595bc824a2655dee22e595a/3.2/Dockerfile
- http://blog.csdn.net/lyj1101066558/article/details/50606628
- http://blog.csdn.net/jianlong727/article/details/53889990

### Redis容器配置

```
# 下载Redis的镜像
$ docker pull redis:3.2

# 编辑Redis配置文件
$ vi /Users/yunyu/Downloads/zhihu/redis/conf/redis.conf

# 运行Redis的容器
$ docker run -v /Users/yunyu/Downloads/zhihu/redis:/data -p 6379:6379 --name zhihu_redis -d redis:3.2 redis-server /data/conf/redis.conf

# 客户端连接Redis容器
$ redis-cli -h localhost -p 6379
localhost:6379> auth "你的密码"
```

参考文章：

- https://hub.docker.com/_/redis/