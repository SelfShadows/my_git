import socket
import select

sk=socket.socket()
sk.bind(('127.0.0.1',8080))
sk.setblocking(False)
sk.listen()

read_list=[sk]
while True:
    r_list,w_list,x_list=select.select(read_list,[],[])
    for i in r_list:
        if i is sk:
            conn,addr=sk.accept()
            read_list.append(conn)
        else:
            ret=i.recv(1024)
            if ret==b'':
                i.close()
                read_list.remove(i)
                continue
            print(ret)
            i.send(b'goodbye!')

