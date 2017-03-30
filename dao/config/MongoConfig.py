HOST = "127.0.0.1"
PORT = 27017
# 用于从此客户端上的查询返回的文档的默认类，这里映射为dict（也就是Map）
DOCUMENT_CLASS = dict
TZ_AWARE = False
CONNECT = True

# 用户名和密码
USER = "admin"
PWD = "admin_password"

# 可选参数
MAX_POOL_SIZE = 100
MIN_POOL_SIZE = 20

# 数据库
DB_ZHIHU = "zhihu"

# User用户表
TABLE_USER = "users"

# 常用查询条件
KEY_LIMIT = "limit"
VALUE_LIMIT = 20
