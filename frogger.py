from pygame import *
init()

# define global variables
width = 1200
height = 1000
screen = display.set_mode((width, height))


# frog globals
froggerImage = image.load("frog.jpg")
frog = Rect(600, 800, froggerImage.get_width(), froggerImage.get_height())
px = 0
py = 0

# car globals
carImage = image.load("car.png")
Img_car = transform.scale(carImage, (80,80))
carList = []
cx = 2

class carRecord():
	carRect = None
	carSpeed = None




# cars
# TASK 3 - Add more cars! # 	DONE


car1 = carRecord()
car1.carRect = Rect(400,500,carImage.get_width(), carImage.get_height())
car1.carSpeed = -4

gameOver = False

# TASK 1 draw the background function!
# define functions
def drawBackground():
	global screen
	screen.fill((0,0,0))
	# draw your background as you wish!

def drawPlayer():
	global screen, frog, froggerImage
	screen.blit(froggerImage, frog)

def moveFrog():
	global py, px, frog
	frog.move_ip(px,py)
	frog.move_ip(px, py)


# TASK 4 - Move the cars. If they go off the screen then wrap them.
def moveCars():
	global car1
	car1.carRect.move_ip(-3,0)
	car1.carRect.move_ip(-3, 0)
	#Img_car.move_ip(cx, py)

	pass


# TASK 2 draw cars # DONE
def drawCars():
	global screen, car1, carImage
	xx = 0
	ddd = 10
	while xx < 5:
		screen.blit(Img_car,car1.carRect(ddd,500))
		ddd += 200
		xx += 1



while not gameOver:
	for e in event.get():
		# task 5 - Make frogger move up and down. # DONE
		if e.type == QUIT:
			gameOver = True
		elif e.type == KEYDOWN:
			if e.key == K_LEFT:
				px = -3
			if e.key == K_RIGHT:
				px = 3
			if e.key == K_UP:
				py = -3
			if e.key == K_DOWN:
				py = 3
		elif e.type == KEYUP:
			if e.key == K_LEFT or e.key == K_RIGHT:
				px = 0
			if e.key == K_UP or e.key == K_DOWN:
				py = 0


	# TASK 6 - Make a more polished frogger game :)

	# movement
	moveFrog() # DONE
	#moveCars()
	# game mechanics
	#for cars in carList:
		#if cars.colliderect(player):
			# collided with car
			#exit()
	# drawing
	drawBackground()
	drawPlayer()
	drawCars()

	# show the newly drawn screen (double buffering)
	display.flip()
	# short delay to slow down animation.
	time.delay(5)


#if frog.x + px > 0 and frog.x + frog.w + px < width and frog.y + py > 0 and frog.y + frog.h + py < height:


#^^ use this for boundary code

#def createCars(count):
  # cx = 10
  # cy = 45

  # while count <= 2:
    # car1.carRect = Rect(cx, cy, carImage.get_width(), carImage.get_height())
    # car1.carSpeed = -4

    # car2.carRect = Rect(cx, cy, carImage.get_width(), carImage.get_height())
    # car2.carSpeed = -4

     ##carList.append(car1)
    # cy = cy + 10
   #  carList.append(car2)
    # count = count + 1

  ## return carList

#cars = createCars(count)  # calls function




#[12:01 PM] Mr A Hamflett
#createCars(maxCount)
#count <= maxCount
#count = 1

