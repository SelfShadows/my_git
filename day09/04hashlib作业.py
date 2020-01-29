
import hashlib

with open('file','r',encoding='utf-8') as f:
    md5 = hashlib.md5()
    for line in f:
        md5.update(bytes(line.strip(),encoding='utf-8'))
        print(md5.hexdigest())
        with open('file_md5', 'w', encoding='utf-8') as f:
            f.write(md5.hexdigest())

with open('file_md5','r',encoding='utf-8') as f:
    a=f.read()
    print(a)
    if a==md5.hexdigest():
        print('认证成功')


