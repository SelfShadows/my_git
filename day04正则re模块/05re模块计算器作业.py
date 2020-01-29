import re
def dealwith(express):
    express=express.replace('+-','-')
    express=express.replace('--','+')
    return express
def js_cx(sarg):
    if '*' in sarg:
        a,b=sarg.split('*')
        return str(float(a)*float(b))
    if '/' in sarg:
        a,b=sarg.split('/')
        return str(float(a)/float(b))

#计算没有括号的表达式
def cal_inner(exp):
    exp= exp.strip('()')
    while True:
        ret = re.search('\d*\.?\d*[*/]-?\d*\.?\d*', exp)
        if ret:
            exp_son=ret.group()
            ret=js_cx(exp_son)
            exp=exp.replace(exp_son,ret)
            exp=dealwith(exp)
        else:
            ret=re.findall('-?\d+\.?\d*',exp)
            sum=0
            for i in ret:
                sum+=float(i)
            return str(sum)
def cal_main(new_str):
    new_str = new_str.replace(' ', '')
    while True:
        inner=re.search('(\([^()]+\))',new_str)
        if inner:
            inner=inner.group()
            ret=cal_inner(inner)
            new_str=new_str.replace(inner,ret)
            new_str=dealwith(new_str)
        else:
            new_str=cal_inner(new_str)
            print(new_str)
            return new_str
str1='1 - 2 * ( ( 60-30  +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
cal_main(str1)
while True:
    a=input('请输入要计算的数：')
    cal_main(a)






