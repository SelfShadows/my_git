import socket
sk=socket.socket()                    #买手机
sk.connect(('127.0.0.1',8080))        #拨别人的号

while True:
    a=input('>>>')
    sk.send(bytes(a.encode('utf-8')))
    ret=sk.recv(1024).decode('utf-8')
    print(ret)
    if ret == 'bye':
        sk.send(b'bye')
        break
# sk.send(b'hello')                    #发送信息
# ret=sk.recv(1024)                   #接收到的信息
# print(ret)                          #打印收到的信息
# sk.send(bytes('中午吃什么'.encode('utf-8')))
# ret=sk.recv(1024)
# print(ret.decode('utf-8'))

sk.close()                          #关手机