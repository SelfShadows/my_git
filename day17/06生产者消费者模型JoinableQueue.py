from multiprocessing import Process,JoinableQueue
import random
import time
def producer(name,food,q):
    for i in range(4):
        time.sleep(random.randint(1,2))
        f='%s生产的第%s个%s'%(name,i,food)
        print(f)
        q.put(f)
    q.join()         #阻塞，直到一个队列中的数据 全部被处理完毕

def consumer(name,q):
    while True:
        f=q.get()
        print('\033[31m%s消费了%s\033[0m'%(name,f))
        time.sleep(random.randint(1,2))
        q.task_done()  #count-1

if __name__=='__main__':
    q=JoinableQueue()

    p1=Process(target=producer,args=('alex','包子',q))
    c1 = Process(target=consumer, args=('jinboss',q))
    p2 = Process(target=producer, args=('baoquan', '土豆', q))
    c2 = Process(target=consumer, args=('xiaoli', q))
    p1.start()
    p2.start()
    c1.daemon=True            #设置消费者为守护进程（主进程代码执行结束，消费者进程执行结束）
    c2.daemon=True
    c1.start()
    c2.start()
    p1.join()
    p2.join()
