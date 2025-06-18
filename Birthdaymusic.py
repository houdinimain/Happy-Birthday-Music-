import pygame
import time 

pygame.init()
pygame.mixer.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Happy Birthday Card ")

card = pygame.image.load("Happy Birthday Card\image1.jpg") 

finalcard = pygame.transform.scale(card,(WIDTH,HEIGHT))
birthdaysound = pygame.mixer.Sound("Happy Birthday Card/happybirthday.mp3")


run = True

while run:
    for i in pygame.event.get():
          if i.type == pygame.QUIT:
             run = False
    font =  pygame.font.SysFont("Endless Script",60)
    text = font.render("Happy Birthday",True,"Black")
    screen.blit(finalcard,(0,0))

    screen.blit(text,(160,300))
    birthdaysound.play()
    pygame.display.update()
    time.sleep(2)
    image2 = pygame.image.load("Happy Birthday Card\image2.jpg")

  
    font2 =  pygame.font.SysFont("Endless Script",60)
    text2 = font.render("happy birthday to you",True,"Black")
    screen.blit(image2,(0,0))

    screen.blit(text2,(100,500))

    pygame.display.update()
    time.sleep(2)


    pygame.display.update()
    time.sleep(2)
    image3 = pygame.image.load("Happy Birthday Card\image3.jpg")



    font3 =  pygame.font.SysFont("Endless Script",60)
    text3 = font.render("Have a good birthday",True,"Black")
    screen.blit(image3,(0,0))

    screen.blit(text3,(100,50))

    pygame.display.update()
    time.sleep(2)

