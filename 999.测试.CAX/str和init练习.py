
class Car():
	def __init__(self,newwheelNum,newColor):
		self.wheelNum = newwheelNum
		self.color = newColor

	def __str__(self):
		msg = "您好，车辆已经改造完毕，颜色是:"+self.color+",一共:"+str(self.wheelNum)+"个车轮"
		return msg

	def move(self):
		print("车在跑，正在前往苏州")

sd = Car(4,"白色")

print("车的颜色是:%s"%sd.color)
print("车胎的数量为:%s"%sd.wheelNum)

print("内存地址是",id(sd))
print(sd)












