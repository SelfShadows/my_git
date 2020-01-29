import redis
'''
    redis之单例模式
'''


class MyRedis(object):
    POOL = redis.ConnectionPool(host='192.168.52.128', port=6379, password='xiaoli', max_connections=1000)


my_redis = MyRedis()
