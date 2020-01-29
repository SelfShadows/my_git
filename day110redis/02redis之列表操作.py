import redis
from day110redis.redis单例模式 import my_redis

'''
redis之列表操作:
redis = {
    k1:[1,4,5,6]
}
队列：先进先出
栈：  后进先出

'''
conn = redis.Redis(connection_pool=my_redis.POOL)


# conn = redis.Redis(host='192.168.52.128', port=6379, password="xiaoli")
# conn.lpush('k6', 'qq1')  # 从列表左边添加数据
# conn.rpush('k6', 222)  # 从列表右边添加数据
# conn.lpush('k6', *[333, 1, 2, 3, 4, 123, 412, 234, 54356, 5467765])  # 插入多个值

# val = conn.lpop('k6')  # 从列表左边移除数据
# val = conn.rpop('k6')  # 从列表右边移除数据

# val = conn.blpop('k6', timeout=3)  # 从列表左边移除数据, 没有数据就一直等(等待timeout设置的时间，超过时间返回None)
# val = conn.brpop('k6', timeout=3)  # 从列表右边移除数据, 没有数据就一直等(等待timeout设置的时间，超过时间返回None)

result = conn.lrange('k6', 0, 100)
print(result)

def getlist(key, count=2):
    index = 0
    while True:
        data_list = conn.lrange(key, index, index + count - 1)
        if not data_list:
            return
        index += count

        for item in data_list:  # 用生成器一点一点取
            yield item


for item in getlist('k6'):
    print(item)
