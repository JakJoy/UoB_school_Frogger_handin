from pygame import *
import random
import time
 
init()
 
# define global variables
width = 1000
height = 1000
screen = display.set_mode((width, height))
main_font = font.SysFont("comicsans", 40)
main_font2 = font.SysFont("comicsans", 200)


count = 0
onLog = 0
 
black = (0, 0, 0)
 
red = (200, 0, 0)
 
bright_red = (255, 0, 0)
 
white = (255, 255, 255)
 
green = (0, 200, 0)
 
bright_green = (0, 255, 0)

gameOver = False 

# frog globals
froggerImage = image.load("frog2.png")
froggerImage = transform.scale(froggerImage,(60,60))
x = 300
y = 950
frog = Rect(x, y, froggerImage.get_width(), froggerImage.get_height())
px = 0
py = 0
 
# car globals
carImage = image.load("Car.png")
carImage = transform.scale(carImage,(60,90))
carList = []
 
# background globals
bg = image.load("bg.png")
bg = transform.scale(bg, (1000, 1000))
 
#load enemy image
log = image.load("log.png")
log = transform.scale(log, (200, 60))
logList = []

class carRecord():
    carRect = None
    carSpeed = 0
 
 
car1 = carRecord()
car2 = carRecord()
car3 = carRecord()
car4 = carRecord()
# cars
# TASK 3 - Add more cars!
 
car1.carRect = Rect(0,525,carImage.get_width(),carImage.get_height())
car1.carSpeed = 6
car2.carRect = Rect(0,675,carImage.get_width(),carImage.get_height())
car2.carSpeed = 7
car3.carRect = Rect(0,600,carImage.get_width(),carImage.get_height())
car3.carSpeed = 4
car4.carRect = Rect(0,830,carImage.get_width(),carImage.get_height())
car4.carSpeed = 8

 
carList.append(car1)
carList.append(car2)
carList.append(car3)
carList.append(car4)

class logRecord():
    logRect = None
    logSpeed = 0

log1 = logRecord()
log2 = logRecord()
log3 = logRecord()
log4 = logRecord()

log1.logRect = Rect(0,325,log.get_width(),log.get_height())
log1.logSpeed = 3
log2.logRect = Rect(0,225,log.get_width(),log.get_height())
log2.logSpeed = 1
log3.logRect = Rect(0,125,log.get_width(),log.get_height())
log3.logSpeed = 2
log4.logRect = Rect(0,400,log.get_width(),log.get_height())
log4.logSpeed = 2

logList.append(log1)
logList.append(log2)
logList.append(log3)
logList.append(log4)


 

 
def button(message,x,y,w,h,inactive_col,active_col,action=None): 

        
        mouse_track = mouse.get_pos()
        click = mouse.get_pressed()
        
        if x+w > mouse_track[0] > x and y+h > mouse_track[1] > y:
                draw.rect(screen, active_col, (x,y,w,h))
                if click[0] == 1 and action != None:
                        action()

        else:
                draw.rect(screen, inactive_col, (x,y,w,h))

        smallText = font.Font("cosmicalien.ttf",20)
        textSurf, textRect = text_objects(message, smallText)
        textRect.center = ((x+(w/2)), (y+(h/2)))
        screen.blit(textSurf, textRect)

def controls():

    c = True

    while c:
        for e in event.get():
            if e.type == QUIT:
                quit()

        screen.fill(white)
        largeText = font.Font('cosmicalien.ttf',100)
        smallText = font.Font('cosmicalien.ttf',20)
        TextSurf, TextRect = text_objects("Controls", largeText)
        TextRect.center = ((width/2), (height-900))
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Movements -> Arrow Keys",smallText)
        TextRect.center = (width/2, height-800)
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Objective -> Reach the end whilst avoiding the obstacles",smallText)
        TextRect.center = (width/2, height-700)
        screen.blit(TextSurf, TextRect)

        
        button("Start",100,900,150,50,green,bright_green,gameloop)
        button("Quit",800,900,150,50,red,bright_red,quitgame)

        display.update()

        

def unpause():
       global pause
       pause = False

def paused():

        largeText = font.Font('cosmicalien.ttf',100)
        TextSurf, TextRect = text_objects2("Game Paused", largeText)
        TextRect.center = ((width/2), (height/2))
        screen.blit(TextSurf, TextRect)

        while pause:
                for e in event.get():
                        if e.type == QUIT:
                                pygame.quit()
                                quit()
                #screen.fill(white)

                button("Continue",275,550,150,50,green,bright_green,unpause)
                button("Rage Quit",775,550,150,50,red,bright_red,quitgame)

                


                #draw.rect(screen, red, (775,550,150,50))
                


                
                display.update()
def win():


    if frog.y < 40:
        message_display("You Win")
        time.sleep(2)

        display.update()
        quit()
            



