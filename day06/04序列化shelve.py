import shelve
# dic=[{'k1':'11'},{'k2':'11'},{'k3':'11'}]
# a=shelve.open('shelve_file')
# a['key']={'int':123,'float':936.3}
# a.close()

f1=shelve.open('shelve_file',flag='r')
c=f1['key']
print(c)
f1['key']=13
f1.close()

f1=shelve.open('shelve_file',flag='r')
c2=f1['key']
print(c2)
f1.close()