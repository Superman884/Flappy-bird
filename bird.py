import pygame
win=pygame.display.set_mode((500,300))
from random import randrange
clock = pygame.time.Clock()
dt = clock.tick(100)
delay=50
dead=False
score=0
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
pygame.mixer.init()
pygame.mixer.music.load("backmusic.mp3")
pygame.mixer.music.play(-1)
flap_sound = pygame.mixer.Sound("flap.wav")
godmode=False
class bird:
	def __init__(self):
		self.x=50
		self.y=150
		self.vel=0
		self.width=20
		self.height=20
	def jump(self):
		self.vel=-0.073
class pipeline:
	def __init__(self,width,height,x,y):
		self.width=width
		self.height=height
		self.x=x
		self.y=y
pipes=[]
pipes.append(pipeline(30,80,300,0))
pipes.append(pipeline(30,130,300,130))
pipes.append(pipeline(30,20,550,0))
pipes.append(pipeline(30,190,550,70))
img=pygame.image.load("MAN5.png")
img_copy=pygame.image.load("MAN5.png")
pipe=pygame.image.load("MAN3.png")
background=pygame.image.load("bacgroud.png")
background=pygame.transform.scale(background,(500,300))
birdy=bird()
gravity=0.0001
run=True
events = pygame.event.get()
while run:
	textsurface = myfont.render(str(score), False, (0, 0, 0))
	win.blit(textsurface,(200,0))
	if birdy.y>=240:
		dead=True
		pygame.mixer.music.stop()
	for i in pipes:
		if not dead:
			i.x-=0.08*dt
		pipe=pygame.image.load("MAN3.png")
		pipe=pygame.transform.scale(pipe,(i.width,i.height))
		win.blit(pipe,(i.x,i.y))
		if i.x<=-30:
			score+=1
			pipes.pop(0)
			pipes.pop(0)
			number1=(randrange(4)+1)*40
			pipes.append(pipeline(30,number1,500,0))
			pipes.append(pipeline(30,(300-number1)-100,500,number1+55))
		if (birdy.y>i.y and birdy.y<i.y+i.height) or (birdy.y+birdy.height>i.y and birdy.y<=i.y+i.height):
			if (birdy.x+birdy.width>i.x and birdy.x+birdy.width<i.x+30) or (birdy.x>i.x and birdy.x<i.x+30):
				dead=True
				pygame.mixer.music.stop()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run=False
	keys=pygame.key.get_pressed()
	if not dead:
		if keys[pygame.K_DOWN]:
			if not godmode:
				flap_sound.play()
				birdy.jump()
			else:
				birdy.y+=1
		elif keys[pygame.K_UP] and godmode:
			birdy.y-=1
		elif keys[pygame.K_j] and delay==0:
			godmode=not godmode
			delay=100
	else:
		if keys[pygame.K_RIGHT]:
			birdy=bird()
			pipes=[]
			pipes.append(pipeline(30,80,300,0))
			pipes.append(pipeline(30,130,300,130))
			pipes.append(pipeline(30,20,550,0))
			pipes.append(pipeline(30,190,550,70))
			dead=False
			pygame.mixer.music.play(-1)
			score=0
	if birdy.y<=240 and not godmode:
		birdy.y+=birdy.vel*dt
		birdy.vel+=gravity*dt
	win.blit(img_copy,(birdy.x,birdy.y))
	angle=birdy.vel*-800
	if angle<-80:
		angle=-80
	img_copy=pygame.transform.rotate(img,angle)
	pygame.display.update()
	win.fill((0,0,0))
	win.blit(background,(0,0))
	if delay!=0:
		delay-=1