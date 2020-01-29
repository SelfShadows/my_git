import pymysql
# 查
# cursor.scroll(1,mode='relative') #相对当前位置移动
# cursor.scroll(2,mode='absolute') #相对绝对位置移动
conn=pymysql.connect(host='localhost',user='root',password='',database='userinfo')
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor) #用字典显示

s1="select * from info"
cursor.execute(s1)

result=cursor.fetchone()  # 从数据库拿一条数据*****
print(result)
result=cursor.fetchmany(4)  # 从数据库拿4条数据
print(result)
# cursor.scroll(0,mode='absolute') #相对绝对位置移动
result=cursor.fetchall()  # 从数据库拿所有的数据*****    #根据指针位置拿指针之后的全部数据
print(result)

cursor.close()
conn.close()