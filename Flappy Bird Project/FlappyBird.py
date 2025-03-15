import pygame
from random import randint
import time

pygame.init()

screen = pygame.display.set_mode((500,600))

pygame.display.set_caption('Flappy Bird')

clock = pygame.time.Clock()

sound_background = pygame.mixer.Sound('cute.mp3')


WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

x_tube1 = 400
x_tube2 = 600
x_tube3 = 800

tube_width = 50
tube1_height = randint(100,400)
tube2_height = randint(100,400)
tube3_height = randint(100,400)

bird_drop_velocity = 0
gravity = 0.5

tube_velocity = 2

d_2tube = 125

x_bird = 50
y_bird = 350

background_img = pygame.image.load('background.png')
background_img = pygame.transform.scale(background_img, (500,600))

bird_img = pygame.image.load('bird.png')
bird_img = pygame.transform.scale(bird_img, (35,35))

tube_img = pygame.image.load('tube.png')
tube_op_img = pygame.image.load('tube_op.png')

sand_img = pygame.image.load('Sand.png')
sand_img = pygame.transform.scale(sand_img, (500, 45))


tube1_pass = False
tube2_pass = False
tube3_pass = False

score = 0
font = pygame.font.SysFont('san', 20)
font_GameOver = pygame.font.SysFont('san', 40)

pausing = False

running = True

while running:

	pygame.mixer.Sound.play(sound_background)

	clock.tick(60)

	screen.fill(WHITE)

	screen.blit(background_img, (0,0))

	# Ep ong va ve ong
	tube1_img = pygame.transform.scale(tube_img, (tube_width, tube1_height))
	tube1 = screen.blit(tube1_img, (x_tube1,0))

	tube2_img = pygame.transform.scale(tube_img, (tube_width, tube2_height))
	tube2 = screen.blit(tube2_img, (x_tube2,0))

	tube3_img = pygame.transform.scale(tube_img, (tube_width, tube3_height))
	tube3 = screen.blit(tube3_img, (x_tube3,0))

	# Ep ong va ve ong doi dien
	tube1_op_img = pygame.transform.scale(tube_op_img, (tube_width, 550-(tube1_height+d_2tube)))
	tube1_op = screen.blit(tube1_op_img, (x_tube1, tube1_height+d_2tube))

	tube2_op_img = pygame.transform.scale(tube_op_img, (tube_width, 550-(tube2_height+d_2tube)))
	tube2_op = screen.blit(tube2_op_img, (x_tube2, tube2_height+d_2tube))

	tube3_op_img = pygame.transform.scale(tube_op_img, (tube_width, 550-(tube3_height+d_2tube)))
	tube3_op = screen.blit(tube3_op_img, (x_tube3, tube3_height+d_2tube))


	# Tube rides to the left
	x_tube1 -= tube_velocity
	x_tube2 -= tube_velocity
	x_tube3 -= tube_velocity

	# Create new tubes
	if x_tube1 < -tube_width:
		x_tube1 = 550
		tube1_height = randint(100,400)
		tube1_pass = False
	if x_tube2 < -tube_width:
		x_tube2 = 550
		tube2_height = randint(100,400)
		tube2_pass = False
	if x_tube3 < -tube_width:
		x_tube3 = 550
		tube3_height = randint(100,400)
		tube3_pass = False

	# Draw bird
	bird = screen.blit(bird_img, (x_bird, y_bird))

	# Falling bird
	y_bird += bird_drop_velocity
	bird_drop_velocity += gravity

	score_txt = font.render("Score:" + str(score), True, RED)
	screen.blit(score_txt, (5,5))

	# Add score
	if x_tube1 + tube_width <= x_bird and tube1_pass == False:
		score += 1
		tube1_pass = True
	if x_tube2 + tube_width <= x_bird and tube2_pass == False:
		score += 1
		tube2_pass = True
	if x_tube3 + tube_width <= x_bird and tube3_pass == False:
		score += 1
		tube3_pass = True

	# Kiểm tra sự va chạm
	tubes = [tube1, tube2, tube3, tube1_op, tube2_op, tube3_op]
	for tube in tubes:
		if bird.colliderect(tube):
			tube_velocity = 0
			bird_drop_velocity = 0
			game_over_txt = font_GameOver.render("Game Over,Score:" + str(score), True, RED)
			screen.blit(game_over_txt, (120,260))
			space_txt = font_GameOver.render("Press space to continue!", True, BLUE)
			screen.blit(space_txt, (85,290))
			pausing = True
			pygame.mixer.pause()

	# Draw sand
	sand = screen.blit(sand_img, (0, 555))

	if bird.colliderect(sand):
		tube_velocity = 0
		bird_drop_velocity = 0
		game_over_txt = font_GameOver.render("Game Over,Score:" + str(score), True, RED)
		screen.blit(game_over_txt, (120,260))
		space_txt = font_GameOver.render("Press space to continue!", True, BLUE)
		screen.blit(space_txt, (85,290))
		pausing = True
		pygame.mixer.pause()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				bird_drop_velocity = 0
				bird_drop_velocity -= 7
				if pausing:
					pygame.mixer.unpause()
					x_bird = 50
					y_bird = 350
					x_tube1 = 400
					x_tube2 = 600
					x_tube3 = 800
					bird_drop_velocity = 0
					score = 0
					tube_velocity = 2
					pausing = False
					time.sleep(0.5)


	pygame.display.flip()

pygame.quit()