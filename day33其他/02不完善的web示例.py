import socket
sk=socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen(5)


while 1:
    conn,addr = sk.accept()
    data=conn.recv(1024)
    print(data)
    conn.send(b'HTTP/1.1 200 OK\r\ncontent-type:text/html; charset=utf-8\r\n\r\n')
    conn.send(b'<h3>hello</h3>')
    conn.close()
sk.close()