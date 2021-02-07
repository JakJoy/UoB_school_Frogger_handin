from pygame import *
init()

# define global variables
width = 1200
height = 750
screen = display.set_mode((width, height))
x = 600
y = 675
win = 0

gameover = False

score = 0

angle = 0
# frog globals
froggerImage = image.load("frog.png")
froggerImage = transform.scale(froggerImage,(75,70))
froggerImage1 = transform.rotate(froggerImage, 0)
froggerImage2 = transform.rotate(froggerImage, 90)
froggerImage3 = transform.rotate(froggerImage, 180)
froggerImage4 = transform.rotate(froggerImage, 270)

FrogIMG = froggerImage
frog = Rect(x, y, froggerImage.get_width()-5, froggerImage.get_height()-5)

playbutton = image.load('playbutton2.png')
playbutton = transform.scale(playbutton,(250,150))
playRect = Rect(460,410,250,150)

# car globals
carImage = image.load("car.png")
carImage = transform.scale(carImage,(150,75))
carImage1 = image.load("car2.png")
carImage1 = transform.scale(carImage1,(225,75))
carImage1 = transform.rotate(carImage1,(180))

carList = []
carList1 = []

roadList = []

font1 = font.Font('ARCADE_N.TTF',45)
frogtext = font1.render("Frogger",True,(57,237,44))

lilypad = image.load("lilypad.png")
lilypad = transform.scale(lilypad,(75,75))
lilylist = []

lily1 = Rect(375,75,lilypad.get_width(),lilypad.get_height())
lilylist.append(lily1)
lily2 = Rect(750,75,lilypad.get_width(),lilypad.get_height())
lilylist.append(lily2)

logImage = image.load("log.png")
logImage = transform.scale(logImage,(225,180))
logList = []

class logRecord():
	logRect = None
	logSpeed = 0

log1 = logRecord()
log2 = logRecord()
log3 = logRecord()

log4 = logRecord()
log5 = logRecord()
log6 = logRecord()

log1.logRect = Rect(75,170,logImage.get_width(), logImage.get_height())
log1.logSpeed = 5
logList.append(log1.logRect)

log2.logRect = Rect(315,170,logImage.get_width(), logImage.get_height())
log2.logSpeed = 5
logList.append(log2.logRect)

log3.logRect = Rect(735,170,logImage.get_width(), logImage.get_height())
log3.logSpeed = 5
logList.append(log3.logRect)

log4.logRect = Rect(435,95,logImage.get_width(), logImage.get_height())
log4.logSpeed = -5
logList.append(log4.logRect)

log5.logRect = Rect(75,95,logImage.get_width(), logImage.get_height())
log5.logSpeed = -5
logList.append(log5.logRect)

log6.logRect = Rect(975,95,logImage.get_width(), logImage.get_height())
log6.logSpeed = -5
logList.append(log6.logRect)

class carRecord():
	carRect = None
	carSpeed = 0
	
car1 = carRecord()
car2 = carRecord()
car3 = carRecord()
car4 = carRecord()

car5 = carRecord()
car6 = carRecord()
car7 = carRecord()
car8 = carRecord()
# cars 
# TASK 3 - Add more cars!

car1.carRect = Rect(450,530,carImage.get_width()-5, carImage.get_height()-5)
car1.carSpeed = 4
carList.append(car1.carRect)

car2.carRect = Rect(150,530,carImage.get_width()-5, carImage.get_height()-5)
car2.carSpeed = 4
carList.append(car2.carRect)

car3.carRect = Rect(0,530,carImage.get_width()-5, carImage.get_height()-5)
car3.carSpeed = 4
carList.append(car3.carRect)

car4.carRect = Rect(900,530,carImage.get_width()-5, carImage.get_height()-5)
car4.carSpeed = 4
carList.append(car4.carRect)

car5.carRect = Rect(600,445,carImage1.get_width(), carImage1.get_height())
car5.carSpeed = -4
carList1.append(car5.carRect)

car6.carRect = Rect(300,445,carImage1.get_width(), carImage1.get_height())
car6.carSpeed = -4
carList1.append(car6.carRect)

car7.carRect = Rect(0,445,carImage1.get_width(), carImage1.get_height())
car7.carSpeed = -4
carList1.append(car7.carRect)

car8.carRect = Rect(900,445,carImage1.get_width(), carImage1.get_height())
car8.carSpeed = -4
carList1.append(car8.carRect)