def game_intro():

        intro = True

        while intro:
                for e in event.get():
                        if e.type == QUIT:
                                #pygame.quit()
                                quit()
                screen.fill(white)
                largeText = font.Font('cosmicalien.ttf',100)
                TextSurf, TextRect = text_objects("Frogger", largeText)
                TextRect.center = ((width/2), (height-900))
                screen.blit(TextSurf, TextRect)


                
                button("Controls",420,400,150,50,green,bright_green,controls)
                button("Start",420,200,150,50,green,bright_green,gameloop)
                button("Quit",420,300,150,50,red,bright_red,quitgame)

                


                #draw.rect(screen, red, (775,550,150,50))
                


                
                display.update()

def text_objects2(text, font):
 
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def text_objects(text, font):
    global red
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):


    largeText = font.Font('cosmicalien.ttf',100)
    TextSurf, TextRect = text_objects2(text, largeText)
    TextRect.center = ((width/2), (height/2))
    screen.blit(TextSurf, TextRect)

    display.update()


 

 
 
def quitgame():
    quit()
 
 
def drawBackground():
    global screen,bg
    screen.fill((0, 0, 0))
    screen.blit(bg, (0,0))
 
 
 
# draw your background as you wish!
 
def drawPlayer():
    global screen, frog, froggerImage
    screen.blit(froggerImage, frog)
 
 
def moveFrog():
    global px,py, frog, width
    #if frog.x + px > -10 and frog.x + frog.w + px < width - 20 and frog.y + py > 0 and frog.y + frog.h + py < height - 147:
    frog.move_ip(px,py)
 

 
# TASK 2 draw cars
def drawCars():
    global screen, carList, carImage
 
    for c in carList:
      screen.blit(carImage, c.carRect)
      if c.carRect.x == 0:
          c.carSpeed = random.randint(5,8)

def drawLog():
    global screen, logList, log

    for l in logList:
        screen.blit(log, l.logRect)
        if l.logRect.x == 0:
            l.logSpeed = random.randint(3,6)
 
 
# TASK 4 - Move the cars. If they go off the screen then wrap them.
def moveCars():
    global carList
    for c in carList:
        c.carRect.move_ip(c.carSpeed,0)
        if c.carRect.x >= width:
            c.carRect.x = 0
 

def moveLog():
    global logList,log
    for l in logList:
        l.logRect.move_ip(l.logSpeed,0)

        if l.logRect.x >= 1700:
            l.logRect.x = 1550
            l.logSpeed = random.randint(4,12)
            l.logSpeed = l.logSpeed * -1

        if l.logRect.x <= -300:
            l.logRect.x = -150
            l.logSpeed = l.logSpeed * -1


    
def car_collide():
    global lives_value
    
    for c in carList:
        if c.carRect.colliderect(frog):
            message_display("You Lost")
            time.sleep(2)
            quit()
            

            display.update()

def enemy_collide():
    for e in enemyList:
        if e.enemyRect.colliderect(frog):
            message_display("You Lost")
            time.sleep(2)
            quit()

            display.update()

            
def gameloop():
    global gameOver, px, py, onLog, count
    
    while not gameOver:
            for e in event.get():
                # task 5 - Make frogger move up and down.
                if e.type == QUIT:
                    gameOver = True



                elif e.type == KEYDOWN:
                    if e.key == K_LEFT:
                        px = -3
                    if e.key == K_RIGHT:
                        px = 3
                    if e.key == K_DOWN:
                        py = 3
                    if e.key == K_UP:
                        py = -3
                    if e.key == K_p:
                        pause = True
                        pause()




                elif e.type == KEYUP:
                    if e.key == K_LEFT or e.key == K_RIGHT or e.key == K_DOWN or e.key == K_UP:
                        px = 0
                        py = 0

                #no diagonal movement 
                if (py == 3 and px == 3) or (py == -3 and px == -3) or (py == 3 and px == -3) or (py == -3 and px == 3):
                    py = 0
                    px = 0


                for l in logList:
                    count += 1
                    if l.logRect.colliderect(frog):
                        px = l.logSpeed
                        onLog = 1
                        count = 0
                    if l.logRect.colliderect(frog) == 1 and frog.x > width or frog.x < 0:
                        frog.x = x
                        frog.y = y

                    if l.logRect.colliderect(frog) == 0 and count == 7:
                        px = 0
                        count = 0
                    if frog.y < 355 and l.logRect.colliderect(frog) == 0 and count == 6:
                        frog.x = x
                        frog.y = y
                        count = 0









            # TASK 6 - Make a more polished frogger game :)
            if x == 100:
                quitgame()

            # movement
            moveFrog()
            # moveCars()

            # game mechanics

            for c in carList:
                if c.carRect.colliderect(frog):
                    quitgame()

            # drawing
            drawBackground()
            drawPlayer()
            drawCars()
            drawLog()

            moveCars()
            moveLog()
            car_collide()
            #enemy_collide()
            win()

            # show the newly drawn screen (double buffering)
            display.flip()
 
game_intro()
gameloop()
quit()
