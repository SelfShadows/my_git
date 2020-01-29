# from greenlet import greenlet
# def eat():
#     print('eating start')
#     g2.switch()
#     print('eating end')
#     g2.switch()
# def play():
#     print('playing start')
#     g1.switch()
#     print('playing end')
#
# g1=greenlet(eat)
# g2=greenlet(play)
# g1.switch()

#进程和线程的任务切换由操作系统完成
#协程任务之间的切换有程序(代码)来完成
from gevent import monkey;monkey.patch_all()  #对其他的IO操作进行打补丁，识别如(time,socket)中的IO操作
import time                                        #必须放在最前面,最好放在文件开头
import gevent
import threading
def eat():
    print(threading.current_thread())
    print('eating start')
    time.sleep(1)
    print('eating end')
def play():
    print(threading.current_thread())
    print('playing start')
    time.sleep(1)
    print('playing end')

g1=gevent.spawn(eat)
g2=gevent.spawn(play)
g1.join()
g2.join()