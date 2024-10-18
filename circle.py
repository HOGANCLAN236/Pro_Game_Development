import pygame 

pygame.init()

black = 0, 0, 0
red = 255, 0, 0

screen = pygame.display.set_mode((600, 600))

screen.fill(black)

pygame.display.update()

pygame.draw.circle(screen, red, (100, 200), 15, 10)

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False