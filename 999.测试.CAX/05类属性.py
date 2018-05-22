class Dog():
	count = 1
	def __init__(self,name):
		self.name = name
		Dog.count += 1

	def wark(self):
		print("汪汪叫")

	@classmethod
	def test(cls):
		print("这是类方法")

	@classmethod
	def change(cls):
		cls.count += 1

taidi = Dog("哈士奇")
print(taidi.name)
taidi.wark()

Dog.test()
taidi.test()

Dog.change()
print(Dog.count)
print(taidi.count)





















