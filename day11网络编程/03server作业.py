import socket
import time

sk=socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()
conn,addr=sk.accept()

while True:
    ret=conn.recv(1024).decode('utf-8')
    ret=float(ret)
    ret=time.localtime(ret)
    print(ret)


conn.close()
sk.close()
