import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):       #self.request 相当于一个conn
        while True:
            msg=self.request.recv(1024).decode('utf-8')
            print(msg)
            info=input(">>>")
            self.request.send(bytes(info.encode('utf-8')))

server=socketserver.ThreadingTCPServer(('127.0.0.1',8080),MyServer)
#thread 线程
server.serve_forever()