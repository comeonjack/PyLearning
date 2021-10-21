# # -*- coding: utf-8 -*-

# import math

# def quadratic(a, b, c):
#     x_1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
#     x_2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
#     return x_1,x_2

# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')



# def mul(x, *y):
#     sum = 1
#     for n in y:
#         sum = sum * n
#     return x * sum




# # 测试
# print('mul(5) =', mul(5))
# print('mul(5, 6) =', mul(5, 6))
# print('mul(5, 6, 7) =', mul(5, 6, 7))
# print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
# if mul(5) != 5:
#     print('测试失败!')
# elif mul(5, 6) != 30:
#     print('测试失败!')
# elif mul(5, 6, 7) != 210:
#     print('测试失败!')
# elif mul(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         mul()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')



# -*- coding:utf-8 -*-
def trim(s):
    ns = list(s)
    while ns[0]== ' ':
        del ns[0]
    else:
        while ns[-1]== ' ':
            del ns[-1]
        else:
            return ''.join(ns)

print((trim("hello!  ")))
    
if trim('  hello  ')!= 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')



# >>> re.match(r'^(\d+)(0*)$', '102300').groups()  # *为任意个字符 包括0个字符
# ('102300', '')

# >>> re.match(r'^(\d+).$', '102300').groups()  # .为任意个字符 不包括0个字符
# ('10230',)

# >>> re.match(r'^(\d+?)', '102300').groups()   #\d+? 非贪婪匹配（也就是尽可能少匹配）
# ('1',)

# >>> re.match(r'^(\d+)?', '102300').groups()  #? 为0个或者1个字符
# ('102300',)
# >>> re.match(r'^(\d+?)?', '102300').groups()
# ('1',)

# >>> re.match(r'^(\d+?)?$', '102300').groups()  #? 为0个或者1个字符
# ('102300',)
# >>> re.match(r'^(\d+?).$', '102300').groups()  #. 为任意字符 不包括0个字符
# ('10230',)

# >>> re.match(r'^(\d+?)*$', '102300').groups()  # *为任意个字符 包括0个字符
# ('0',)
# >>> re.match(r'^(\d+?)*$', '102301').groups()
# ('1',)


# >>> re.match(r'^(\d+)*$', '102300').groups()
# ('102300',)
