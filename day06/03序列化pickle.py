import pickle
dic=[{'k1':'11'},{'k2':'11'},{'k3':'11'}]
dic1={'11':'22','33':'44'}
f=open('f','wb')
s=pickle.dumps(dic1)
print(s)
f.write(s)
f.close()
f=open('f','rb')
c=pickle.load(f)
print(c)