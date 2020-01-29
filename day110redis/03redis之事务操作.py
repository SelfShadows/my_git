import redis
from day110redis.redis单例模式 import my_redis
conn = redis.Redis(connection_pool=my_redis.POOL)

# pipe = conn.pipeline(transaction=True)
# pipe.multi()
#
# pipe.set('k11', '111')
# pipe.hset('k12', 'name', '222')
# pipe.lpush('k13', '333')
#
# pipe.execute()

print(conn.get('k11'))
print(conn.hget('k12', 'name'))  # 字典
print(conn.lrange('k13', 0, 100))  # 列表

