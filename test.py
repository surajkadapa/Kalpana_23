#import pygame
# from pygame import mixer

#pygame.init()


# white= (255,255,255)
# x=400
# y=400

# """font = pygame.font.Font('freesansbold.ttf',24)
# text=font.render('learn python',True,white)
# textRect = text.get_rect()
# textRect.center=(x//2,y//2)"""

# font = pygame.font.Font('freesansbold.ttf',24)

# #create the screen
# screen = pygame.display.set_mode((x, y))

# #background sound
# #mixer.music.load('sound1.mp3')
# #mixer.music.play(-1)

# timer = pygame.time.Clock() - clock
# message = 'learn python with us'
# snip= font.render('',True,'white')
# counter= 0
# speed = 4
# done=False

# #infinite game loop so window doesn't close until we quit
# running= True
# while running:
#     screen.fill((3,3,3))
#     timer.tick(60)
#     pygame.draw.rect(screen,'black',[0,300,800,200])
#     if counter < speed*len(message):
#         counter += 1
#     elif counter>= speed*len(message):
#         done = True
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running= False
#     snip= font.render(message[0:counter//speed], True, 'white')
#     screen.blit(snip,(10,310))
#     pygame.display.flip()
# pygame.quit()


import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')

def car(x,y):
    gameDisplay.blit(carImg,(x,y))



def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)
        car(x,y)

        if x > display_width - car_width or x < 0:
            gameExit = True
            
        
        pygame.display.update()
        clock.tick(60)



game_loop()
pygame.quit()
quit()
