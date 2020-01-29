from multiprocessing import Process,Pipe

def func(conn1,conn2):
    conn2.close()
    while True:
        try:
            msg=conn1.recv()
            # if msg==None:break
            print(msg)
        except EOFError :
            conn1.close()
            break


if __name__=='__main__':
    conn1,conn2=Pipe()
    p1=Process(target=func,args=(conn1,conn2))
    p1.start()
    conn1.close()
    for i in range(5):
        conn2.send('hello')
    conn2.close()
    # conn2.send(None)

#管道在传输的时候不安全，需要加锁，才能安全，底层用的socket