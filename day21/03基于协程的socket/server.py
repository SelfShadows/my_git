from    gevent import monkey;monkey.patch_all()
import socket
import gevent

def myserver(conn):
    while True:
        conn.send(b'hello')
        ret=conn.recv(1024).decode('utf-8')
        print(ret)
    conn.close()
sk=socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()
while True:
    conn,addr=sk.accept()
    g=gevent.spawn(myserver,conn)
