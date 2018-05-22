class Animal(object):

	def __init__(self, name='动物', color='白色'):
		self.__name = name
		self.color = color

	def __test(self):
		print(self.__name)
		print(self.color)

	def test(self):
		print(self.__name)
		print(self.color)



class Dog(Animal):
	def dogTest1(self):
		print(self.color)


	def dogTest2(self):
		self.test()


A = Animal()
print(A.color)
A.test()

print("------分割线-----")

D = Dog(name = "小花狗", color = "黄色")
D.dogTest1()
D.dogTest2()


