

import json
'''json.dumps    json.loads   不加s后面要加文件名'''

dic = [{'k1':'11'},{'k2':'11'},{'k3':'11'}]
f = open('file','w')
for i in dic:
    str_dic=json.dumps(i)
    f.write(str_dic+'\n')
f = open('file')
cc = []
for i in f:
    t=json.loads(i.strip())
    cc.append(t)
f.close()
print(cc)
dic = [{'k1':'11'},{'k2':'11'},{'k3':'11'}]
dic1 = {'11':'22','33':'44'}
f=open('file','w')
for i in dic:
    json.dump(i,f)
f.close
# f=open('file','r')
# c=json.load(f)
# print(c)


