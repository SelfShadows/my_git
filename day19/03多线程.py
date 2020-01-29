from threading import Thread
import time
#多线程并发  ,线程之间数据是共享的
#第一种启动方式

def func(n):
    time.sleep(1)
    print(n,g)
for i in range(10):
    t=Thread(target=func,args=(i,))
    t.start()
print('-'*50)
#第二种启动方式
class MyThread(Thread):
    def __init__(self,n):
        super().__init__()
        self.n=n
    def run(self):
        time.sleep(1)
        print(self.n)
for i in range(10):
    t=MyThread(i*100)
    t.start()

#进程是 最小的内存分配单位
#线程是 操作系统的最小单位
#线程被CPU执行了
#进程内至少含有一个线程
#进程中可以开启多个线程
    #开启一个线程所需要的时间要远远小于开启一个进程的时间
    #多个线程内部有自己的数据栈，数据不共享
    #全局变量在多个线程之间是共享的