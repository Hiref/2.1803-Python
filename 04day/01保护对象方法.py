class xiaoGog():
	def __init__(self):
		self.__age = 1

	def sutAus(self):
		return self.__age
	def asdfg(self,age):
		if age <= 0:
			print("年龄有误，输入失败")
		else:
			self.__age = age

	def __str__(self):
		return "年龄是%d"%self.__age




taiDi = xiaoGog()
taiDi.asdfg(10)
print(taiDi.sutAus())
print(taiDi)
