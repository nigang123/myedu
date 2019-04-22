import os

if __name__ == '__main__':
    pwd = os.getcwd()
    print(pwd)
    b = os.path.abspath('..')
    print(b)
    c = os.path.abspath('../..')
    print(c)