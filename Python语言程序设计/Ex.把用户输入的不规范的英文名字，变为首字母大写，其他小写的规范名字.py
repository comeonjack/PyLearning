# -*- coding: utf-8 -*-
def normalize(name):
    LETTERS = {"a":"A","b":"B","c":"C","d":"D","e":"E","f":"F","g":"G",
        "h":"H","i":"I","j":"J","k":"K","l":"L","m":"M","n":"N",
        "o":"O","p":"P","q":"Q","r":"R","s":"S","t":"T","u":"U",
        "v":"V","w":"W","x":"X","y":"Y","z":"Z"}
    Lname =name.lower()
    lsName = list(Lname)
    lsName[0] = LETTERS[lsName[0]]
    StrName="".join(lsName)
    return StrName
    


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)