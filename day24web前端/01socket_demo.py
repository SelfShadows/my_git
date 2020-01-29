import socket
sk=socket.socket()
sk.bind(('127.0.0.1', 900))
sk.listen(5)


while 1:
    conn,addr = sk.accept()
    data=conn.recv(1024)
    print(data)
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    with open('02data1.html', 'rb') as f:
        msg=f.read()
    conn.send(msg)

    conn.close()
sk.close()

