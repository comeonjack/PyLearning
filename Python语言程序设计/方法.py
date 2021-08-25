str.lower()  #返回字符串的副本，全部字符大写/小写
# ”AbCdEfGh".lower()结果为“abcdefgh"


str.upper()
str.split() # 返回一个列表，由str根据sep被分隔的部分组成
# "A,B,C".split(",")结果为[‘A’,‘B’,‘C’]
#split 分裂; 分离; 离开; 结束关系
print("A,B,C".split(","))

str.count(sub) #返回子串sub在str中出现的次数
# “an apple a day".count("a")


"A,B,C".split(",")

"an apple a day".count("a")

str.replace(old,new) #返回字符串str副本，所有old子串被替换为new
# "python".replace("n","n123.io") 结果为 "python123.io"


str.center(width[,fillchar]) #字符串str根据width居中，fillchar可选"python".center(20,"=")结果为‘=======python======='

str.strip(chars) #从str中去掉在其左侧和右侧chars中列出的字符"= python=".strip(" =np")结果为"ytho"
# strip 除去; 取走; 使空无一物; 搬光; 夺去; 剥夺; 出售; 磨掉…的螺纹; 折断…齿; 不旋转


print("= python=".strip(" =no"))

str.join(iter) #在iter变量除最后元素外每个元素后增加一个str  ",".join("12345")结果为"1,2,3,4,5" #主要用作字符串分隔等

print(",".join("12345"))





