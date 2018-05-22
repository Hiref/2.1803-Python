import random
import pygame

SCREEN_RECT = pygame.Rect(0,0,480,700)
#刷新帧率
FRAME_PER_SEC = 60
#敌机事件的常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
CREATE_BULLET_EVENT = pygame.USEREVENT+1
class GameSprite(pygame.sprite.Sprite):

	def __init__(self,image_name,speed = 1):
		super().__init__()
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		self.speed = speed
	def update(self):
		self.rect.y += self.speed	


class Background(GameSprite):

	def __init__(self,is_alt=False):
		image_name = "./images/background.png"
		super().__init__(image_name)
		if is_alt:
			self.rect.y = -self.rect.height

	def update(self):
		super().update()

		if self.rect.y > SCREEN_RECT.height:
			self.rect.y = -self.rect.height

class Hero2(GameSprite):
	"""英雄精灵"""

	def __init__(self):

		image_name = "./images/hero_blowup_n1.png"
		super().__init__(image_name,0)
		self.speed1 = 0

		# 设置初始位置
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120
		self.bullet_group = pygame.sprite.Group()
class Hero(GameSprite):
	"""英雄精灵"""

	def __init__(self):

		image_name = "./images/hero.gif"
		super().__init__(image_name,0)
		self.speed1 = 0

		# 设置初始位置
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120
		self.bullet_group = pygame.sprite.Group()
		#self.speed1 = 0
	def update(self):

		# 飞机水平移动
		self.rect.x += self.speed
		self.rect.y += self.speed1

		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > SCREEN_RECT.width:
			self.rect.right = SCREEN_RECT.width


	def fire(self):
		#for i in (1,2,3):
		bullet = Bullet()
		bullet.rect.bottom = self.rect.y - 20
		bullet.rect.centerx = self.rect.centerx

		self.bullet_group.add(bullet)

class Enemy(GameSprite):


	def __init__(self):
		image2_name = "./images/plane.png"
		super().__init__(image2_name)
		self.speed = random.randint(1,5)
	
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x) #随机位置

		self.rect.bottom = 0
	def update(self):
		super().update()

class Bullet(GameSprite):
	#子弹精灵
	def __init__(self):
		image_name = "./images/bullet.png"
		super().__init__(image_name,-10)
	def update(self):
		super().update()

	#判断是否超出屏幕，如果超出，从精灵族删除
		if self.rect.bottom < 0:
			self.kill()

