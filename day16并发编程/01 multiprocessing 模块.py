from multiprocessing import Process
import os
import time


def func(args):
    print(args)
    print(12345)
    print('子进程:', os.getpid())
    print('子进程的父进程:', os.getppid())


if __name__ == '__main__':  # windows下必须要写这行代码，不然会报错
    p = Process(target=func, args=(1818,))  # 注册  ,argsw为要传的参数必须是个元祖，传一个参数要加,号
    # p是一个进程对象，还没有启动进程
    p.start()  # 开启一个子进程
    print('*****')
    time.sleep(0.2)
    print('父进程', os.getpid())  # os.getpid查看当前进程的进程号
    print('父进程的父进程', os.getppid())  # os.getppid查看当前父进程的进程号
