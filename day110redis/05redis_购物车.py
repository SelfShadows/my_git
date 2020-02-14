import redis
import json
from day110redis.redis单例模式 import my_redis

conn = redis.Redis(connection_pool=my_redis.POOL)
# conn.flushall()  # 清楚所有缓存
# v = conn.keys()  # 所有键
'''购物车：
第一版：
redis = {
    luffy_shopping_car : {
        user_id : {
            course_id : {
                course_detail :{
                
                }
            }
        }
    }
}
第二版：
redis = {   
    luffy_shopping_car_uid_cid : {
        course_detail :{
        
        }
    }
}
'''
# 添加课程
# redis_key = "luffy_shopping_car_%s_%s" % (5, 11)  # 用户id, 课程id
# conn.hmset(redis_key, {'title': "21天入门到放弃", "src": "xx/xx.png"})

# 删除课程
# conn.delete('luffy_shopping_car_6_14')
# print(conn.keys())

# 修改课程
# conn.hset('luffy_shopping_car_6_12', 'src', 'x1/x1.png')
# print(conn.hget('luffy_shopping_car_6_12', 'src'))

# 查看所有课程
# print(conn.keys('luffy_shopping_car_6_*'))
# for item in conn.scan_iter('luffy_shopping_car_6_*', count=10):  # 数据多就用scan_iter
#     course = conn.hgetall(item)
#     print(course)

print(conn.keys())
# print(conn.exists('shopping_car_2_1'))  # 判断是否有这个key 有返回1，没有返回0
# """结算：
#     redis = {
#     "payment_userId_curseId": {
#     "course_id" :
#     "policy_date" ：
#     "price" :
#     "coupon": {}
#     }
# }
# """
# payment_list = []
#
# for i in conn.scan_iter("payment_2_*"):
#     print(conn.hgetall(i))
#
# print(conn.hgetall("payment_global_2"))


