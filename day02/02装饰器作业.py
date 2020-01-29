from urllib.request import urlopen
import os

def cache(funk):
    def inner(*args,**kwargs):
        if os.path.getsize('web_cache'):
            with open('web_cache', 'rb') as f:
                return f.read()
        ret=funk(*args,**kwargs)
        print(ret)
        with open('web_cache','wb') as f:
            f.write(b'fdsfddsgdfg')
        return ret
    return inner
@cache
def get(url):
    code=urlopen(url).read
    return code

ret=get('http://www.baidu.com')
print('11',ret)
print('11',ret)
print('11',ret)
