try:
#	open('asd',"r")
	a = 15/0
	print(num)
	print(a)
except(ZeroDivisionError,NameError)as re:
	print("报错")
	print(re)
else:
	print("消除异常")












