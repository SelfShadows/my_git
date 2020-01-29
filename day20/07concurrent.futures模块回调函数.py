import time
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
                               #线程池             #进程池

def func(n):
    time.sleep(2)
    print(n)
    return n*n

def call_back(m):
    print('结果是%s'%m.result())

t=ThreadPoolExecutor(5)
for i in range(20):
    t.submit(func,i).add_done_callback(call_back)