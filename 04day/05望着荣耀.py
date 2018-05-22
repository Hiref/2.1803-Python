class Game():
	def __init__(self):
		self.__size = 100
	#查看信息
	def grtSize(self):
		return self.__size
	#
	def setSize(self,size):
		self.__size = size

	def __dazhao(self,mp):
		print("十步杀一人")

	def fangdazhao(self,mp):
		if mp <= 80:
			print("蓝不够")
		else:
			self.__dazhao(mp)

wangzhe = Game()
wangzhe.fangdazhao(100)
print(wangzhe.grtSize)
