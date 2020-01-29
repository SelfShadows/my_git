'''
%和format的区别
'''
# Python2.6 新加入的format语法支持
# 3.6加入了一个 f-strings新特性
# 新版Python推荐使用 format

a = (250, 250)

command1='二营长，向他开炮：敌人的坐标:%s' % (a, )
print(command1)

command2='二营长，向他开炮：敌人的坐标:{}'.format(a)
print(command2)
print('-'*50)

name = 'Alex'
age = 9000
s1 = "{} is {}".format(name,age)
print('s1:', s1)
s2 = f"{name} is {age}"
print('s2:', s2)
