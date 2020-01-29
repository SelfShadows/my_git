


egg_list=['鸡蛋%s'%i for i in range(10)] #列表推导式
print(egg_list)

老母鸡=('鸡蛋%s'%i for i in range(10)) #生成器
for 蛋 in 老母鸡:
    print(蛋)

ret=[i for i in range(30) if i%3==0] #完整的列表推导式
print(ret)

# g=(i for i in range(10))  #生成器表达式
# print(g)
# for i in g:
#     print(i)
#
# #括号不一样
# #返回的值不一样=====几乎不占用内存
#
# g=(i**2 for i in range(10))
# for i in g:
#     print(i)