#求输出结果
# def f (x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(l)
#
# f(2)
# f(3,[3,2,1])
# f(3)
# hello
#乘法口诀表
# for i in range(1,10):
#     for x in range(1,i+1):
#         print('%d*%d =%d  '%(i,x,i*x),end='')
#     print('')

#列表类型转换
# list3=[
#     {'name':'alex','hobby':'抽烟'},
#     {'name':'alex','hobby':'喝酒'},
#     {'name':'alex','hobby':'烫头'},
#     {'name':'alex','hobby':'Massage'},
#     {'name':'egon','hobby':'喊麦'},
#     {'name':'egon','hobby':'街舞'},
# ]
# list4=[]
# for i in list3:
#     for dic in list4:
#         if i['name']==dic['name']:
#             dic['hobby_list'].append(i['hobby'])
#             break
#     else:
#         list4.append({'name': i['name'], 'hobby_list':[i['hobby']]})
# for i in list4:
#     print(i)

class Student():

    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def get_course(self):
        # for i in self.course:
        #     if self.course[0]>=self.course[1]:
        #         if self.course[0]>=self.course[2]:
        #             return self.course[0]
        #         else:
        #             return self.course[2]
        #     else:
        #         if self.course[1]>=self.course[2]:
        #             return self.course[1]
        #         else:
        #             return self.course[2]
        self.course.sort()
        return self.course[0]

li=Student('lijinjin',21,[130,30,533])

print(li.name)
print(li.age)
print(li.get_course())
