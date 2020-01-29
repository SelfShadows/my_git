import socket
import time
import os
import json
import struct
buffer=1024
sk=socket.socket()
sk.connect(('127.0.0.1',8080))

head_len=sk.recv(4)
head_len=struct.unpack('i',head_len)[0]
head=sk.recv(int(head_len)).decode('utf-8')
head=json.loads(head)
print(head)
file_size=head['filesize']
i=0
with open(head['filename'],'wb') as f:
    while file_size:
        i+=1
        print(file_size,i)
        if  file_size>=buffer:
            content=sk.recv(buffer)
            f.write(content)
            file_size-=buffer
        else:
            content=sk.recv(file_size)
            f.write(content)
            break

    print(file_size)

sk.close()