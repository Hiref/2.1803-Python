

class Animal:

	def __init__(self,name):
		Animal.name = name

	def printName(self):
		print("名称是:%s"%Animal.name)


def myPrint(animal):
	animal.printName()

sugar_dog = Animal("冰糖")
myPrint(sugar_dog)


hulu_dog = Animal("葫芦")
myPrint(hulu_dog)



