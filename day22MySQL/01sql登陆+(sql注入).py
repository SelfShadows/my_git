import pymysql

user = input('username:')
pwd = input('password:')

conn = pymysql.connect(host='localhost', user='root', password='', database='userinfo')  # 与数据库建立连接(打开柜子)
cursor = conn.cursor()  # 光标(用手去拿)
s1 = "select * from info where username='%s' and password='%s'" % (user, pwd)
# 不能在后面拼接,会有sql注入导致直接登陆成功(正确的用户名' -- )(任意数' or 1=1 -- )
cursor.execute(s1)  # 执行SQL语句
result = cursor.fetchone()  # 执行SQL语句的返回结果

cursor.close()  # 关闭光标
conn.close()  # 关闭连接uu

if result:  # result 有值
    print('登陆成功')
else:  # result 没有值
    print('登陆失败')
