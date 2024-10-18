import pygame 

pygame.init()

black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

screen = pygame.display.set_mode((600, 600))

screen.fill(black)

pygame.display.update()

class rectangle():
    def __init__(self, color, dimensions):
        self.rect_surf = screen
        self.rect_dimensions = dimensions
        self.rect_color = color
    
    def draw(self):
        self.Draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions)

red_rect = rectangle(red, (50, 20, 120, 75))
blue_rect = rectangle(blue, (150, 200, 175, 100))
green_rect = rectangle(green, (300, 400, 200, 120))

red_rect.draw()
blue_rect.draw()
green_rect.draw()

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


