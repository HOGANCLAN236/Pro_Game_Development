import pygame
import random
from pygame.locals import *
import time

#change background
def changeBackground(img):
    # Change the background 
    background = pygame.image.load(img)
    #set its size
    bg = pygame.transform.scale(background, (screen_width,screen_height))
    screen.blit(bg,(0,0))
  
 

# Initialize Pygame
pygame.init()
pygame.display.set_caption('Recycle Marathon')
# Set the height and width of the screen
screen_width=900
screen_height=700
screen = pygame.display.set_mode([screen_width,screen_height])

#Player sprite (Bin)
class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Images/bin.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,60))
        self.rect = self.image.get_rect()

#Recyclable sprite
class Recyclable(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()


#Non_recyclable sprite
class Non_recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Images/plastic.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()

#List of images for Recyclable class
images=["Images/item1.png","Images/item2.png","Images/item3.png"]
  

#create sprite groups
item_list = pygame.sprite.Group()
allsprites= pygame.sprite.Group()
plastic_list=pygame.sprite.Group()

plastic_piece = []

#create item sprites
for i in range(65):
    item = Recyclable(random.choice(images)) 
    # Set a random location for the item
    item.rect.x = random.randrange(0 + item.rect.width, screen_width - item.rect.width)
    item.rect.y = random.randrange(0 + item.rect.height, screen_height - item.rect.height)
    # Add to item list
    item_list.add(item)
    allsprites.add(item)

#create plastic
for i in range(20):
    plastic=Non_recyclable()
    # Set a random location for the plastic
    plastic.rect.x = random.randrange(0 + item.rect.width, screen_width - item.rect.width)
    plastic.rect.y = random.randrange(0 + item.rect.height, screen_height - item.rect.height)

    # Add to plastic list
    plastic_list.add(plastic)
    allsprites.add(plastic)
    plastic_piece.append(plastic)

 
# Create bin
bin = Bin()
allsprites.add(bin)



#initialize essential variables
# Define colour
WHITE = (255, 255, 255)
RED=(255,0,0)

playing=True
score = 0
#clock 
clock = pygame.time.Clock()
#start time
start_time = time.time()
#font to print score on screen 
myFont=pygame.font.SysFont("Times New Roman",22)
timingFont=pygame.font.SysFont("Times New Roman",22)
text=myFont.render("Score ="+str(0),True,WHITE)


# -------- Main Program Loop -----------
while playing:
    #refresh 60 times in a second
    #can be used to control speed
    clock.tick(30)
        
    #quit the game
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            playing=False
    
    #check if time>60 secs
    timeElapsed=time.time()-start_time
    if timeElapsed >=60:        
        if score>50:
            text=myFont.render("    Bin loot successful    ",True,RED)
            # Change the background 
            changeBackground("winscreen.jpg")
        else:
            text=myFont.render("Better luck next time",True,WHITE)
            # Change the background 
            changeBackground("losescreen.jpg")
        screen.blit(text,(250,40))        
    else:
               
        # Change the background 
        changeBackground("Images/bground.png")
        countDown=timingFont.render("Time Left:"+str(60-int(timeElapsed)),True,WHITE)
        screen.blit(countDown,(20,10))
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: # UP
            if bin.rect.y> 0:     
                 bin.rect.y -= 5
        if keys[pygame.K_s] : # DOWN
            if bin.rect.y <630:
                bin.rect.y += 5 
        
        if keys[pygame.K_a] : # LEFT
            if bin.rect.x> 0:    
                 bin.rect.x -= 5 
        
        if keys[pygame.K_d] : # RIGHT
             if bin.rect.x <850:
                 bin.rect.x += 5  
         
        
     
        # See if item and bin has collided
        item_hit_list = pygame.sprite.spritecollide(bin, item_list, True)
        plastic_hit_list=pygame.sprite.spritecollide(bin, plastic_list, True)

     
        # Check the list of collisions.
        for item in item_hit_list:
            score += 1
            #print(score)
            text=myFont.render("Score ="+str(score),True,WHITE)
        for plastic in plastic_hit_list:
            score -= 5
            #print(score)
            text=myFont.render("Score ="+str(score),True,WHITE)

        # print the score on screen
        screen.blit(text,(20,50))

             
        # Draw all the spites
        allsprites.draw(screen)
     
        
    pygame.display.update()
     
        
pygame.quit()