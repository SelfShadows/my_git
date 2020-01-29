import collections
dq=collections.deque([1,2])
dq.append('a')
dq.appendleft('b')
dq.insert(2,3)
print(dq.pop())
print(dq)


# list=[11,677,89,44,55,66,772,88]
# a={}
# a[123]=[1,2]
# print(a)
# b=[]
# for i in list:
#     if i >50:
#         b.append(i)
#     a['k1']=b
# print(a)