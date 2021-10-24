#pip install pygame
#pip install pillow
import pygame
import time
import random
from PIL import Image
from pygame import mixer
l=["pirates.mp3","bond.mp3"]
print("1) Pirates of the Caribbean theme song")
print("2) James Bond theme song")
ch=int(input())
if ch==1:
    song=l[0]
elif ch==2:
    song=l[1]
else:
    print("Invalid choice")
    print("Using default song - Pirates of the Caribbean")
    song=l[0]
mixer.init()
mixer.music.load(song)
pygame.init() #manadatory statement for python game initialization

display_width=800
display_height=600

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
block_color=(225,0,0)

gameDisplay=pygame.display.set_mode((display_width,display_height))
clock=pygame.time.Clock() #set the clock for ur game (frames per sec)

#make a game loop

basewidth = 50
hsize=50
img = Image.open('racecar.png')
#wpercent = (basewidth/float(img.size[0]))
#hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('rcar.jpg')
carImg=pygame.image.load('rcar.jpg')
car_width=50

def quit_game():
    pygame.quit()
    quit()
    
def things_dodged(count):
    font=pygame.font.SysFont(None,25)
    text=font.render("Dodged: "+str(count),True,black)
    gameDisplay.blit(text,(0,0))
    
def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(txt,font):
    textSurface=font.render(txt,True,black)
    return textSurface,textSurface.get_rect()

def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect=text_objects(text,largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()
    
def crash():
    message_display('You Crashed')
    
def game_loop():
    mixer.music.play(999)
    x=(display_width*0.45)
    y=(display_height*0.8)
    
    x_change=0
    
    thing_startx=random.randrange(0,display_width)
    thing_starty=-600
    thing_speed=4
    thing_width=50
    thing_height=50
    
    dodged=0
    
    gameExit=False
    while not gameExit:
        for event in pygame.event.get(): #this gets all the events about the game where your mouse is, where it is pointing, keys pressed etc
            if event.type == pygame.QUIT:
                quit_game()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                elif event.key==pygame.K_RIGHT:
                    x_change=5
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
        x+=x_change
        
        gameDisplay.fill(white)
        
        #things(thingx,thingy,thingw,thingh,color)
        things(thing_startx,thing_starty,thing_width,thing_height,block_color)
        thing_starty+=thing_speed
        car(x,y)
        things_dodged(dodged)
        
        if x>display_width-car_width or x<0:
            crash()
        
        if(thing_starty>display_height):
            thing_starty=0-thing_height
            thing_startx=random.randrange(0,display_width)
            dodged+=1
            thing_speed+=1
            thing_width+=(dodged*1.2)
            
        if y<thing_starty+thing_height:
            if x>thing_startx and x<thing_startx+thing_width or x+car_width>thing_startx and x+car_width<thing_startx+thing_width:
                crash()
        pygame.display.update()
        clock.tick(60) #frames per sec
        
game_loop()
quit_game()
