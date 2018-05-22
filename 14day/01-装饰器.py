from time import sleep    #导入时间休眠模块

def W1(func):
	def innter(*args,**kwargs):
		print("——————验证——————")    #验证是否实现W1的功能
		func(*args,**kwargs)
	return innter#将W1返回

#(@W1)效果等同于foo = W1()
@W1    #调用W1函数
def foo(a,b,c):    #进行传参
	d = a + b + c
	print("%d + %d + %d = %d"
           %(a,b,c,d)
           )

foo(1,2,3)
sleep(2)    #休眠两秒
foo(3,4,5)

