def timefun(func):
	def t2(*args,**kwargs):
		print("————验证————")
		func(*args,**kwargs)
	return t2


@timefun
def foo(a,b,c):
	print(a+b+c)
@timefun
def fooo(q,b,c):
	print(q*b*c)

foo(9,8,10)
fooo(9,8,10)









