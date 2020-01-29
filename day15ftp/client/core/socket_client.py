import socket
import json

class MySocketClient:
    def __init__(self):
        self.sk=socket.socket()
        self.sk.connect(('127.0.0.1',8080))

    def mysend(self,msg):
        ret_json=json.dumps(msg)
        self.sk.send(ret_json.encode('utf-8'))

    def myrecv(self):
        msg=self.sk.recv(1024).decode('utf-8')
        msg=json.loads(msg)
        return msg