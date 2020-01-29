import socket
sk=socket.socket()
sk.connect(('192.168.0.24',8080))

ret=sk.recv(1024).decode('utf-8')
print(ret)
u=input('user:')
p=input('passworld:')
sk.send(bytes(u.encode('utf-8')))
sk.send(bytes(p.encode('utf-8')))
dl=sk.recv(1024).decode('utf-8')
print(dl)
d2=sk.recv(1024).decode('utf-8')
print(d2)
if dl=='登陆成功':
    while True:
        z= input('输入你想要的操作:')
        sk.send(bytes(z.encode('utf-8')))
        if z=='1':
            print(z)
            dd = sk.recv(1024).decode('utf-8')
            print(dd)
            pwd=input('>>>')
            sk.send(bytes(pwd.encode('utf-8')))
            with open(pwd,encoding='utf-8') as f:
                read=f.read()
                sk.send(bytes(read.encode('utf-8')))
                break
        if z == '1':
            print(z)
        if z=='已退出':
            break
sk.close()
