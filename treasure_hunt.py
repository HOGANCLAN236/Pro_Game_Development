import pygame
import random
from pygame.locals import *
import time

#change bg
def changebackground(img):
    bg1 = pygame.image.load(img)
    #setting the background size
    bg = pygame.transform.scale(bg1, (WIDTH, HEIGHT))
    screen.blit(bg, (0, 0))

#initializing pygame
pygame.init()
pygame.display.set_caption("Treasure Hunt")

#set width and height of screen
WIDTH = 900
HEIGHT = 700
screen = pygame.display.set_mode([WIDTH, HEIGHT])

#setting up player sprite
class Pirate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/pirate.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 100))
        self.rect = self.image.get_rect()

#setting up stone sprite
class Stone(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

#stone has multiple images so setting them up in a list
images = ["Images/stone1.png", "Images/stone2.png", "Images/stone3.png"]

#create sprite groups
stone_list = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

#create stone sprites
for i in range(100):
    stone = Stone(random.choice(images))
    #setting up random location
    stone.rect.x = random.randrange(WIDTH)
    stone.rect.y = random.randrange(HEIGHT)
    #adding stone to list
    stone_list.add(stone)
    allsprites.add(stone)

#create pirate
pirate = Pirate()
allsprites.add(pirate)

#game essential variables
white = (255, 255, 255)
red = (255, 0, 0)

playing = True
score = 0
#clock
clock = pygame.time.Clock()
start_time = time.time()
my_font = pygame.font.SysFont("Times New Roman", 40)
timing_font = pygame.font.SysFont("Times New Roman", 70)
text = my_font.render("Score =" + str(0), True, white)

while playing:
    clock.tick(30)
    
    #quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    time_elapsed = time.time() - start_time
    if time_elapsed >= 30:
        text = my_font.render(" Game Over ", True, white)
        screen.blit(text, (300, 40))
    else:
        changebackground("Images/space_bg.png")
    
        #move the glove as per key pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if pirate.rect.y > 0:
                pirate.rect.y -= 5

        if keys[pygame.K_DOWN]:
            if pirate.rect.y < 630:
                pirate.rect.y += 5
        
        if keys[pygame.K_LEFT]:
            if pirate.rect.x > 0:
                pirate.rect.x -= 5

        if keys[pygame.K_RIGHT]:
            if pirate.rect.x < 850:
                pirate.rect.x += 5
        
         #check if stone and pirate have collided
        stone_hit_list = pygame.sprite.spritecollide(pirate, stone_list, True)

        #check the list of collisions
        for stone in stone_hit_list:
            score += 1
            text = my_font.render(f"Score ={score}" , True, white)

        #printing the score on screen
        screen.blit(text, (730, 80))

        #draw all sprites
        allsprites.draw(screen)

    pygame.display.update()
pygame.quit()

