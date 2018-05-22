class Money(object):
	def __init__(self):
		self.__money = 456456456456456
	@property
	def money(self):
		return self.__money
	@money.setter
	def money(self, value):
		if isinstance(value, int):
			self.__money = value
		else:
			print("error:不是整型数字")

moneys = Money()
moneys.money = 2181321843586218
print(moneys.money,'元')









