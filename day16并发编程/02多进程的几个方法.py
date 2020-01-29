from   multiprocessing import Process
import time
import os

def func(args1,args2):
    print('*'*args1)
    time.sleep(0.05)
    print('='*args2)

def write_file(filename,info):
    with open(filename,'w') as f:
        f.write(info)

if __name__=='__main__':
    # p=Process(target=func,args=(10,20))
    # p.start()
    # p.join()      #感知一个子进程的结束，将异步改为同步
    # print('====程序结束')

    p_list=[]
    for i in range(1,6):
        p=Process(target=write_file,args=('info+%s'%i,'%s'%i))
        p_list.append(p)
        p.start()
    [p.join() for p in p_list]     #之前的所有进程必须在这里全部执行完，才能执行下面的代码
    # for i in range(1,6):         #感知了5个子程序的结束
    #     p.join()
    print([i for i in os.walk(r'D:\01python\day16多进程')])