from multiprocessing import Pool
import os
def func1(n):
    print('in func1 ',os.getpid())
    return n*n

def func2(nn):
    print(nn)
    print('in func2 ',os.getpid())

if __name__=='__main__':
    print('in 主 ',os.getpid())
    p=Pool(5)
    p.apply_async(func1,args=(3,),callback=func2)
    p.close()
    p.join()


#回调函数在主进程中运行