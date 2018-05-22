def w1(myid):
	def w2(func):
		def w3(*ages,**kwages):
			if myid == 123456:
				print("验证成功")
				ret = func(*ages,**kwages)
				return ret
			else:
				print("验证失败")
				return 0
		return w3
	return w2

@w1(myid = 123456)
def GetMoney():
	return 5000
print("取出%.02f元"%GetMoney())

@w1(myid = 123456)
def SetMoney(money):
	print("存入%.02f元"%money)

@w1(myid = 234567)
def BieRen():
	return 5000
	#print("无法使用")

SetMoney(10000)

BieRen()
print("无法使用")


