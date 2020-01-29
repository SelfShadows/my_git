from threading import Thread,RLock
import time
#Lock  互斥锁
#RLock 递归锁  是为了解决死锁问题  ，在一个线程里可以被acquire多次
#当在同一个线程或进程用到两把或以上锁的时候就容易出现死锁现象
    #这时就用递归锁
def eat1(name):
    noodle_look.acquire()           #一把钥匙
    print('%s拿到面条啦'%name)
    fork_look.acquire()
    print('%s拿到叉子了'%name)
    print('%s吃面'%name)
    fork_look.release()
    noodle_look.release()

def eat2(name):
    fork_look.acquire()
    print('%s拿到叉子了'%name)
    time.sleep(1)
    noodle_look.acquire()
    print('%s拿到面条啦' % name)
    print('%s吃面'%name)
    noodle_look.release()
    fork_look.release()



noodle_look=fork_look=RLock()        #一个钥匙串上的两把锁

Thread(target=eat1,args=('baoquan',)).start()
Thread(target=eat2,args=('bossjin',)).start()
Thread(target=eat1,args=('xiaoli',)).start()
Thread(target=eat2,args=('laoxiao',)).start()
