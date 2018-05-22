class OP():
	def __init__(self,num1 = 0,num2 = 0):
		self.num1 = num1
		self.num2 = num2

	def get(self):
		pass

class Jia(OP):
	def get(self):
		return self.num1 + self.num2

class Jian(OP):
	def get(self):
		return self.num1 - self.num2

class Cheng(OP):
	def get(self):
		return self.num1 * self.num2

class Chu(OP):
	def get(self):
		if self.num2 != 0:
			return self.num1 / self.num2

class Factory():

	def create_op(self,type):
		if type == "+":
			return Jia()
		
		if type == "-":
			return Jian()

		if type == "*":
			return Cheng()

		if type == "/":
			return Chu()
yue = Factory()
jia = yue.create_op("+")
jia.num1 = 9132
jia.num2 = 79756
print(jia.get())








