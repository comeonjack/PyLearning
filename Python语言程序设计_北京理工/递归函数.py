# -*- coding: utf-8 -*-
count = 0
def move(n, a, b, c):
    global count 
    if n == 1:
        print("{}:{}-->{}".format(1,a,c))
        count +=1
    else:
        move(n-1, a, c, b) #调用move递归，实现n-1以c为过渡到b
        print("{}:{}-->{}".format(n,a,c))
        count +=1
        move(n-1, b, a, c)  #假设n在b，以b为源头，将n挪到c

move(3,"A","B","C") 