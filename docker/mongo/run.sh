docker run -v /Users/yunyu/Downloads/zhihu/mongo/data:/data/db -v /Users/yunyu/Downloads/zhihu/mongo/conf:/data/configdb -p 27017:27017 --name zhihu_mongo -d mongo:3.2 mongod