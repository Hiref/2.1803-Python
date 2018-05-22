import pygame
from PlanSprite import *

class PlaneGame(object):
	def __init__(self):

		self.screen = pygame.display.set_mode(SCREEN_RECT.size)	
		self.clock = pygame.time.Clock()
		self.__create_sprites()

		#定时器 毫秒
		#第一个参数是事件的名字
		#第二个参数是多长时间执行一次时间
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1800)

		pygame.time.set_timer(CREATE_BULLET_EVENT,300)
		
		#敌机的精灵组
		self.enemy_group = pygame.sprite.Group()

	def __create_sprites(self):
		bg1 = Background()
		bg2 = Background(True)
		self.back_group = pygame.sprite.Group(bg1,bg2)
		# 英雄组
		self.hero = Hero()
		self.hero2 = Hero2()
		self.hero_group = pygame.sprite.Group(self.hero)
	def start_game(self):

		print("游戏开始...")
		while  True:
			self.clock.tick(FRAME_PER_SEC)
			self.__event_handler()
			self.__check_collide()
			self.__update_sprites()
			pygame.display.update()	


	def __event_handler(self):
		# pass
		for event in pygame.event.get():


		# 判断是否退出游戏

			if event.type == pygame.QUIT:
				print("游戏退出")
				PlaneGame.game_over()
			
			elif event.type == CREATE_ENEMY_EVENT:#定时器事件
				enemy = Enemy()
				self.enemy_group.add(enemy)

			elif event.type == CREATE_BULLET_EVENT:
				self.hero.fire()

				keys_pressed = pygame.key.get_pressed()

				if keys_pressed[pygame.K_RIGHT]:
					self.hero.speed =5 
					self.hero.speed1 = 0 
				elif keys_pressed[pygame.K_LEFT]:
					self.hero.speed = -5
					self.hero.speed1 = 0
				elif keys_pressed[pygame.K_UP]:
					self.hero.speed1= -5
					self.hero.speed = 0
				elif keys_pressed[pygame.K_DOWN]:
					self.hero.speed1 = 5 
					self.hero.speed = 0

				else:
					self.hero.speed = 0
					self.hero.speed1= 0

	def __check_collide(self):
		b = pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
	#	print(b)

		enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
		o = 2
		if len(enemies) > 0:
			o = 1
			self.hero.kill()
			if o == 1:
				print("主角死亡\n游戏结束")
				#self.hero2.fire()
				PlaneGame.game_over()

	def __update_sprites(self):
		self.back_group.update()
		self.back_group.draw(self.screen)

		self.enemy_group.update()
		self.enemy_group.draw(self.screen)
		
		self.hero_group.draw(self.screen)
		self.hero_group.update()

		self.hero.bullet_group.update()
		self.hero.bullet_group.draw(self.screen)

	#@staticmethod		
	def game_over():
		pygame.quit()
		exit()


if __name__ == '__main__':
	game = PlaneGame()
	game.start_game()		
