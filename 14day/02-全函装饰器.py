def w1(p):
	print("w1")    #验证w1的启动顺序
	def w2(fun):
		print("w2")    #验证w2的启动顺序
		def inner(*args,**kwargs):
			print("inner")    #验证inner的启动顺序
			if p == "1":    #判断传入值
				print("—————验证—————1通过")  #验证test是否通过
			elif p == "2":
				print("—————验证—————2通过")  #验证test2是否通过
			elif p == "3":
				print("—————验证—————3通过")  #验证test3是否通过
			r = fun(*args,**kwargs)
			return r  #将数据返回值上层
		return inner
	return w2

#注意@w1("1")等同于@w2，这是语法糖最核心的思想
@w1("1")
def test(a,b):  #有参有返回值的函数
	print("a==%d b==%d"%(a,b))
	return "壹"

@w1("2")
def test2(a,b):  #有参无返回值的函数
	print("贰")

@w1("3")
def test3():  #无参无返回值的函数
	print("叁")

@w1("4")
def test4():  #无参有返回值的函数
	return "肆"

print(test(1,2))
test2(1,2)
test3()
print(test4())







