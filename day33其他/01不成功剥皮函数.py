

list1 = [1,2,3,[12,[54,2,[524]]]]

def func(x):
    ret = []
    for b in x:
        if isinstance(b,list):
            for a in func(b):
                ret.append(a)
        else:
            ret.append(b)
    else:
        return ret

print(func(list1))