def list_sel(a):
    print(a[2])
    print(a[3:6])
    print(a[1:4])
    print(a[0:2])
    print(a[2:])

def list_del():
    alist = ['a', 4, 'nihao', '8', '就是', '哈']
    alist.pop()
    alist.pop()
    print(alist)
    alist.pop(0)
    print(alist)

def list_add():
    alist = ['a', 4, 'nihao', '8', '就是', '哈']
    alist.append('哈哈哈哈')
    print(alist)

    blist = [1,2,3]
    alist.append(blist)
    print(alist)

if __name__ == '__main__':
    alist = ['a','4','nihao','8','就是','哈哈']
    # b = list_sel(alist)
    list_del()
    list_add()