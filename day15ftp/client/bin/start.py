import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))   #把client文件夹添加到sys.path里

from core import client_main
if __name__=='__main__':
    client_main.main()