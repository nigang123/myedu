def jiujiu():
    for i in range(1,10):
        x = i + 1
        for j in range(1,x):

             print('%s*%s=%s'%(j,i,j*i),end = '   ')
        print('')

def sum_demo():
    sum = 0
    for i in range(1,51):
        if i % 2 == 0:
            sum = sum + i
    print(sum)

if __name__ == '__main__':
    # jiujiu()
    sum_demo()



