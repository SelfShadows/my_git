import socket
sk=socket.socket(type=socket.SOCK_DGRAM)     #DGRAM  datagram
sk.bind(('127.0.0.1',8080))
while True:
    msg,addr=sk.recvfrom(1024)
    print(msg.decode('utf-8'))
    info = input('服务器:')
    info = ('\033[34m来自服务器发送的消息:\033[0m%s'%info).encode('utf-8')
    sk.sendto(bytes(info),addr)

sk.close()