import pygame

pygame.init()

WIDTH = 700
HEIGHT = 500

caption = "Rocket in Space"

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(caption)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/ship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 100))
        self.rect = self.image.get_rect()

    # move the sprite based on key presses
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_w]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_a]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_s]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_d]:
            self.rect.move_ip(5, 0)
    
        # keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

sprites = pygame.sprite.Group()

def start_game():
    player = Player()
    sprites.add(player)

    #start game loop
    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                exit(0)
            
        # get the set of keys pressed and check for user input 
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        # add bg image
        
        screen.blit(pygame.image.load("Images/space_bg.png"), (0, 0))

        # draw the sprites

        sprites.draw(screen)

        pygame.display.update()

start_game()




    
        
    
        

