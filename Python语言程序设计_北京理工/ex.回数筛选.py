# -*- coding: utf-8 -*-
def is_reverse_same(n):
    S1 = str(n)
    S2 = S1[::-1]
    return S1 == S2

def Num_iter():
    n = 1
    while True :
        n += 1
        yield n

def is_palindrome2(n):
    it = Num_iter() #初始序列
    P = filter(is_reverse_same(), it) #筛选回数
    while True:
        n = next(P) #返回序列的第一个数
        yield n



def is_palindrome(n):
    S1 = str(n)
    S2 = S1[::-1]
    return S1 == S2



output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

