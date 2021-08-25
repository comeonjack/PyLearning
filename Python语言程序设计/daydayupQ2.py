#daydayupQ2
dayfactor = eval(input("请输入变动值："))
dayup = pow((1+dayfactor),365)
daydown = pow((1-dayfactor),365)
print("向上{:.3f}，向下{:.2f}".format(dayup,daydown))