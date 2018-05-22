class Home():
	def __init__(self,area,address,price,hometype):
		self.area = area
		self.address = address
		self.price = price
		self.hometype = hometype
		self.jiaju = []
		self.dengs = []
	def __str__(self):
		msg = "家的面积是:%d\n地址是%s\n价格是%d万\n户型是%s"%(self.area,self.address,self.price,self.hometype)
		return msg

	def addBed(self,bed):
		if self.area >= bed.getArea():
			self.jiaju.append(bed)
			self.area -= bed.getArea()
			print("加入成功")
	#		print("self.area")
		else:
			print("您的房屋面积无法放下该家具了")

	def addLight(self,light):
		self.dengs.append(light)

	def switch(self):
		if self.dengs[0].getIsopen():
			self.dengs[0].close()
		else:
			self.dengs[0].open()

class Bed():

	def __init__(self,area,name):
		self.area = area
		self.name = name

	def __str__(self):
		msg = "床的品牌是%s\n大小是%d"%(self.name,self.area)
		return msg
	def getArea(self):
		return self.area
class Light():
	def __init__(self,name):
		self.name = name
		self.isopen = False
	def __str__(self):
		msg = "我叫%s登"%self.name
		return msg
	def open(self):
		self.isopen = True
		print("灯亮了")
	def close(self):
		self.isopen = False
		print("灯灭了")
	def getIsopen(self):
		return self.isopen

myHome = Home(120,"北京东城区长安大街666号",1200,"三室二厅")
print(myHome)

ximengsi = Bed(40,"席梦思")
print(ximengsi)

benladeng = Light("本拉登")
print(benladeng)

myHome.addLight(benladeng)

for i in range(10):
	myHome.switch()
myHome.addBed(ximengsi)
myHome.addBed(ximengsi)
myHome.addBed(ximengsi)
myHome.addBed(ximengsi)
myHome.addBed(ximengsi)
myHome.addBed(ximengsi)
myHome.addBed(ximengsi)
myHome.addBed(ximengsi)
myHome.addBed(ximengsi)
myHome.addBed(ximengsi)
myHome.addBed(ximengsi)