road1 = Rect(450,522,30,8)
roadList.append(road1)
road2 = Rect(350,522,30,8)
roadList.append(road2)
road3 = Rect(250,522,30,8)
roadList.append(road3)
road4 = Rect(150,522,30,8)
roadList.append(road4)
road5 = Rect(50,522,30,8)
roadList.append(road5)
road6 = Rect(550,522,30,8)
roadList.append(road6)
road7 = Rect(650,522,30,8)
roadList.append(road7)
road8 = Rect(750,522,30,8)
roadList.append(road8)
road9 = Rect(850,522,30,8)
roadList.append(road9)
road10 = Rect(950,522,30,8)
roadList.append(road10)
road11 = Rect(1050,522,30,8)
roadList.append(road11)
road12 = Rect(1150,522,30,8)
roadList.append(road12)


gameOver = False

# TASK 1 draw the background function!
# define functions
def drawBackground():
	global screen
	screen.fill((0,0,0))
	# draw your background as you wish!

def drawPlayer():
	global screen, x, y, froggerImage, angle
	screen.blit(FrogIMG, (x,y))

# TASK 2 draw cars
def drawCars():
	global carList,screen, carImage
	for c in carList:
		screen.blit(carImage,c)
	for c in carList1:
		screen.blit(carImage1,c)

def drawLogs():
	global logList, screen, logImage
	for l in logList:
		screen.blit(logImage,l)

def drawRoad():
	global roadList,screen
	road = draw.rect(screen,(158,164,166),(0,440,1200,170))
	for r in roadList:
		draw.rect(screen,(255,255,255),r)

def drawLilyPads():
	global lilylist
	for l in lilylist:
		screen.blit(lilypad,l)
	

# TASK 4 - Move the cars. If they go off the screen then wrap them. 
def moveCars():
	global carList, carList1
	if 1200 < car1.carRect[0] < 1250:
		car1.carRect[0] = -160
	if 1200 < car2.carRect[0] < 1250:
		car2.carRect[0] = -160
	if 1200 < car3.carRect[0] < 1250:
		car3.carRect[0] = -160
	if 1200 < car4.carRect[0] < 1250:
		car4.carRect[0] = -160
	
	if -260 < car5.carRect[0] < -225:
		car5.carRect[0] = 1200
	if -260 < car6.carRect[0] < -225:
		car6.carRect[0] = 1200
	if -260 < car7.carRect[0] < -225:
		car7.carRect[0] = 1200
	if -260 < car8.carRect[0] < -225:
		car8.carRect[0] = 1200
	
	car1.carRect.move_ip(car1.carSpeed,0)
	car2.carRect.move_ip(car2.carSpeed,0)
	car3.carRect.move_ip(car3.carSpeed,0)
	car4.carRect.move_ip(car4.carSpeed,0)
	
	car5.carRect.move_ip(car5.carSpeed,0)
	car6.carRect.move_ip(car6.carSpeed,0)
	car7.carRect.move_ip(car7.carSpeed,0)
	car8.carRect.move_ip(car8.carSpeed,0)

def moveLogs():
	global logList
	if 1200 < log1.logRect[0] < 1250:
		log1.logRect[0] = -220
	if 1200 < log2.logRect[0] < 1250:
		log2.logRect[0] = -220
	if 1200 < log3.logRect[0] < 1250:
		log3.logRect[0] = -220
	
	if -260 < log4.logRect[0] < -225:
		log4.logRect[0] = 1200	
	if -260 < log5.logRect[0] < -225:
		log5.logRect[0] = 1200
	if -270 < log6.logRect[0] < -225:
		log6.logRect[0] = 1200
	log1.logRect.move_ip(log1.logSpeed,0)
	log2.logRect.move_ip(log2.logSpeed,0)
	log3.logRect.move_ip(log3.logSpeed,0)
	log4.logRect.move_ip(log4.logSpeed,0)
	log5.logRect.move_ip(log5.logSpeed,0)
	log6.logRect.move_ip(log6.logSpeed,0)


z = 0

