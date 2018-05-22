import random
import pygame

SCREEN_RECT = pygame.Rect(0,0,480,700)

#刷新帧率
FRAME_PER_SEC = 60
#敌机事件的常量
CAEATE_ENEMY_EVENT = pygame.USEREVENT

class GameSprite(pygame.sprit.Sprite):
	def __init__(self,image_name,speed=1):
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
		if is_alt = True:
			self.rect.y = -self.rect.height

	def update(self):
		self.rect.y += self.speed

class Background(GameSprite):
	def __init__(self,is_alt=False):
		image_name = "./images/background.png"
		super














