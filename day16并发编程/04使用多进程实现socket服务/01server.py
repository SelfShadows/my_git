import socket
from multiprocessing import Process
def server(conn):
    while True:
        infoa='haha'.encode('utf-8')
        conn.send(infoa)
        msg = conn.recv(1024).decode('utf-8')
        print(msg)
    conn.close()
if __name__=='__main__':
    sk=socket.socket()
    sk.bind(('127.0.0.1',8090))
    sk.listen()

    while True:
        conn,addr = sk.accept()
        p=Process(target=server,args=(conn,))
        p.start()
    sk.close()