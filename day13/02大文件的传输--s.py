import socket
import os
import json
import time
import struct
buffer=1024
sk=socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()
conn,addr=sk.accept()

head={'filepath':'D:\Downloads',
      'filename':'YNote.exe',
      'filesize':None}
filepath=os.path.join(head['filepath'],head['filename'])
filesize=os.path.getsize(filepath)
head['filesize']=filesize
head_dumps=json.dumps(head).encode('utf-8')
len_head=len(head_dumps)
len_pack=struct.pack('i',len_head)
conn.send(len_pack)
conn.send(head_dumps)
print(filepath)
i=0
with open(filepath,'rb') as f:
    while filesize:
        i+=1
        print(filesize,i)
        if filesize>=buffer:
            content=f.read(buffer)
            conn.send(content)
            filesize-=buffer
        else:
            content=f.read(filesize)
            conn.send(content)
            break



conn.close()
sk.close()



