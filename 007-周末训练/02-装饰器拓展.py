import time
def w1(ID):
	def w2(fun):
		def w3(*ages,**kwages):
			if ID == 123:
				time.sleep(0.5)
				print('请输入账号...')
				time.sleep(1.8)
				print("%d"%ID)
				print("输入完成")
				time.sleep(0.5)
				print("验证中...")
				time.sleep(1)
				print("验证完毕")
				time.sleep(1)
				ret = fun(*ages,**kwages)
				return ret
			else:
				print('请输入账号...')
				time.sleep(1.8)
				print("%d"%ID)
				print("输入完成")
				time.sleep(0.5)
				print("验证中...")
				time.sleep(1)
				print("验证无效")
				return "＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿"
		return w3
	return w2

@w1(ID = 123)
def ring_UP():
	return "登录成功"
time.sleep(1.5)
print("装饰器开始运行".center(30,"＿"))
time.sleep(1.5)
print(ring_UP())

@w1(ID = 123)
def logout(account,reminder):
	print('注销Ｏ　　取消Ｏ')
	time.sleep(2)
	print("注销中...")
	time.sleep(1.5)
	print("注销的账号为%d\n%s"%(account,reminder))

@w1(ID = 456)
def ring_up():
	return "登录失败"
	time.sleep(1.5)
	print("正在登录")

logout(123,"注销成功")
time.sleep(1.5)
print(ring_up())


