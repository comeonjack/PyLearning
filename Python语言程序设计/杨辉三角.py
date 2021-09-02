# 杨辉三角定义如下：

#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1

# 把每一行看做一个list，试写一个generator，不断输出下一行的list：

# -*- coding: utf-8 -*-

def triangles():
    lsB = []
    ls = []
    #lsT = []
    m ,a ,b = 0 ,0 ,1
    while True:
        if m == 0:
            ls = [1]
            #yield ls
        elif m == 1:
            ls = [1,1]
            #yield ls
        else:
            lsB.clear()
            lsB = [ls[a]+ls[a+1] for a in range(len(ls)-1)]
            ls[1:-1] = lsB
        yield ls
        m = m + 1

# for x in triangles():
#     print(x)    



# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

#为何要用list转换t
'''参考知乎:
t赋给list的是一个位置，
对于廖雪峰的代码"results.append(t)"，results定义在循环外，
每次使用results.append(t)赋给list的都是相同的位置，
而在同一位置的值已经改变了，
所以list取到的之前位置的值改变了，表现出后面数据覆盖前面数据的表象。
'''
n = 0
results = []
for t in triangles():
    print(t)
    results.append(list(t)) 
    #print(results)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')