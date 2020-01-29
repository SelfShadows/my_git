import socket
from multiprocessing import Pool
def server(conn):
    while True:
        conn.send(b'hello')
        ret = conn.recv(1025).decode('utf-8')
        print(ret)
    conn.close()
if __name__=='__main__':
    p = Pool(2)
    sk=socket.socket()
    sk.bind(('127.0.0.1',8080))
    sk.listen()
    while True:
        conn, addr = sk.accept()
        p.apply_async(server,args=(conn,))
    sk.close()