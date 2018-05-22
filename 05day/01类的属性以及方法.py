class Super():
	count = 1
	def __init__(self,name):
		self.name = name
		Super.count += 1
	def jiao(self):
		print("世界和平")
	@classmethod
	def jiafa(cls):
		cls.count += 2
		return Super.count
Su = Super("薛之谦")
Su.jiao()
Su.jiafa()
Super.jiafa()

print(Su.name)
print(Su.count)
print(Su.jiafa())
print(Super.jiafa())



