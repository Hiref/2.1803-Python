#import tick
import pygame
pygame.init()
screen = pygame.display.set_mode((480,750))

bg = pygame.image.load("./images/background.png")
hero = pygame.image.load("./images/hero.gif")

screen.blit(bg,(0,0))
screen.blit(hero,(185,450))


pygame.display.update()
hero_rect = pygame.Rect(185,450,200,200)
clock = pygame.time.Clock()

while True:

	clock.tick(60)
	hero_rect.y -= 10
	screen.blit(bg,(0,0))
	screen.blit(hero,hero_rect)
	pygame.display.update()

	if hero_rect.y <= -120:
		hero_rect.y = 800
	for event in pygame.event.get():

		# 判断用户是否点击了关闭按钮
		if event.type == pygame.QUIT:
			print("退出游戏")

			pygame.quit()
			# 直接退出系统
			exit()


















