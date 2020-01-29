import pymysql

conn=pymysql.connect(host='localhost',user='root',password='',database='db10',charset='utf8')
cursor=conn.cursor()

user=('alex')
sql="select permiss from permission where id in (select permiss_id from relation where user_id in(select id from userinfo where %s=name))"
cursor.execute(sql,user)

result=cursor.fetchall()
print(result)

cursor.close()
conn.close()