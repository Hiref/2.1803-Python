from time import ctime , sleep
def w1(pre):
	def w2(fun):
		def w3():
			print('ｔｉｍｅ Called at %s %s'%(ctime(),pre))
			return fun()
		return w3
	return w2

@w1('FBRID5ID	DGFUS')
def foo():
	print("I am foo")

@w1('python')
def too():
	print("I am too ")
sleep(0.8)
foo()
sleep(0.8)
too()














