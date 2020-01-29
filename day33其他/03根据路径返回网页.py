import socket
sk=socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen(5)

def register(url):
    with open('04信息收集卡.html', encoding='utf-8') as f:
        ret = f.read()
    return ret.encode()

def login(url):
    with open('05登陆.html', encoding='utf-8') as f:
        ret = f.read()
    return ret.encode()
def f404(url):
    return '找不到 {}'.format(url).encode()

list_url=[
    ('/register', register),
    ('/login', login)
]

while 1:
    conn,addr = sk.accept()
    data=conn.recv(4096).decode()
    list_data=data.split('\r\n')
    data=list_data[0].split()
    url=data[1]
    print(url)
    for i in list_url:
        if i[0] == url:
            func = i[1]
            print(func)
            break
        else:
            func=f404
    conn.send(b'HTTP/1.1 200 OK\r\ncontent-type:text/html; charset=utf-8\r\n\r\n')
    respons=func(url)

    conn.send(respons)


    conn.close()
sk.close()