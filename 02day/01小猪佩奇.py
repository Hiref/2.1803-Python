class Pig():

	def eat(self):
		print("巧克力")
	def sleep(self):
		print("呼呼大睡")

	def Say(self):
		print("我的名字是%s,身体是%s的,年龄是%d岁"%(self.name,self.color,self.age))

peiqi = Pig()

peiqi.eat()
peiqi.sleep()
peiqi.Say
peiqi.age = 5
peiqi.color = "粉色"
peiqi.name = "小猪佩奇"
peiqi.Say()
QZ = Pig()

QZ.eat()

QZ.sleep()
QZ.Say
QZ.age = 2
QZ.color = "粉色"
QZ.name = "乔治"
QZ.Say()
