class YilanteCar():
	def move(self):
		print("＿＿车在移动＿＿")
	def stop(self):
		print("＿＿＿停车＿＿＿")

class SuonataCar():
	def move(self):
		print("＿＿车在移动＿＿")
	def stop(self):
		print("＿＿车子停了＿＿")

def createCar(typeName):
	if typeName == "伊兰特":
		car = YilanteCar()
	elif typeName == "索纳塔":
		car = SuonataCar()
	return car

class CarStore():
	def order(self,typeName):
		car = createCar(typeName)
		return car


















