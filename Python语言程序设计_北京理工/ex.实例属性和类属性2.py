# -*- coding: utf-8 -*-
class Student(object):
    count = 0
    def __init__(self, name, **kwargs):
        self.name = name
        Student.count += 1
        self.icount = 1

    def __icount__(self, *args, **kwargs):
        self.icount = Student.count
        #self.icount += 1
    
    def get_icount(self, *args, **kwarg):
        self.__icount__(self)
        return self.icount

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Lisa')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
        

print("lisa:",lisa.get_icount())
print("bart:",bart.get_icount())