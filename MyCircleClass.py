import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)

screen.fill(white)

class MyCircle():
    def __init__(self, color, pos, rad, width = 0):
        self.color = color
        self.pos = pos
        self.rad = rad
        self.width = width
        self.scrn = screen
    
    def draw(self):
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.width)

    def grow(self, x):
        self.rad += x
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.width)

position = (300, 300)
radius = 50
width = 2
pygame.draw.circle(screen, red, position, radius, width)

pygame.display.update()

blue_circle = MyCircle(blue, position, radius + 60)
red_circle = MyCircle(red, position, radius + 40)
green_circle = MyCircle(green, position, radius, 5)
yellow_circle = MyCircle(yellow, position, 20)

while 1:
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            blue_circle.draw()
            red_circle.draw()
            yellow_circle.draw()
            green_circle.draw()
        elif (event.type == pygame.MOUSEBUTTONUP):
            blue_circle.grow(2)
            red_circle.grow(2)
            yellow_circle.grow(2)
            green_circle.grow(2)
        elif (event.type == pygame.MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            blackCircle = MyCircle(black, pos, 5)
            blackCircle.draw()
            pygame.display.update()
        