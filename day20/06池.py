import time
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
                               #线程池             #进程池

def func(n):
    time.sleep(2)
    print(n)
    return n*n
       #改成ProcessPoolExecutor就变成进程池了，其他都不变
pool_t=ThreadPoolExecutor(5)    #一般不超过cpu个数*5
t_lst=[]
for i in range(20):
    ret=pool_t.submit(func,i)
    t_lst.append(ret)
pool_t.shutdown()   #close+join
print('主线程')
for i in t_lst:
    print('**',i.result())   #相当于get