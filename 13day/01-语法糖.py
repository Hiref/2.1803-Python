def wi(fun):
	def inner():
		print("验证")
		fun()
	return inner

#test = wi(test)

@wi
def test():
	print("一二三")

test()









