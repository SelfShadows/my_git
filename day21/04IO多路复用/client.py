from gevent import monkey;monkey.patch_all()
import socket
from threading import Thread
import gevent
import time
def connect():
    sk=socket.socket()
    sk.connect(('127.0.0.1',8080))
    time.sleep(1)
    sk.send(b'hello')
    print(sk.recv(1024).decode('utf-8'))
    sk.close()

for i in range(100):
    g=gevent.spawn(connect)

for i in range(100):
    g.join()



