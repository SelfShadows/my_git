from threading import Thread
import time
def func1():
    while True:
        print('*'*40)
        time.sleep(1)

def func2():
    print('in func2')
    time.sleep(5)


t=Thread(target=func1)
t.daemon=True
t.start()
t2=Thread(target=func2)
t2.start()

print('主进程结束')

#守护进程会随着主进程的代码执行结束而结束
#守护线程会在主线程代码结束之后等待其他子线程的结束才结束
