import pygame
from pygame.locals import *
import time
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

player_x = 200
player_y = 200

#        Up    Left   Down   Right
Keys = [False, False, False, False]

player = pygame.image.load("Images/ship.png")

bg = pygame.image.load("Images/space_bg.png")

while player_y < 600:
    screen.blit(bg, (0, 0))
    screen.blit(player, (player_x, player_y))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        #check if any keyboard button is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                Keys[0] = True
            if event.key == K_a:
                Keys[1] = True
            if event.key == K_s:
                Keys[2] = True
            if event.key == K_d:
                Keys[3] = True
        
        #check if any keyboard button is released
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                Keys[0] = False
            if event.key == K_a:
                Keys[1] = False
            if event.key == K_s:
                Keys[2] = False
            if event.key == K_d:
                Keys[3] = False

    #adding movement
    if Keys[0]:
        if player_y > 0:
            player_y -= 7
    
    if Keys[2]:
        if player_y < 536:
            player_y += 7
    
    if Keys[1]:
        if player_x > 0:
            player_x -= 2
    
    if Keys[3]:
        if player_x < 536:
            player_x += 2
    
    player_y += 5 #gravity
    time.sleep(0.05)

print("Game Over! :(")
    