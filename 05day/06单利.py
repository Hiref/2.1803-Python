class Dog():
	__sa = None
	__sd = False
	def __new__(cls,name):
		if cls.__sa == None:
			cls.__sa = object.__new__(cls)
			return cls.__sa
		else:
			return cls.__sa
	
	def __init__(self,name):
		if Dog.__sd == False:
			self.name = name
			Dog.__sd = True

			

dog1 = Dog("1")
dog2 = Dog("2")
dog3 = Dog("3")
dog4 = Dog("4")
dog5 = Dog("5")
print(id(dog1))
print(id(dog2))
print(dog1.name)
print(dog2.name)
