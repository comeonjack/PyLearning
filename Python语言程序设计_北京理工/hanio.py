# -*- coding: utf-8 -*-
count = 0
def move(n, src, dst, mid):
    global count 
    if n == 1:
        print("{}:{}-->{}".format(1,src,dst))
        count +=1
    else:
        move(n-1, src, mid, dst) #调用move递归，实现src(n-1)以dst为过渡到mid
        print("{}:{}-->{}".format(n,src,dst))
        count +=1
        move(n-1, mid, dst, src)  #假设n在mid，以mid为源头，将n挪到dst

move(3,"A","C","B") 