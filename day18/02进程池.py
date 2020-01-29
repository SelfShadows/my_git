from multiprocessing import Process,Pool
import time

def func(n):
    for i in range(10):
        print(n+1)
def func2(n):
    print(n[0])
    print(n[1])
    print(123)
if __name__=='__main__':
    t=time.time()

    pool=Pool(5)                    #同一时间只开启5个进程,一般开启cpu个数加1个进程
    pool.map(func,range(100))       #100个任务,自带join功能
    pool.map(func2,[('hello','world'),('python',333)])       #100个任务,先执行前100个在执行这一行的两个进程
                  #第二个参数为可迭代的
    
    t1=time.time()-t




    t2=time.time()
    # for i in range(100):
    #     p=Process(target=func,args=(i,))
    #     p.start()
    # for i in range(100):p.join()
    t2=time.time()-t2
    print(t1,t2)