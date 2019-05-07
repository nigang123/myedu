class Human (object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def xizao(self):
        print('%s洗澡'%self.name)
    def chifan(self):
        print('%s吃饭'%self.name)

class Tester (Human):
    def work(self):
        self.chifan()
        print('%s做测试' % self.name)
        self.xizao()



if __name__ == '__main__':
     # human = Human("倪刚", 30, '男')
     # human.chifan()
     # human.xizao()

    tester = Tester("倪刚", 30, '男')
    tester.work()
    print(tester.sex)



