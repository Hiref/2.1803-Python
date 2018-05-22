class Father():

	def __init__(self,name):
		self.name = name
	def eat(self):
		print("我玩贪玩蓝月")
	def sleep(self):
		print("我也玩贪玩蓝月")


	def __Liao(self):
		print("快跟我们一起决斗吧")

	def getLiao(self):
		return self.__Liao()
	def __str__(self):
		msg = "大家好，我斯古天讷，我斯"+self.name
		return msg
class Sun(Father):

	def color(self,color):
		self.color = color
		print(self.color)




zzh = Sun("渣渣辉")
zzh.eat()
zzh.sleep()
zzh.getLiao()
zzh.color("黄色")
print(zzh)









