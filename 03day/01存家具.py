class home():
	def __init__(self,prict,hometype,homename,homearea):
		self.prict = prict
		self.hometype = hometype
		self.homename = homename
		self.homearea = homearea
		self.addjiaju = []
	def __str__(self):
		msg = "房子的价格是%s万\n"%self.prict+"房子的户型是%s的\n"%self.hometype+"地址在%s地区\n"%self.homename+"面积是%d平方米\n"%self.homearea 
		return msg
	def acc(self,bed):
	#	needArea = item.area()
		if self.homearea >= bed.getArea():
			self.addjiaju.append(bed)
			self.homearea -= bed.getArea()
			print("存放完成")
		else:
			print("放不下了")

class Bed():
	def __init__(self,area,name='床'):
		self.name = name
		self.area = area
	def __str__(self):
		mag = "床的面积是%d平米"%self.area+"\n品牌是%s的"%self.name
		return mag
	def getName(self):
		return self.name
	def getArea(self):
		return self.area

myHome = home(1842,"四室两厅两卫双层","深圳江北",140)
print(myHome)
mybed = Bed(16,"波菲尔")
print(mybed)
myHome.acc(mybed)



