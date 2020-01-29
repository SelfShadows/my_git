import time

#计算2019年7月15日8点于现在相差多少年，月，日，分，秒
t_now=time.time()#获取现在的时间戳
t1=time.strptime('2019-8-2 18:00:00','%Y-%m-%d %X')#把以前的时间转化成格式化时间
t2=time.mktime(t1)#转化成时间戳
t3=t_now-t2
t4=time.localtime(t3)#把时间戳转化成格式化时间
print(t4)
print('过去了%d年%d月%d日%d小时%d分钟%d秒'%(t4.tm_year-1970,t4.tm_mon-1,t4.tm_mday-1,t4.tm_hour-8,t4.tm_min,t4.tm_sec))
print(time.localtime(0))
print(time.localtime())
print(time.strftime("%Y-%m-%d  %X %j",t4))
# t=time.localtime()
# print('%d-%d-%d'%(t.tm_year,t.tm_mon,t.tm_mday-2))