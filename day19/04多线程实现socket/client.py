import socket
sk=socket.socket()
sk.connect(('127.0.0.1',8080))
while True:
    msg=sk.recv(1024).decode('utf-8')
    print(msg)
    info=input('>>>')
    sk.send(bytes(info.encode('utf-8')))


sk.close()