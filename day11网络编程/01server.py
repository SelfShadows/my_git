import socket
sk=socket.socket()             #买手机
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)        #避免服务器重启的时候报 address already in use 的错误
#sk.bind(('ip','port'))        #绑定手机卡
sk.bind(('127.0.0.1',8080))    #绑定手机卡
sk.listen()                    #监听    等着别人给我打电话

conn,addr=sk.accept()          #接收到别人的电话   connection   连接   ， address  地址
print(addr,conn)
while True:
    ret=conn.recv(1024).decode('utf-8')
    print(ret)
    if ret =='bye':
        conn.send(b'bye')
        break
    a=input('>>>')
    conn.send(bytes(a.encode('utf-8')))

# ret=conn.recv(1024)            #听别人说话   接受1024个字节以内的字节
# print(ret)
# conn.send(b'hi')               #和别人说话，必须传一个bytes类型
# ret=conn.recv(1024)
# print(ret.decode('utf-8'))
# conn.send(bytes('吃饺子',encoding='utf-8'))


conn.close()                  #挂电话
sk.close()                    #关手机


#send  ---  recv
#send  ---  recv
#recv  ---  send

#有收必有发，收发必相等