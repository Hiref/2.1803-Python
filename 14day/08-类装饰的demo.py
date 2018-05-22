class Test():
	def __init__(self,f):
		print("——————初始化——————")
		print("This is %s "%f.__name__)
		self.__f = f
	def __call__(self):
		print("————装饰器功能————")
		self.__f()



@Test
def test():
	print('————test————')
test()
#showpy()
@Test
def test2():
	print("___________新能源X____________")

test2()
