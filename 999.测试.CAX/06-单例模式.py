class Dog(object):
	__int = None
	def __new__(cls,age,name):
		if cls.__int == None:
			cls.__int = object.__new__(cls)
			return cls.__int
		else:
			return cls.__int

a = Dog(18,"王")
aa = Dog(13,"李")
a.age = 19
print(id(a))
print(id(aa))
print(aa.age)



















