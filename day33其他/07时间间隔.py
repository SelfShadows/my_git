import datetime

now = datetime.datetime.now()
print(now)
# 七天,两小时，20分钟
d7 = datetime.timedelta(days=7, hours=2, minutes=20)
print(d7)

# 现在的的时间加上 七天,两小时，20分钟
ret = now + d7

print(ret)