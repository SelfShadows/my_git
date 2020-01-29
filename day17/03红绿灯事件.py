from multiprocessing import Event,Process
import time
import random
def car(e,i):
    if not e.is_set():
        print('车辆%s等待通行'%i)
        e.wait()      #阻塞，直到等到一个事件变为True的信号
    print('\033[30m车辆%s通过\033[0m'%i)

def light(e):
    while True:
        if  e.is_set():
            e.clear()
            print('\033[31m红灯亮了\033[0m')
        else:
            e.set()
            print('\033[32m绿灯亮了\033[0m')
        time.sleep(2)
if __name__=='__main__':
    e=Event()
    Process(target=light,args=(e,)).start()
    for i in range(20):
        cars=Process(target=car, args=(e,i))
        cars.start()
        time.sleep(random.random())