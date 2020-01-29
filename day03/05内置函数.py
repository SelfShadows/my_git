
from math  import sqrt
#导入数学模块  sqrt 开平方根

# reversed 得到一个反转的迭代器
# str=[1,2,3,4,5]
# a=reversed(str)
# for i in a:
#     print(i)
# sli=slice(3,4,1)
# print(str[sli])

# #去掉空和None
# def aa(x):
#     if type(x)==str:
#         return x and x.strip()
#     return x or x==0
# c=[0,3,1,'qq','','   ',0, None,'aa',546,'dd',5,5,2,21,4323,24]
# #            前面必须是个函数的名字
# ret=filter(aa,c)
# for i in ret:
#     print(i)
# #  filter 返回的是一个迭代器

# def bb(x):
#     return sqrt(x)% 1==0
# a1=filter(bb,range(1,101))
# for i in a1:
#     print(i)
#
# #abs取绝对值
# ret=map(abs,[1,-2,4,-5,2])
# for i in ret:
#     print(i)

#filter 执行后的结果集合<=执行前的个数
    #filter 只管筛选，不会改变原来的值

#map 执行前后元素个数不变
    # 值可能发生改变

q=[1,2,-3,4,123,55,6,-7]
print(sorted(q,reverse= True))
    #生成一个新列表 不改变原列表 占内存
q3=['  ',[33,44],'hello sorted']
print(sorted(q3,key=len))
    #按字符串长度进行排序

