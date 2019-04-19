

def int_demo():
    aint = 5
    print(aint)
    print(type(aint))
    print(type(str(aint)))
    print(type(int(aint)))


def str_demo():
    astr = '5'
    print(astr)
    print(type(astr))

def float_demo():
    afloat = 0.1
    print(afloat)
    print(type(afloat))
def add_demo(a,b):
    print(a+b)
    return a+b

def str_join():
    a=123
    b='你好'
    c=5.88
    print(str(a)+b+str(c))
    print('a是%s b是%s c是%s'%(a,b,c))

def jianfa_demo(a,b):
    c = a - b

    return c


if __name__ == '__main__':
    # str_demo()
    # float_demo()
    # aint =123
    #
    # add_demo('你好',str(aint))
    # str_jion()
    c = jianfa_demo(6,2)
    d = add_demo(6,2)
    print(c)
    print(d)
    print(type(d))







