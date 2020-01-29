from multiprocessing import Process,Queue
import time
#队列 先进先出
def produce(q):
    q.put('hello')      #放入队列中，如果队列满了会一直堵塞，直到从队列里取值后在放入队列
    q.put('ok')
    print(q.full())     #队列是否满了
def consume(q):
    print(q.empty())    #队列是否为空
    print(q.get())      #从队列中取值，如果队列里没有值会一直堵塞
    print(q.empty())    #队列是否为空
    while True:
        try:
            print(q.get_nowait())#从队列里取值，没有值会报错
        except:
            print('队列里已没有值')
            time.sleep(1)
if __name__=='__main__':
    q=Queue(1)                   #1代表队列可容纳的个数
    Process(target=produce,args=(q,)).start()
    Process(target=consume,args=(q,)).start()
