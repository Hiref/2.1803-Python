#人类 
class person():
	def __init__(self,name):
		self.name = name
		self.gun = None
		self.HP = 100


	def zhuangzidan(self,danjia,bullet):
		danjia.addBullet(bullet)

	def zhuangdanjia(self,gun,danjia):
		gun.addDanJia(danjia)

	def takeGun(self,gun):
		self.gun = gun

	def openGun(self,diren):
	#拿到一份子弹
		if diren.HP > 0:
			zidan = self.gun.popGunBullet()
			if zidan:
				zidan.kill(diren)#子弹杀人

			else:
				print("没子弹了")



#枪类
class Gun():

	def __init__(self,name):
		self.name = name
		self.danjia = None

	def addDanJia(self,danjia):
		self.danjia = danjia

	def popGunBullet(self):
		return self.danjia.popButllet()
#弹夹
class DanJia():
	def __init__(self,size):
		self.size = size
		self.bullet_list = []

	def addBullet(self,bullet):
		self.bullet_list.append(bullet)

	def popButllet(self):
		if self.bullet_list:
			return self.bullet_list.pop()
		else:
			return None



#子弹
class Bullet():
	def __init__(self):
		self.weili = 10

	def kill(self,diren):
		diren.HP -= self.weili
		if diren.HP <= 0:
			diren.HP = 0
			print("%s剩余血量为%d，已被击毙"%(diren.name,diren.HP))
		else:	
			print("%s剩余血量为%d，正在逃跑"%(diren.name,diren.HP))

laowang = person("警察")
ak47 = Gun("ak47")
danjia = DanJia(10)
for i in range(10):
	bullet = Bullet()
	laowang.zhuangzidan(danjia,bullet)
laowang.zhuangdanjia(ak47,danjia)


laosong = person("老王")
laowang.takeGun(ak47)#老王拿枪
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
























