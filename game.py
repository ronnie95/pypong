import pygame
import random
import time
import sys
pygame.init()

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (1360, 768)
screen = pygame.display.set_mode(SCREEN_SIZE)

screen.fill(BLACK)

ball_center = (int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2))
ball_radius = 20
ball = pygame.draw.circle(screen, RED, ball_center, ball_radius)

PADDLE_LENGTH = 150
PADDLE_WIDTH = 10

paddle1_top = (5, int((SCREEN_HEIGHT/2) - (PADDLE_LENGTH/2)))
paddle1_bottom = (5, int((SCREEN_HEIGHT/2) + (PADDLE_LENGTH/2)))

paddle2_top=(SCREEN_WIDTH-6, int((SCREEN_HEIGHT/2) - (PADDLE_LENGTH/2)))
paddle2_bottom = (SCREEN_WIDTH-6, int((SCREEN_HEIGHT/2) + (PADDLE_LENGTH/2)))


paddle1 = pygame.draw.line(screen,GREEN,paddle1_top,paddle1_bottom,PADDLE_WIDTH)
paddle2 = pygame.draw.line(screen,GREEN,paddle2_top,paddle2_bottom,PADDLE_WIDTH)

bar_1_top=(10,0)
bar_1_bottom=(10,SCREEN_HEIGHT)
bar_2_top=(SCREEN_WIDTH-10,0)
bar_2_bottom=(SCREEN_WIDTH-10,SCREEN_HEIGHT)

bar1=pygame.draw.line(screen,WHITE,bar_1_top,bar_1_bottom,2)
bar2=pygame.draw.line(screen,WHITE,bar_2_top,bar_2_bottom,2)

ball_velocity = (random.choice(range(-5,5)), random.choice(range(-15, 15)))
paddle1_velocity = (0,0)
paddle2_velocity = (0,0)

def get_new_position(pos, vel):
	return (pos[0]+vel[0],pos[1]+vel[1])
p1=0
p2=0
sc=0
try:
	fname=open("scores.txt","r")
	sc=int(fname.read())
	fname.close()
except:
	fname=open("scores.txt","w")
	fname.close()


