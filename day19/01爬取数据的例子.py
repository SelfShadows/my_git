import requests                                      #第一种获取网页内容的模块
from multiprocessing import Pool
from urllib.request import urlopen                    #第二种获取网页内容的模块
#200 网页正常的返回
#404 网页找不到  ，其他的数字是各种错误
def get(url):
    response=requests.get(url)
    if response.status_code == 200:
        return url,response.content.decode('utf-8')

def get_urllib(url):
    ret=urlopen(url)
    return url ,ret.read().decode('utf-8')

def call_back(args):                  #回调函数只能传一个参数
    url,content=args
    print(url,len(content))

if __name__=='__main__':
    url_lst=[
        'https://www.baidu.com/',
        'http://www.sohu.com/',
        'https://www.cnblogs.com/',
        'https://www.sogou.com/',
    ]
    p=Pool(5)
    for url in url_lst:
        p.apply_async(get,args=(url,),callback=call_back)
    p.close()
    p.join()

    print('-'*50)

    p2 = Pool(5)
    for url in url_lst:
        p2.apply_async(get_urllib, args=(url,), callback=call_back)
    p2.close()
    p2.join()