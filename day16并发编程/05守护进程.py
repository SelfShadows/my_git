from multiprocessing import Process
import time

def func():
    while True:
        time.sleep(0.2)
        print('我还活着')
def func2():
    print('start')
    time.sleep(8)
    print('end')


if __name__=='__main__':
    p=Process(target=func)
    p.daemon=True           #设置子进程为守护进程    daemon release acquire   daemon
    p.start()
    p=Process(target=func2).start()
    for i in range(5):
        print('我是socket server')
        time.sleep(1)

#p.terminate()结束一个子进程
#p.is_alive() 检验一个子进程是否还或者，是返回True

#守护进程会随着 主进程的 代码执行完毕  而结束，(而不是主进程的结束而结束)
#在主程序内结束一个子进程 p.terminate()
    #结束一个进出不是在执行方法后立即生效，而是需要一个操作系统响应的过程
#p.name  p.pid 这个进程的名字和进程号