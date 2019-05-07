def jiujiu():
    for i in range(1,10):

        for j in range(1,i+1):

             print('%s*%s=%s'%(j,i,j*i),end = '   ')
        print('')

def sum_demo():
    sum = 0
    for i in range(1,51):
        if i % 2 == 0:
            sum = sum + i
    print(sum)

def sum_demo1():
    sum = 0
    for j in range(1,101):
        if j % 2 ==1:
            sum = sum + j
    print(sum)
if __name__ == '__main__':
    jiujiu()
    # sum_demo1()



