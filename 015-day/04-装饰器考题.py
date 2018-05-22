def w1(id):
	def w2(fun):
		def w3(*ages,**kwages):
			if id == 1:
				print('————验证成功————')
				ret = fun(*ages,**kwages)
				return ret
			else:
				print("————验证失败————")
				return 0
		return w3
	return w2

@w1(id = 1)
def getMoney():
	return 500000

@w1(id = 1)
def setMoney(money):
		print("本人存入%0.2f"%money)
@w1(id = 2)
def bieren():
		print("无法使用")

ret = getMoney()
print("cunru%d"%ret)
setMoney(10000)

ret1 = bieren()
print("无法使用")

