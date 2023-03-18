import pygame
import time 
import random
pygame.init()
display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
grey = (166,166,166)

#####
carImg = pygame.image.load('racecar.png')

def car(x,y):
    gameDisplay.blit(carImg,(x,y))
car_width = 75

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
########

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('The Game')
clock = pygame.time.Clock()

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("advanced_pixel-7.ttf",30)
    textSurf, textRect = text_objects(msg, smallText,black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def game_intro():

    intro = True
    message = "Python"
    font = pygame.font.Font('advanced_pixel-7.ttf',45)
    snip = font.render('',True,'white')
    counter = 0
    speed = 1
    done = False

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(black)
        clock.tick(60)
        pygame.draw.rect(gameDisplay,'black',[0,300,800,200])
        if counter <speed*len(message):
            counter +=1
        elif counter >= speed*len(message):
            done = True
        snip = font.render(message[0:counter//speed], True, 'white')
        gameDisplay.blit(snip,(360,210))
        pygame.display.flip()

        button("GO!",350,280,100,50,white,grey,screen1)
        #button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def screen1():
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, white, pygame.Rect(300, 200, 60, 60))
        largeText = pygame.font.SysFont("padauk",115)
        TextSurf, TextRect = text_objects("Python", largeText,grey)
        TextRect.center = ((display_width/2),210)
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(30)


game_intro()
pygame.quit()
quit()