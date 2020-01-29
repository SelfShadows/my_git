from multiprocessing import Process
from multiprocessing import Semaphore
import time
import random
def ktv(i,sem):
    sem.acquire()                 #获取钥匙                     semaphore  lock acquire relase samaphore daemon
    print('%s 进 '%i)
    time.sleep(random.randint(0,10))
    print('%s  出'%i)
    sem.release()                 #还钥匙

if __name__=='__main__':
    sem=Semaphore(2)           #设置同时有几个进程运行
    for i in range(10):
        p=Process(target=ktv,args=(i,sem))
        p.start()