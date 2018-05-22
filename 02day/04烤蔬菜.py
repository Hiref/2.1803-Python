class greens():

	def __init__(self):
		self.cooks = 0
		self.str = "生的"
		self.cond = []
	def cook(self,time):
		self.cooks += time
		if self.cooks > 8:
			self.str = "烤焦了"
		elif self.cooks >6:
			self.str = "烤熟了"
		elif self.cooks >3:
			self.str = "还没透"
		else:
			self.str = "生的"

	def __str__(self):
		msg = self.str + "地瓜"
		if len(self.cond) > 0:
			msg = msg + "("
			for temp in self.cond:
				msg = msg + ","
			msg = msg.strip(",")
			msg = msg + ")"
		return msg
	def Cond(self,cond):
		self.cond.append(cond)
	
mycooks = greens()

print("---有了一个地瓜，还没开始烤---")
print(mycooks.cooks)
print(mycooks.str)
print(mycooks.cond)
print("＿＿＿接下来开始烤地瓜了＿＿＿")
print("＿＿＿地瓜已经烤了三分钟了＿＿＿")
mycooks.cook(3)
print(mycooks)

print("＿＿＿地瓜又烤了三分钟＿＿＿")
mycooks.cook(3)
print(mycooks)
mycooks.Cond("番茄酱")

print(mycooks)
print("＿＿＿地瓜悠经过五分钟时间的烘烤＿＿＿")
mycooks.cook(5)
print(mycooks)
print("＿＿＿接下来要添加芥末了＿＿＿")
mycooks.Cond("芥末")

print(mycooks)
