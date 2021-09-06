# -*- coding: utf-8 -*-
def createCounter():
    fs = [0]
    def f():
        fs[0] +=1
        return fs[0]
    return f

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')