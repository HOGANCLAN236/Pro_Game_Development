import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

black = 0, 0, 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Greeting Card")

bg = pygame.image.load("Images/bg.jpg").convert()
image = pygame.transform.scale(bg, (WIDTH, HEIGHT))
pygame.display.update()

while True:
    font = pygame.font.Font("freesansbold.ttf", 72) # Times New Roman
    text = font.render("Happy", True, (0, 0, 0))
    text2 = font.render("Birthday", True, (0, 0, 0))
    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))
    screen.blit(text, (190, 150))
    screen.blit(text2, (165, 225))
    pygame.display.update()
    time.sleep(2)


    birthdaycake = pygame.image.load("Images/birthdaycake.jpg")
    #cakeimage = pygame.transform.scale(birthdaycake, (WIDTH, HEIGHT))
    font2 = pygame.font.SysFont("Arial", 36)
    text3 = font2.render("Wishing you a bright future ahead!", True, (0, 0, 0))
    screen.fill((255, 255, 255))
    screen.blit(birthdaycake, (0, 0))
    screen.blit(text3, (30, 30))
    pygame.display.update()
    time.sleep(2)

    present = pygame.image.load("Images/pressent.jpg")
    screen.fill((255, 255, 255))
    screen.blit(present, (0, 0))
    pygame.display.update()
    time.sleep(2)



