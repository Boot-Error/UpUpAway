#This version is intended for Windows OS  only!

import pygame, sys, random, os
from pygame.locals import *

pygame.init()

#Display
root = pygame.display.set_mode([400, 300])
#FPS settings
FPS 	= 60
fpsClock= pygame.time.Clock()
#Main color tuple
WHITE 	= (255, 255, 255)
#constant variables for the rect
move 	= 390
mspeed 	= 6
width 	= 50
space 	= 100
#initial height of the rect
height1 = random.randint(50, 150)
height2 = space + (height1)
#Constant variables for the circle
radius 	= 20
circley = 100
upspeed	= 8
gspeed 	= 4
#Constants for score and red colour screen
score 	= 0
rvalue	= 0	
prescore= 0
#Console write
print "CIRCLY : A flappy bird replica" + "\nWritten in python using pygame library" + "\nBy : Vighnesh SK"
print "\nThe final score obtained after a hit is displayed below\n"
print "Press a key to start!\n\n"
os.system('pause')
#Comments:
comment = ("Awesome!", "Keep it up!", "King of the skies!", "I'm jealous of you!")
	
#Main game loop
while True:

	#FPS control
	fpsClock.tick(FPS)

	root.fill((rvalue, 0, 0))#fills the screen
	pygame.display.set_caption("Circly  "+"Score : " + str(score))

	#Mouse Event Check
	mousepress = pygame.mouse.get_pressed()[0]
	#if x==1:
		#print "left is pressed!"

	#Rect movement
	move -= mspeed
	if move <= 5:
		move = 390
		height1 = random.randint(50, 150)
		height2 = space + (height1)
		score += 1

	#Display rect
	#Top rect200
	pygame.draw.polygon(root, WHITE, ((move, 0), (move+width, 0), (move+width, height1), (move, height1)))
	#Bottom rect
	pygame.draw.polygon(root, WHITE, ((move, height2), (move+width, height2), (move+width, 300), (move, 300)))

	#Player Part
	pygame.draw.circle(root, WHITE, [150, circley], radius)
	if mousepress==1:
		circley -= upspeed
	circley +=gspeed

	#collision
	rvalue = 0
	#pillar collision
	if move == 150:
		if circley-radius < height1 or circley+radius > height2:#condition for pillar collision
			rvalue=255
			print "Your Final Score is ", score
			if prescore < score:
				print "\n<<< " + comment[random.randint(0,3)] + " >>>\n"
			prescore = score
			score = 0
			circley = 150
	#ground and sky collision
	if circley-radius==0 or circley+radius==300:
		rvalue=255
		print "Your Final Score is ", score
		if prescore < score:
			print "\n<<< " + comment[random.randint(0,3)] + " >>>\n"
		prescore = score
		score = 0
		circley = 150
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
