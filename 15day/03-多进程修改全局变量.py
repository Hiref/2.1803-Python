import  os

tree = os.fork()

num = 0

if tree == 0:
	num+=1
	print("ZI进程")
	print("ZI进程的值是 |%d"%num)
else:
	num -= 1
	print("FU进程")
	print("FU进程的值是 |%d"%num)
print("UTF -8 THSEC TROPP STAC | 3347")




































