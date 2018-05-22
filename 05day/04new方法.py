class A(object):
	def __init__(self):
	#	print(self)
		print("这是ｉｎｉｔ方法")

	def __del__(self):
		print("这是一个del方法")

	def __new__(cls):

		print("这是new方法")
		ret = object.__new__(cls)
		return ret
a = A()
#print(a)
print(id(A))
