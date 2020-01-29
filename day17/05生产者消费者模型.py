from multiprocessing import Process,Queue
import random
import time
def producer(name,food,q):
    for i in range(10):
        time.sleep(random.randint(1,2))
        f='%s生产的第%s个%s'%(name,i,food)
        print(f)
        q.put(f)

def consumer(name,q):
    while True:
        f=q.get()
        if f==None:break
        print('\033[31m%s消费了%s\033[0m'%(name,f))
        time.sleep(random.randint(1,2))

if __name__=='__main__':
    q=Queue()
    p1=Process(target=producer,args=('alex','包子',q))
    p1.start()
    c1 = Process(target=consumer, args=('jinboss',q))
    c1.start()
    p2 = Process(target=producer, args=('baoquan', '土豆', q))
    p2.start()
    c2 = Process(target=consumer, args=('xiaoli', q))
    c2.start()
    p1.join()
    p2.join()
    q.put(None)
    q.put(None)