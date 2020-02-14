from threading import Timer
import time


def func():
    print('时间同步')
    time.sleep(10)


Timer(2, func).start()  # 过两秒后开启这个线程
print('haha')
