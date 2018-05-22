def fib():
	a,b = 0,1
	for i in range(20):
		print(b)
		a,b = b,a+b
#		return 'done'

fib()
