import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))   #把client文件夹添加到sys.path里
print(os.path.dirname(os.path.dirname(os.getcwd())))
from conf.setting import addr
import socketserver
from core.server_main import MyFtpServer
if __name__=='__main__':

    server=socketserver.ThreadingTCPServer(addr,MyFtpServer)
    server.serve_forever()