import pymysql

user = 'xiaoli'
pwd = '1231ss23'
conn = pymysql.connect(host='localhost', user='root', password='xiaoli', database='userinfo')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 用字典显示

s1 = "insert into info(username,password) values (%s,%s)"
r = cursor.execute(s1, [user, pwd])

print(cursor.lastrowid)  # 获取刚插入数据的自增ID (当插入多行时获取最后一行的自增id)

conn.commit()

cursor.close()
conn.close()