while not gameOver:
	for e in event.get():
		# task 5 - Make frogger move up and down.
		if e.type == QUIT: 
			gameOver = True
		elif e.type == KEYDOWN:
			if e.key == K_LEFT and x != 0:
				x += -75
				FrogIMG = froggerImage2
				drawPlayer()
			if e.key == K_RIGHT and x != 1125:
				x += 75
				FrogIMG = froggerImage4
				drawPlayer()
			if e.key == K_UP and y != 75:
				y += -75
				FrogIMG = froggerImage1
				drawPlayer()
			if e.key == K_DOWN and y != 675:
				y += 75
				FrogIMG = froggerImage3
				drawPlayer()
	# TASK 6 - Make a more polished frogger game :)
	# movement
	#moveCars()
	# game mechanics
	for c in carList:
		if c.colliderect(x, y, froggerImage.get_width(), froggerImage.get_height()):
			# collided with car
			z += 1
	for c in carList1:
		if c.colliderect(x, y, froggerImage.get_width(), froggerImage.get_height()):
			# collided with car
			z += 1
	# drawing
	drawBackground()
	draw.rect(screen,(142,108,29),(0,300,1200,450))
	draw.rect(screen,(255,255,255),(436,5,330,60))
	draw.rect(screen,(0,0,0),(441,10,320,50))
	draw.rect(screen,(9,161,9),(0,75,1200,75))
	drawRoad()
	drawLilyPads()
	water = draw.rect(screen,(0,171,219),(0,150,1200,150))
	drawLogs()
	if gameover == False:
		drawPlayer()
	drawCars()
	moveCars()
	moveLogs()
	screen.blit(frogtext,(450,15))
	if y < 150:
		if 340 < x < 410:
			x = 375
			win = 1 
		elif 715 < x < 785:
			x = 750
			win = 1
		else:
			x = 600
			y = 675
			z+= 1
	if 150 < y < 300:
		if log1.logRect[0] < x < (log1.logRect[0] + 150):
			x += log1.logSpeed
		elif log2.logRect[0] < x < (log2.logRect[0] + 150):
			x += log2.logSpeed
		elif log3.logRect[0] < x < (log3.logRect[0] + 150):
			x += log3.logSpeed
		else: 
			x = 600
			y = 675
			z += 1
		
	if 75 < y < 225:
		if log5.logRect[0] < x < (log5.logRect[0] + 150):
			x += (log5.logSpeed)
		elif log4.logRect[0] < x < (log4.logRect[0] + 150):
			x += (log4.logSpeed)
		elif log6.logRect[0] < x < (log6.logRect[0] + 150):
			x += (log6.logSpeed)
		else: 
			x = 600
			y = 675
			z += 1
	if z > 0:
		x = 600
		y = 675
		gameover = True
		z = 0
	if win == 1 and y >= 675:
		log1.logSpeed += 1
		log2.logSpeed += 1
		log3.logSpeed += 1
		log4.logSpeed -= 1
		log5.logSpeed -= 1
		log6.logSpeed -= 1
		
		car1.carSpeed += 1
		car2.carSpeed += 1
		car3.carSpeed += 1
		car4.carSpeed += 1
		car5.carSpeed -= 1
		car6.carSpeed -= 1
		car7.carSpeed -= 1
		car8.carSpeed -= 1
		score += 1
		win = 0
	if gameover == True:
		for e in event.get():
			if e.type == MOUSEBUTTONDOWN:
				pos = mouse.get_pos()
				if playRect.collidepoint(pos):
					z = 0
					score = 0
					gameover = False
					x = 600
					y = 675
					log1.logSpeed = 5
					log2.logSpeed = 5
					log3.logSpeed = 5
					log4.logSpeed = -5
					log5.logSpeed = -5
					log6.logSpeed = -5
					
					car1.carSpeed = 4
					car2.carSpeed = 4
					car3.carSpeed = 4
					car4.carSpeed = 4
					car5.carSpeed = -4
					car6.carSpeed = -4
					car7.carSpeed = -4
					car8.carSpeed = -4
		draw.rect(screen,(255,255,255),(300,200,600,400))
		draw.rect(screen,(0,0,0),(310,210,580,380))
		gameovertext = font1.render("GAME OVER", True,(255,255,255))
		scoretext = font1.render("Score - "+str(score), True,(18,221,224))
		screen.blit(gameovertext,(400,240))
		screen.blit(scoretext,(400,350))
		screen.blit(playbutton,(460,410))
	#drawCars()
	# show the newly drawn screen (double buffering)
	display.flip()
	# short delay to slow down animation.
	
