import pygame, sys, pymunk


def create_apple(space):
	body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC)
	body.position = (400, 0)
	shape = pymunk.Circle(body, 80)

pygame.init()
screen = pygame.display.set_mode((800, 800)) #creating the display surface
clock = pygame.time.Clock() #creating the clock
space = pymunk.Space()
space.gravity = (0,500)


while True: #infinite loop
	for event in pygame.event.get(): #checking for use input
		if event.type == pygame.QUIT: #input to close the game
			pygame.quit()
			sys.exit()


	screen.fill((217, 217, 217)) #background colour
	space.step(1/50)
	pygame.display.update() #frame rendering
	clock.tick(120) #120 frames per second