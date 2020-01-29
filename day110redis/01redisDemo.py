import redis


# conn = redis.Redis(host='192.168.52.128', port=6379, password="xiaoli")
# conn.set('k2', 'xiaoli')
# val = conn.get("k2")
# print(val)


POOL = redis.ConnectionPool(host='192.168.52.128', port=6379, password='xiaoli', max_connections=1000)
conn = redis.Redis(connection_pool=POOL)
'''
redis之字典操作：
redis = {
    k4:{
        username: alex,
        age: 18
     }
}
'''

# conn.hset('k4', "username", 'alex')
# conn.hset("k4", 'age', 18)
conn.hmset("k4", {'username': 'alex', 'age': 18})
#
val = conn.hget('k4', 'username')
# print(val)

# 计数器
print(conn.hget('k4', 'age'))
conn.hincrby('k4', 'age', amount=2)  # 计数间隔 可以设为负数
print(conn.hget('k4', 'age'))

'''问题：如果redis的k4对应的字典中有1000w条数据，请打印所有的数据'''
# -- 不可用hgetall （从redis取到数据后，服务器内存无法承受，爆栈）
result = conn.hgetall('k4')
print(result)
# 应该这样:
result = conn.hscan_iter("k4", count=100)  # 一次取100个数据
for item in result:
    print(item)
