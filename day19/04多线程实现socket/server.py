from threading import Thread
import socket
def server_socket(conn):
    while True:
        info=input('>>>')
        conn.send(bytes(info.encode('utf-8')))
        msg = conn.recv(1024).decode('utf-8')
        print(msg)
    conn.close()

sk=socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()
while True:
    conn,addr=sk.accept()
    t = Thread(target=server_socket, args=(conn,))
    t.start()


sk.close()