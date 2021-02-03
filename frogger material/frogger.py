from pygame import*
init()
width=1200
height=1200
screen=display.set_mode((width,height))
dx=0
dy=0
halberd=image.load("halberd.PNG")
warpstar1=image.load("warpstar.PNG")
warpstar=image.load("warpstar.PNG")
starcutter=image.load("starcutter.PNG")
player=image.load("player.PNG")


player=transform.scale(player,(80,80))
playerbox=Rect(500,900, 55, 55)
screen.blit(player,playerbox)


count=0
warpstarx=30
warpstarlist=[]
while count<=4:
    warpstar=transform.scale(warpstar,(80,70))
    screen.blit(warpstar,(warpstarx,310))
    warpstarbox=Rect(warpstarx, 310, 70, 70)
    warpstarlist.append(warpstarbox)
    warpstarx=warpstarx+250
    count=count+1


count1=0
warpstar2x=30
warpstar2list=[]
while count1<=4:
    warpstar2=transform.scale(warpstar,(80,70))
    screen.blit(warpstar,(warpstar2x,770))
    warpstarbox2=Rect(warpstar2x, 770, 70, 70)
    warpstar2list.append(warpstarbox2)
    warpstar2x=warpstar2x+250
    count1=count1+1



count2=0
starcutterx=1190
starcutterlist=[]
while count2<=4:
    starcutter=transform.scale(starcutter,(130,110))
    screen.blit(starcutter,(starcutterx,400))
    starcutterbox=Rect(starcutterx, 400, 125 , 90)
    starcutterlist.append(starcutterbox)
    starcutterx=starcutterx-270
    count2=count2+1




count=0
halberdx=20
halberdlist=[]
while count<=3:
    halberd=transform.scale(halberd,(200,100))
    screen.blit(halberd,(halberdx,630))
    halberdbox=Rect(halberdx, 630, 190, 80)
    halberdlist.append(halberdbox)
    halberdx=halberdx+340
    count=count+1

  





gameover=False
while gameover==False:
    screen.fill((0,0,0))
    
    rect=draw.rect(screen,(100,100,100),(0,300,1200,550),0) 
    draw.line(screen,(255,255,255),(0,760),(1200,760),5)
    draw.line(screen,(255,255,255),(0,390),(1200,390),5)
        
  
        
    for warpstarbox in warpstarlist:
        warpstarbox.move_ip(2,0)
        screen.blit(warpstar,warpstarbox)
        if warpstarbox.x>=1220:
            warpstarbox.x=-50
            screen.blit(warpstar,warpstarbox)
        if warpstarbox.colliderect(playerbox):
            gameover=True
            exit()
            


    for warpstarbox2 in warpstar2list:
        warpstarbox2.move_ip(2,0)
        screen.blit(warpstar,warpstarbox2)
        if warpstarbox2.x>=1220:
            warpstarbox2.x=-50
            screen.blit(warpstar,warpstarbox2)
        if warpstarbox2.colliderect(playerbox):
            ameover=True
            exit()


    for starcutterbox in starcutterlist:
        starcutterbox.move_ip(-2,0)
        screen.blit(starcutter,starcutterbox)
        if starcutterbox.x<=-130:
            starcutterbox.x=1200
            screen.blit(starcutter,starcutterbox)
        if starcutterbox.colliderect(playerbox):
            gameover=True
            exit()


    for halberdbox in halberdlist:
        halberdbox.move_ip(1,0)
        screen.blit(halberd,halberdbox)
        if halberdbox.x>=1230:
            halberdbox.x=-140
            screen.blit(halberd,halberdbox)
        if halberdbox.colliderect(playerbox):
            gameover=True
            exit()


    
    
            
       
            
    
    
    for e in event.get():
        if e.type==KEYDOWN:
            if e.key==K_LEFT:
                dx=-2
            if e.key==K_RIGHT:
                dx=2
            if e.key==K_UP:
                dy=-2
            if e.key==K_DOWN:
                dy=2
        if e.type==KEYUP:
            if e.key==K_LEFT or e.key==K_RIGHT:
                dx=0
            if e.key==K_UP or e.key==K_DOWN:
                dy=0
                
    playerbox.move_ip(dx,dy) 
    screen.blit(player,playerbox)
    display.flip()
    

