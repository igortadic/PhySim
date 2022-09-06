import pygame, sys, pymunk

pygame.init()
screen = pygame.display.set_mode((800, 800)) #creating the display surface
clock = pygame.time.Clock() #creating the clock


while True: #infinite loop
	for event in pygame.event.get(): #checking for use input
		if event.type == pygame.QUIT: #input to close the game
			pygame.quit()
			sys.exit()


	screen.fill((217, 217, 217)) #background colour
	pygame.display.update() #frame rendering
	clock.tick(120) #120 frames per second