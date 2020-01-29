# import logging
#
# file_handler = logging.FileHandler(filename='x1.log', mode='a', encoding='utf-8',)
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     handlers=[file_handler,],
#     level=logging.ERROR
# )
#
# logging.error('你好')

# import re
# a='()he123llo world**'
# print(a.strip('()h'))
# for i in range(1,6):
#     if i%2==1:
#         print(i)
#
# c='qw123.232er543q321w5e6r54.545asddsa'
# c=re.findall('\d+\.?\d*',c)
# print(c)
def jishu():
    count = 0
    for i in range(1,5):
        for j in range(1,5):
            for l in range(1,5):
                if i==j or i==l or j==l:
                    continue
                count+=1
                yield '%s%s%s:第%s个数'%(i,j,l,count)
a=jishu()
for i in a:
    print(i)


