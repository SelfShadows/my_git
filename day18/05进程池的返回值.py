from multiprocessing import Pool
import time

def func(n):
    time.sleep(0.5)
    return n*n

if __name__=='__main__':
    p=Pool(5)
    res_1=[]

    for i in range(10):
        ret=p.apply_async(func,args=(i,))     #5个5个返回结果
        res_1.append(ret)
        # print(ret.get())      ret.get()会阻塞，等着func的计算结果
    for i in res_1:
        print(i.get())


    ret=p.map(func,range(10))     #100个任务执行完了在返回结果
    print(ret)

