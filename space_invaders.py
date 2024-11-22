import pygame
import os

pygame.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

White = (255, 255, 255)
Black = (0, 0, 0)
Red_color = (255, 0, 0)
Yellow_color = (255, 255, 0)

border = pygame.Rect(WIDTH // 2 -5, 0, 10, HEIGHT)
healthFont = pygame.font.SysFont("comicsans", 40)
WinnerFont = pygame.font.SysFont("comicsans", 100)

pygame.display.update()

FPS = 60
vel = 5
bullet_vel = 7
max_bullets = 3
spaceship_width, spaceship_height = 55, 40

yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2

yellow_spaceship_img = pygame.image.load("Assets/Spaceship_yellow.png")
red_spaceship_img = pygame.image.load("Assets/Spaceship_red.png")

yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship_img, (spaceship_width, spaceship_height)), 90)
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship_img, (spaceship_width, spaceship_height)), 270)

space = pygame.transform.scale(pygame.image.load("Assets\SpaceBG.png"), (WIDTH, HEIGHT))


pygame.display.update()

def draw_window(Red, Yellow, Red_color, Yellow_color, Red_Bullets, Yellow_bullets, Red_health, Yellow_health):
    screen.blit(space, (0, 0))
    pygame.draw.rect(screen, Black, border)

    red_health_text = healthFont.render("Health: " + str(Red_health), 1, White)
    Yellow_health_text = healthFont.render("Health: " + str(Yellow_health), 1, White)

    screen.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    screen.blit(Yellow_health_text, (10, 10))

    screen.blit(yellow_spaceship, (Yellow.x, Yellow.y))
    screen.blit(red_spaceship, (Red.x, Red.y))

    for bullet in Red_Bullets:
        pygame.draw.rect(screen, Red_color, bullet)
    
    for bullet in Yellow_bullets:
        pygame.draw.rect(screen, Yellow_color, bullet)

    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - vel > 0:
        yellow.x -= vel
    if keys_pressed[pygame.K_d] and yellow.x + vel + yellow.width < border.x:
        yellow.x += vel
    if keys_pressed[pygame.K_w] and yellow.y - vel > 0:
        yellow.y -= vel
    if keys_pressed[pygame.K_s] and yellow.y + vel + yellow.height < HEIGHT - 15:
        yellow.y += vel

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_j] and red.x - vel > border.x + border.width:
        red.x -= vel
    if keys_pressed[pygame.K_l] and red.x + vel + red.width < WIDTH:
        red.x += vel
    if keys_pressed[pygame.K_i] and red.y - vel > 0:
        red.y -= vel
    if keys_pressed[pygame.K_k] and red.y + vel + red.height < HEIGHT - 15:
        red.y += vel

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += bullet_vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= bullet_vel
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WinnerFont.render(text, 1, White)
    screen.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2,
                             HEIGHT / 2 - draw_text.get_height() / 2))
    
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    red = pygame.Rect(700, 300, spaceship_width, spaceship_height)

    yellow = pygame.Rect(100, 300, spaceship_width, spaceship_height)
    
    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < max_bullets:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.width // 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                
                if event.key == pygame.K_RCTRL and len(red_bullets) < max_bullets:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 -2, 10, 5)
                    red_bullets.append(bullet)
            
            if event.type == red_hit:
                red_health -= 1
            if event.type == yellow_hit:
                yellow_health -= 1
            
        winner_text = ""

        if red_health <= 0:
            winner_text = "Yellow Wins"
        if yellow_health <= 0:
            winner_text = "Red Wins"
        
        if winner_text != "":
            draw_winner(winner_text)
            break
        
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, Red_color, Yellow_color, red_bullets, yellow_bullets, red_health, yellow_health)

main()

                 

