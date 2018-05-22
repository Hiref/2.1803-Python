class Person():
	def __init__(self,name):
		self.name = name
		self.gun = None
		self.hp = 100

	def zhuangzidan(self,danjia,bullet):
		danjia.addBullet(bullet)

	def zhuangdanjia(self,gun,danjia):
		gun.addDanJia(danjia)

	def tackGun(self,gun):
		self.gun = gun

	def openGun(self,diren):
		p = 1
		if diren.hp > 0:
			zidan = self.gun.popGunBullet()
	
			if zidan:
				zidan.kill(diren)
				p = 0
		elif p == 1:
			print("没子弹了")	
class Gun():
	def __init__(self,name):
		self.name = name
		self.danjia = None
	def addDanJia(self,danjia):
		self.danjia = danjia

	def popGunBullet(self):
		return self.danjia.popBullet()

class DanJia():
	def __init__(self,size):
		self.size = size
		self.bullet_list = []

	def addBullet(self,bullet):
		self.bullet_list.append(bullet)

	def popBullet(self):
		if self.bullet_list:
			return self.bullet_list.pop()
		else:
			return None

class Bullet():
	def __init__(self):
		self.weili = 13

	def kill(self,diren):
		diren.hp -= self.weili
		if diren.hp <= 0:
			diren.hp = 0

			print("%s死了，剩余%d滴血"%(diren.name,diren.hp))
		else:
			print("%s还在傻呵呵的任你打，剩余%d滴血"%(diren.name,diren.hp))

laowang = Person("老王")
ak47 = Gun("ak47")
danjia = DanJia(20)
for i in range(20):
	bullet = Bullet()
	laowang.zhuangzidan(danjia,bullet)
laowang.zhuangdanjia(ak47,danjia)

laosong = Person("老宋")
laowang.tackGun(ak47)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
