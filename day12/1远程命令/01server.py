import socket
import struct
sk=socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()

conn,addr=sk.accept()
while True:
    cmd=input('>>>')
    if cmd=='q':
        conn.send(b'q')
        break
    conn.send(bytes(cmd.encode('gbk')))
    num=conn.recv(4)
    print(num)
    num=struct.unpack('i',num)[0]
    print(num)
    ret=conn.recv(int(num)).decode('gbk')
    print(ret)

conn.close()
sk.close()