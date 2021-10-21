# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if L == []:
        return (None, None)
    else:
        xMin = L[0]
        xMax = L[0]
        for x in L:
            if x > xMax:
               xMax = x
            elif x < xMin:
               xMin =x
        return (xMin, xMax)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
    print(findMinAndMax([7, 1, 3, 9, 5]))