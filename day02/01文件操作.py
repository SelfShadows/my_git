# username=input('请输入你要注册的用户名：')
# password=input('请输入你要注册的密码：')
# with open('list_of_info','w',encoding='utf-8') as f:
#     f.write('{}\n{}'.format(username,password))
# print('注册成功')
list=[]
i =0
while i<3:
    uname = input('请输入用户名：')
    pword = input('请输入密码：')
    with open('list_of_info','r+',encoding='utf-8') as f:
        for line in f:
            list.append(line)
    if uname==list[0].strip()   and pword == list[1].strip():
        print('登陆成功')
        break
    else:
        print('账号密码错误')
        if i== 2:
            print('登陆错误3次，账号已被冻结1天')

    i+=1

