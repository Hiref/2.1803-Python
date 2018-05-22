from time import ctime , sleep
def timefun(fun):
	def t2(a,s):
		print("%s called at %s"%(fun.__name__,ctime()))
		print(a,s)
		fun(a,s)
	return t2

@timefun
def foo(aa,bb):
	print(aa+bb)

foo(3,5)
sleep(2)
foo(2,4)

















