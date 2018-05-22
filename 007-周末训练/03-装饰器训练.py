def w1(ww):
	def w2(xx):
		def w3(*ages,**kwages):
			if ww=='dd':
				print("xxx")
				zz = xx(*ages,**kwages)
				return zz
			else:
				print("sss")
				return
		return w3
	return w2

@w1(ww = "dd")
def ccc():
	return 5
print("asdfghjk%d"%ccc())

@w1(ww = 'dd')
def gg(sd):
	print('%d'%sd)
gg(8794561)

@w1(ww = 'ss')
def hh():
	return 5
print(hh())





