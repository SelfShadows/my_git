import socket
import struct
import subprocess
sk=socket.socket()
sk.connect(('127.0.0.1',8080))
while  True:
    cmd=sk.recv(1024).decode('gbk')
    if cmd =='q':
        break
    res=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    std_out=res.stdout.read()
    std_err=res.stderr.read()
    len_num=len(std_out)+len(std_err)
    ret=struct.pack('i',len_num)
    sk.send(ret)
    sk.send(std_out)
    sk.send(std_err)



sk.close()