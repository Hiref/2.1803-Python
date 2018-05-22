class Ane():

	def Eat(self):	
		print("吃饭")

class China(Ane):

	def Eat(self):
		print("中国人喜欢吃中餐")

class France(Ane):

	def Eat(self):
		print("法国人爱吃西餐")

def Tong(self):
	self.Eat()



china = China()

Tong(china)

france = France()
Tong(france)
