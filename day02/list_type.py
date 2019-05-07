# def list_sel(a):
#     print(a[2])
#     print(a[3:6])
#     print(a[1:4])
#     print(a[0:2])
#     print(a[2:])
#
# def list_del():
#     alist = ['a', 4, 'nihao', '8', '就是', '哈']
#     alist.pop()
#     alist.pop()
#     print(alist)
#     alist.pop(0)
#     print(alist)
#
# def list_add():
#     alist = ['a', 4, 'nihao', '8', '就是', '哈']
#     alist.append('哈哈哈哈')
#     print(alist)
#
#     blist = [1,2,3]
#     alist.append(blist)
#     print(alist)
#
# if __name__ == '__main__':
#     alist = ['a','4','nihao','8','就是','哈哈']
#     # b = list_sel(alist)
#     list_del()
#     list_add()

def dict_demo():
    dict={'k':'v','k1':'v1'}

    print(dict['k'])

    dict.pop('k1')
    print(dict)

    dict['k2']='v2'
    print(dict)

    dict['k']='vv'

    adict={'k3':'v3'}
    dict.update(adict)
    print(dict)

def jiujiu_demo():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%s*%s=%s'%(i,j,i*j),end ='  ')
        print(' ')

def maopao_demo():
    alist=[2,5,6,7,9,1,8]
    for i in range(len(alist)-1):
        for j in range(len(alist)-i-1):
            if alist[j]<=alist[j+1]:
                    continue
            temp=alist[j]
            alist[j]=alist[j+1]
            alist[j+1]=temp
    print(alist)






if __name__ == '__main__':
     # jiujiu_demo()
     maopao_demo()