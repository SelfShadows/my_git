import re


#ret=re.split('ab','abcd')
#print(ret)

# ret=re.search('[\d|\w](?P<name>\w.*?s)','sdfdf 3dd3fds2 13f')
# print(ret)
# print(ret.group('name'))


#命名
# ret=re.search('<(?P<flag_name>\w+)>\w+</(?P=flag_name)>','<tl>hello</tl>')
# print(ret.group())


#匹配整数
ret=re.findall('\d+\.\d+|(\d+)','8+4-2*5.21-5+10-(50.75+55)')
for i in ret:
    if i=='':
        ret.remove('')
print(ret)