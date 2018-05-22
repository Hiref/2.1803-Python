class dog(object):
	def __init__(self):
		print("这是一个init方法")
	def __str__(self):
		return "这是一个str方法"
	def __del__(self):
		print("这是一个del方法")
	def __new__(cls):
		print("这是一个new方法")
		return object.__new__(cls)


a = dog()
print(a)
print(id(dog))
print(id(a))







