
# def generator():
#     print(123)
#     content=yield
#     print('====',content)
#     print(456)
#     yield
#
# g=generator()
# ret=g.__next__()
# print('***',ret)
# ret=g.send('hello')   #.__next__()和.send()效果一样
# print('***',ret)

#send 在获取下一个值的时候，给上一个yield的位置传递一个值
#使用send注意事项：
    #第一次使用生成器的时候 必须使用next 获取下一个值
    #最后一个yield不能接受外部的值
def init(average):
    def inner(*args,**kwargs):
        ret=average(*args,**kwargs)
        ret.__next__()
        return ret
    return inner

@init
def average():
    sum=0
    count=0
    avg=0
    while True:
        num = yield avg
        sum+=num
        count+=1
        avg=sum/count

avg_g=average()
a=avg_g.send(21)
a=avg_g.send(30)
print(a)