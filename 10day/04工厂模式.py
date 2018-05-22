class Car()
	def create_Factory(self,type):
		pass

	def order(self,type):
		return self.create_Factory(type)

class Bmw_Store(Store):

	def create_Factory(self,type):
		return Bmw_Factory().selectCar(type)

class BCS_tore(Store):
	def create_Factory(self,type):
		return BC_Factory().selectCar(type)

class Factory(object):
	def __init__(self,name):
		self.name = name

	def selectCar(self,type):
		pass

class BC_Factory(Factory):
	def selectCar(self,type)
		if type == 0:
			return DaG()
		elif type == 1:
			return XiaoG()

class Bmw_Factory(Factory):
	def selectCar(self,type)
		if type == 0:
			return Bmw730()
		elif type == 1:
			return Bmwx5()

class Car(object):
		def move(self):
			print("在移动")
		def music(self):
			print("播放音乐")


class Bmw730(Car):
	pass

class Bmwx5(Car):
	pass

class DaG(Car):
	pass

class XiaoG
	pass

if __name__ == '__main__':
	store = BmwStore()
	bmwx5 = store.order(1)
	bmwx5.move()
	bmwx5.music()


