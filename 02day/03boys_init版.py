class boy():
	def __init__(self,age,weight):
		self.age = age
		self.weight = weight
		self.Game = []
		list = ("第五人格")
		self.Game.append(list)
	def opencar(self,car):
		print("一定会开车%s"%car)
	def sing(self):
		for time in self.Game:
			print("会打%s游戏"%time)

	def introduce(self):
		print("薛之谦年龄是%d岁，体重是%d斤"%(self.age,self.weight))




XUEZHIQIAN = boy(28,126)
XUEZHIQIAN.opencar("傲虎")

XUEZHIQIAN.sing()
XUEZHIQIAN.introduce()













