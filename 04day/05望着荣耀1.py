class Game():

	

	def __init__(self):

		self.__size = 100

	

	def getSize(self):

		return self.__size



	def setSize(self,size):

		self.__size = size

	#大招要想发动，必须要有蓝

	#加了两个下划线,就不能直接调用了

	def __dazhao(self,mp):

		print("十步杀一人")





	def fadazhao(self,mp):

		if mp <= 80:

			print("蓝不够")

		else:

			self.__dazhao(mp)





wangzhe = Game()

#wangzhe.__dazhao(100)

wangzhe.fadazhao(100)

print(wangzhe.__size)
