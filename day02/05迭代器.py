

# print(dir([]))  #告诉我列表拥有的所有方法
# print(dir({}))  #告诉我字典拥有的所有方法
# print(dir(''))  #告诉我字符串拥有的所有方法
# print(dir(range(10)))  #告诉我range拥有的所有方法
# ret=set(dir([])) &  set(dir({})) &  set(dir('')) &  set(dir(range(10)))
# print(ret)
#双下方法
# a=[1]
# b=[2]
# print(a.__add__(b))
#1+2 -->__and__ -->3
#只要能被for循环的数据类型  就一定有__iter__方法
print([].__iter__())
print(set(dir([].__iter__())) - set(dir([])))
print([1,2,3].__iter__().__length_hint__())
#一个列表执行了__iter__()之后的返回值就是一个迭代器

#Iterable  可迭代的   ==>__iter__   #只要含有__iter__方法的都是可迭代的
#[].__iter__() 迭代器 ==> __next__　＃通过  next  就可以从迭代器中一个一个取值

#只要含有  iter  方法的都是可迭代的 ———— python的  可迭代协议
#迭代器协议————内部含有  next  和  iter  方法的就是迭代器
#迭代器一定可迭代
#可迭代的.__iter__()方法就可以得到一个迭代器
#迭代器中的  next  ()方法可以一个一个的获取值