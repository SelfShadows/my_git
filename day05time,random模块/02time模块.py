import time

print(time.strftime("%Y-%m-%d  %X %j"))  # %j过了1年的第多少天
# 结构化化时间
# 时间戳和结构化时间
t = time.time()  # 时间戳
print(t)
print(time.localtime())  # 结构化时间
print(time.localtime(t))  # 本地时间，北京时间
print(time.localtime(2000000000))
print(time.gmtime())  # 美国时间

print(time.strptime('2019-7-17 15:52:44', '%Y-%m-%d %X'))  # 格式化时间转化为时间戳
print(time.mktime(time.localtime()))  # 结构化时间转化为时间戳
print(time.asctime())
