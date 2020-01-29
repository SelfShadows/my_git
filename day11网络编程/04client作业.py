import socket
import time
sk=socket.socket()
sk.connect(('127.0.0.1',8080))

while True:
    a=time.time()
    print(a)
    sk.send(bytes(str(a).encode('utf-8')))
    time.sleep(10)

sk.close()