pygame.display.update()
while True:
	screen.fill(BLACK)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			fname=open("scores.txt","w")
			fname.write(str(max(sc,p1,p2)))
			fname.close()
			fname.close()
			pygame.quit()
			sys.exit()
		
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				paddle2_velocity = (0,-8)    #3 is arbitrary	
			elif event.key == pygame.K_DOWN:
				paddle2_velocity = (0,8)
			elif event.key == pygame.K_w:
				paddle1_velocity = (0,-8)    #Fill in the right values
			elif event.key == pygame.K_s:
				paddle1_velocity = (0,8)   #Fill in the right values
			elif event.key==pygame.K_r:
				ball = pygame.draw.circle(screen, BLACK, ball_center, ball_radius)				
				ball_center = (int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2))
				ball_velocity = (random.choice(range(-5,5)), random.choice(range(-15, 15)))
				sc=max(sc,p1,p2)
				fname=open("scores.txt","w")
				fname.write(str(sc))
				fname.close()
				p1=0
				p2=0

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP or event.key==pygame.K_DOWN:
				paddle2_velocity = (0,0)
			if event.key==pygame.K_w or event.key==pygame.K_s:
				paddle1_velocity=(0,0)

	
	#paddle1 = pygame.draw.line(screen,BLACK,paddle1_top,paddle1_bottom,PADDLE_WIDTH)
	#paddle2 = pygame.draw.line(screen,BLACK,paddle2_top,paddle2_bottom,PADDLE_WIDTH)

	p2_top = get_new_position(paddle2_top, paddle2_velocity)
	p2_bottom = get_new_position(paddle2_bottom, paddle2_velocity)
	
	p1_top = get_new_position(paddle1_top, paddle1_velocity)
	p1_bottom = get_new_position(paddle1_bottom, paddle1_velocity)
	
	if(p1_top[1]>0 and p1_bottom[1]<SCREEN_HEIGHT):
		paddle1_top=p1_top
		paddle1_bottom=p1_bottom
	
	if(p2_top[1]>0 and p2_bottom[1]<SCREEN_HEIGHT):
		paddle2_top=p2_top
		paddle2_bottom=p2_bottom


	paddle1 = pygame.draw.line(screen,GREEN,paddle1_top,paddle1_bottom,PADDLE_WIDTH)

	paddle2 = pygame.draw.line(screen,GREEN,paddle2_top,paddle2_bottom,PADDLE_WIDTH)

	if(ball_center[1]+ball_radius>=SCREEN_HEIGHT or ball_center[1]-ball_radius<=0):
		ball_velocity=(ball_velocity[0],-ball_velocity[1])
	#if(ball_center[0]+ball_radius==894 or ball_center[0]-ball_radius==8):
	#	x=ball_velocity[0]		
	#	ball_velocity=(-x,ball_velocity[1])

	#ball = pygame.draw.circle(screen, BLACK, ball_center, ball_radius)	
	ball_center = get_new_position(ball_center, ball_velocity)
	#draw the new ball
	ball = pygame.draw.circle(screen, RED, ball_center, ball_radius)
	

	if(ball_center[0]+ball_radius>=SCREEN_WIDTH-10):
		if (paddle2_top[1] < ball_center[1] and paddle2_bottom[1] > ball_center[1]):
			ball_velocity = (-ball_velocity[0], ball_velocity[1])
			p2=p2+1
		else:
			ball = pygame.draw.circle(screen, BLACK, ball_center, ball_radius)				
			ball_center = (int(SCREEN_WIDTH/2),int(SCREEN_HEIGHT/2))
			ball_velocity = (random.choice(range(-5,5)), random.choice(range(-15, 15)))
			myfont = pygame.font.SysFont("Arial", 50)			
			if(p1>p2):
				letter = myfont.render("PLAYER 1 WINS",0,WHITE)
			elif(p2>p1):
				letter = myfont.render("PLAYER 2 WINS",0,WHITE)
			else:
				letter = myfont.render("   !!IT IS A TIE!!",0,WHITE)
			screen.fill(BLACK)
			screen.blit(letter,(SCREEN_WIDTH*0.38, SCREEN_HEIGHT/3))
			pygame.display.update()
			time.sleep(1)
			sc=max(sc,p1,p2)
			fname=open("scores.txt","w")
			fname.write(str(sc))
			fname.close()
			p2=0
			p1=0
	
	if(ball_center[0]-ball_radius<=10):
		if (paddle1_top[1] < ball_center[1] and paddle1_bottom[1] > ball_center[1]):
			ball_velocity = (-ball_velocity[0], ball_velocity[1])
			p1=p1+1
		else:
			ball = pygame.draw.circle(screen, BLACK, ball_center, ball_radius)				
			ball_center = (int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2))
			ball_velocity = (random.choice(range(-5,5)), random.choice(range(-15, 15)))
			myfont = pygame.font.SysFont("Arial", 50)			
			if(p1>p2):
				letter = myfont.render("PLAYER 1 WINS",0,WHITE)
			elif(p2>p1):
				letter = myfont.render("PLAYER 2 WINS",0,WHITE)
			else:
				letter = myfont.render("   !!IT IS A TIE!!",0,WHITE)	
			screen.fill(BLACK)
			screen.blit(letter,(SCREEN_WIDTH*0.38, SCREEN_HEIGHT/3))
			pygame.display.update()
			time.sleep(1)
			sc=max(sc,p1,p2)
			fname=open("scores.txt","w")
			fname.write(str(sc))
			fname.close()
			p1=0
			p2=0
			
	
	myfont = pygame.font.SysFont("Arial", 20)
	letter = myfont.render("PLAYER 1",0,WHITE)
	screen.blit(letter,(SCREEN_WIDTH*0.25, SCREEN_HEIGHT/9))
	
	myfont = pygame.font.SysFont("Arial", 40)
	letter = myfont.render(str(p1),0,WHITE)
	screen.blit(letter,(SCREEN_WIDTH*0.25 + 20, (SCREEN_HEIGHT/9)+40))


	myfont = pygame.font.SysFont("Arial", 20)
	letter = myfont.render("PLAYER 2",0,WHITE)
	screen.blit(letter,(SCREEN_WIDTH*0.7, SCREEN_HEIGHT/9))

	myfont = pygame.font.SysFont("Arial", 40)
	letter = myfont.render(str(p2),0,WHITE)
	screen.blit(letter,(SCREEN_WIDTH*0.7 + 20, (SCREEN_HEIGHT/9)+40))

	myfont = pygame.font.SysFont("Arial", 20)
	letter = myfont.render("HIGH SCORE:"+str(max(sc,p1,p2)),0,WHITE)
	screen.blit(letter,(SCREEN_WIDTH*0.45, SCREEN_HEIGHT/10))
	
	myfont = pygame.font.SysFont("Arial", 15)
	letter = myfont.render("PRESS R TO RESET",0,WHITE)
	screen.blit(letter,(SCREEN_WIDTH*0.45, SCREEN_HEIGHT-20))
	
	myfont = pygame.font.SysFont("Arial", 25)
	letter = myfont.render("!!PYPONG!!",0,(255,255,0))
	screen.blit(letter,(SCREEN_WIDTH*0.45, 5))


	bar1=pygame.draw.line(screen,WHITE,bar_1_top,bar_1_bottom,2)
	bar2=pygame.draw.line(screen,WHITE,bar_2_top,bar_2_bottom,2)

	#update the changes on the screen
	
	time.sleep(0.008)
	pygame.display.update()











