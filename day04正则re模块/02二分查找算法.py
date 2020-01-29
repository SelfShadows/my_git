# def func(a):
# #     if a==1:
# #         return 1
# #     return a*func(a-1)
# #
# # aa=func(int(4))
# # print(aa)

aa=[11,22,33,44,55,66,77,88,99,121,233,444,555,666,777]

def find(list,num,start=0,end=None):
    end=len(list) if end is None  else end
    middle=(end-start)//2 +start
    print(end,start,middle)
    if start <=end:
        if num < list[middle]:
            return find(list,num,start=start,end=middle-1)
        elif num > list[middle]:
            return find(list,num,start=middle+1,end=end)
        else:
           return middle
    else:
        return '没有这个数'

aaa=find(aa,99)
print(aaa)
