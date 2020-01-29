from multiprocessing import Process
from multiprocessing import Lock   #导入锁模块
import time
import json

def show(i):
    with open('ticket') as f:
        dic=json.load(f)
        print('%s查看余票：%s'%(i,dic['ticket']))

def buy_ticket(i,lock):
    lock.acquire()           #拿钥匙进门(获得锁）multiprocessing process Lock acquire  release   daemon tacket
    with open('ticket') as f:
        dic=json.load(f)
        time.sleep(0.1)
    if dic['ticket'] > 0:
        dic['ticket']-=1
        print('%s购票成功'%i)
    else:
        print('%s票已售光'%i)
    time.sleep(0.1)
    with open('ticket','w')as f:
        json.dump(dic,f)
    lock.release()            #还钥匙（释放锁）


if __name__=='__main__':
    for i in range(1,6):
        p=Process(target=show,args=(i,))
        p.start()
    lock=Lock()             #实例化一个锁的对象
    for i in range(1,11):
        p=Process(target=buy_ticket,args=(i,lock))
        p.start()
