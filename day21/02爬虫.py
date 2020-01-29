from gevent  import monkey;monkey.patch_all()
import gevent
from urllib.request import urlopen   #内置的
import requests                      #需要安装

# url='http://www.baidu.com'
# res1=urlopen(url)
# res2=requests.get(url)
# print(res1)
# print(res2)
# print(res1.read().decode('utf-8'))     #有格式的
# print(res2.content.decode('utf-8'))    #无格式的

def get_url(url):
    response=urlopen(url)
    content=response.read().decode()
    return len(content)

url_lst=[
        'https://www.baidu.com/',
        'http://www.sohu.com/',
        'https://www.cnblogs.com/',
        'https://www.sogou.com/',
    ]

g1=gevent.spawn(get_url,'https://www.baidu.com')  #启动协程
g2=gevent.spawn(get_url,'http://www.sohu.com')
g3=gevent.spawn(get_url,'https://www.cnblogs.com')
g4=gevent.spawn(get_url,'https://www.sogou.com')

gevent.joinall([g1,g2,g3,g4])

print(g1.value)           #获取启动的协程的函数的返回值
print(g2.value)
print(g3.value)
print(g4.value)