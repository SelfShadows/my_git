import socketserver
import json
from conf import setting
from core import views

class MyFtpServer(socketserver.BaseRequestHandler):
    def handle(self):
        msg=self.my_recv()
        op_str=msg['operation']
        if hasattr(views,op_str):
            pass
            func=getattr(views,op_str)
            ret=func(msg)
            print(ret)
            self.my_sennd(ret)

    def my_recv(self):
        msg=self.request.recv(1024)
        msg=msg.decode(setting.code)
        msg=json.loads(msg)
        return msg

    def my_sennd(self,msg):
        msg=json.dumps(msg,ensure_ascii=False).encode(setting.code)
        self.request.send(msg)
