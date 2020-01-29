import random

a=[]
for i in range(3):
    b=random.randint(1,10)
    a.append(str(b))
for i in range(3):
    c=random.randint(65,90)
    a.append(chr(c))
c=''.join(list(a))
print(c)
y=input('请输入验证码：')
if y==c:
    print('验证成功')
else:
    print('验证码输入错误')
