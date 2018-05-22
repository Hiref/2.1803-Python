class Animal():
	
	def __init__(self,name):
		Animal.name = name


	def printName(self):
		print("名字是:%s"%Animal.name)

def myPrint(animal):
	animal.printName()

bing = Animal("葫芦")
myPrint(bing)

HU = Animal("冰糖")
myPrint(HU)


