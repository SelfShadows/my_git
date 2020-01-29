from threading import Thread,Event
import time
import random

def connect_db(e):
    count=0
    while count<3:
        e.wait(0.5)                  #等待0.5秒后继续往下执行
        if e.is_set()==True:
            print('连接成功')
            break
        else:
            count+=1
            print('第%s次连接失败'%count)
    else:
        raise TimeoutError('数据库连接超时')  #主动抛出错误


def check_web(e):
    time.sleep(random.randint(0,3))
    e.set()

e=Event()

Thread(target=connect_db,args=(e,)).start()
Thread(target=check_web,args=(e,)).start()