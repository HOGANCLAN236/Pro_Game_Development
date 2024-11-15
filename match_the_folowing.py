import pygame
import random 
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

img_SS = pygame.image.load("Images/SS.png")
img_TR = pygame.image.load("Images/TR.png")
img_LD = pygame.image.load("Images/LD.png")
img_CC = pygame.image.load("Images/CC.jpg")

pos1 = (100, 100)
pos2 = (100, 200)
pos3 = (100, 300)
pos4 = (100, 400)

txt1 = (300, 125)
txt2 = (300, 225)
txt3 = (300, 325)
txt4 = (300, 425)

screen.fill((255, 255, 255))

pygame.display.update()

sprites = ["SS", "TR", "LD", "CC"]
txt_list = ["SS", "TR", "LD", "CC"]
random.shuffle(sprites)
random.shuffle(txt_list)

ss = 0
tr = 0
ld = 0
cc = 0

ss1 = 0
tr1 = 0
ld1 = 0
cc1 = 0

ss2 = 0
tr2 = 0
ld2 = 0
cc2 = 0

def draw_sprites():
    global ss, tr, cc, ld

    if sprites[0] == "SS":
        ss = screen.blit(img_SS, pos1)

    if sprites[0] == "TR":
        tr = screen.blit(img_TR, pos1)

    if sprites[0] == "LD":
        ld = screen.blit(img_LD, pos1)

    if sprites[0] == "CC":
        cc = screen.blit(img_CC, pos1)


    if sprites[1] == "SS":
        ss= screen.blit(img_SS, pos2)

    if sprites[1] == "TR":
        tr = screen.blit(img_TR, pos2)

    if sprites[1] == "LD":
        ld = screen.blit(img_LD, pos2)

    if sprites[1] == "CC":
        cc= screen.blit(img_CC, pos2)


    if sprites[2] == "SS":
        ss = screen.blit(img_SS, pos3)

    if sprites[2] == "TR":
        tr = screen.blit(img_TR, pos3)

    if sprites[2] == "LD":
        ld = screen.blit(img_LD, pos3)

    if sprites[2] == "CC":
        cc= screen.blit(img_CC, pos3)


    if sprites[3] == "SS":
        ss = screen.blit(img_SS, pos4)

    if sprites[3] == "TR":
        tr = screen.blit(img_TR, pos4)

    if sprites[3] == "LD":
        ld = screen.blit(img_LD, pos4)

    if sprites[3] == "CC":
        cc= screen.blit(img_CC, pos4)

    pygame.display.update()

def draw_text():
    global txt_list, ss1, tr1, cc1, ld1, ss2, cc2, ld2, tr2
    if txt_list[0] == "SS":
        font = pygame.font.Font("freesansbold.ttf", 32) # Times New Roman
        ss1 = font.render("Subway Surfers", True, (0, 0, 0))
        ss2 = screen.blit(ss1, txt1)

    if txt_list[0] == "TR":
        font = pygame.font.Font("freesansbold.ttf", 32) # Times New Roman
        tr1 = font.render("Temple Run", True, (0, 0, 0))
        tr2 = screen.blit(tr1, txt1)

    if txt_list[0] == "LD":
        font = pygame.font.Font("freesansbold.ttf", 32) # Times New Roman
        ld1 = font.render("Ludo", True, (0, 0, 0))
        ld2 = screen.blit(ld1, txt1)

    if txt_list[0] == "CC":
        font = pygame.font.Font("freesansbold.ttf", 32) # Times New Roman
        cc1 = font.render("Candy Crush", True, (0, 0, 0))
        cc2 = screen.blit(cc1, txt1)

    
    if txt_list[1] == "SS":
        font = pygame.font.Font("freesansbold.ttf", 32) # Times New Roman
        ss1 = font.render("Subway Surfers", True, (0, 0, 0))
        ss2 = screen.blit(ss1, txt2)

    if txt_list[1] == "TR":
        font = pygame.font.Font("freesansbold.ttf", 32) # Times New Roman
        tr1 = font.render("Temple Run", True, (0, 0, 0))
        tr2 = screen.blit(tr1, txt2)

    if txt_list[1] == "LD":
        font = pygame.font.Font("freesansbold.ttf", 32) # Times New Roman
        ld1 = font.render("Ludo", True, (0, 0, 0))
        ld2 = screen.blit(ld1, txt2)

    if txt_list[1] == "CC":
        font = pygame.font.Font("freesansbold.ttf", 32) # Times New Roman
        cc1 = font.render("Candy Crush", True, (0, 0, 0))
        cc2 = screen.blit(cc1, txt2)


    if txt_list[2] == "SS":
        font = pygame.font.Font("freesansbold.ttf", 32) # Times New Roman
        ss1 = font.render("Subway Surfers", True, (0, 0, 0))
        ss2 = screen.blit(ss1, txt3)

    if txt_list[2] == "TR":
        font = pygame.font.Font("freesansbold.ttf", 32) # Times New Roman
        tr1 = font.render("Temple Run", True, (0, 0, 0))
        tr2 = screen.blit(tr1, txt3)

    if txt_list[2] == "LD":
        font = pygame.font.Font("freesansbold.ttf", 32) # Times New Roman
        ld1 = font.render("Ludo", True, (0, 0, 0))
        ld2 = screen.blit(ld1, txt3)

    if txt_list[2] == "CC":
        font = pygame.font.Font("freesansbold.ttf", 32) # Times New Roman
        cc1 = font.render("Candy Crush", True, (0, 0, 0))
        cc2 = screen.blit(cc1, txt3)


    if txt_list[3] == "SS":
        font = pygame.font.Font("freesansbold.ttf", 32) # Times New Roman
        ss1 = font.render("Subway Surfers", True, (0, 0, 0))
        ss2 = screen.blit(ss1, txt4)

    if txt_list[3] == "TR":
        font = pygame.font.Font("freesansbold.ttf", 32) # Times New Roman
        tr1 = font.render("Temple Run", True, (0, 0, 0))
        tr2 = screen.blit(tr1, txt4)

    if txt_list[3] == "LD":
        font = pygame.font.Font("freesansbold.ttf", 32) # Times New Roman
        ld1 = font.render("Ludo", True, (0, 0, 0))
        ld2 = screen.blit(ld1, txt4)

    if txt_list[3] == "CC":
        font = pygame.font.Font("freesansbold.ttf", 32) # Times New Roman
        cc1 = font.render("Candy Crush", True, (0, 0, 0))
        cc2 = screen.blit(cc1, txt4)
    
    pygame.display.update()


draw_sprites()
draw_text()

clicked = False
clicke1 = False
clicke2 = False
clicke3 = False

int_x = 0
int_y = 0
x = 0
y = 0
init_x = 0
init_y = 0
end_x = 0
end_y = 0

ss_done = False
tr_done = False
ld_done = False
cc_done = False

while True:
    ss_rect = img_SS.get_rect()

    if ld_done == True and cc_done == True and tr_done == True and ss_done == True:
        print("you win")
        screen.fill((255, 255, 255))
        font = pygame.font.Font("freesansbold.ttf", 52) # Times New Roman
        tr1 = font.render("You Win!", True, (0, 0, 0))
        tr2 = screen.blit(tr1, (175, 50))
        pygame.display.update()
                
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            int_x, int_y = event.pos
            if ss_done == False:
                if pygame.Rect.collidepoint(ss, int_x, int_y) and clicked == False:
                    print("CLICKED YIPPEE")
                    init_x = int_x
                    init_y = int_y
                    x = init_x
                    y = init_y
                    print(str(init_x))
                    clicked = True
                    

                if pygame.Rect.collidepoint(ss2, int_x, int_y) and clicked == True:
                    print("clicked")
                    end_x = int_x
                    end_y = int_y
                    print(str(init_x))
                    pygame.draw.line(screen, (0, 0, 0), (x, y), (end_x, end_y), 3)
                    pygame.display.update()
                    clicked = False
                    ss_done = True
            if ld_done == False:
                if pygame.Rect.collidepoint(ld, int_x, int_y) and clicke1 == False:
                    print("CLICKED YIPPEE")
                    init_x = int_x
                    init_y = int_y
                    x = init_x
                    y = init_y
                    print(str(init_x))
                    clicke1 = True
                    

                if pygame.Rect.collidepoint(ld2, int_x, int_y) and clicke1 == True:
                    print("clicked")
                    end_x = int_x
                    end_y = int_y
                    print(str(init_x))
                    pygame.draw.line(screen, (0, 0, 0), (x, y), (end_x, end_y), 3)
                    pygame.display.update()
                    clicke1 = False
                    ld_done = True
            if tr_done == False:
                if pygame.Rect.collidepoint(tr, int_x, int_y) and clicke2 == False:
                    print("CLICKED YIPPEE")
                    init_x = int_x
                    init_y = int_y
                    x = init_x
                    y = init_y
                    print(str(init_x))
                    clicke2 = True
                    

                if pygame.Rect.collidepoint(tr2, int_x, int_y) and clicke2 == True:
                    print("clicked")
                    end_x = int_x
                    end_y = int_y
                    print(str(init_x))
                    pygame.draw.line(screen, (0, 0, 0), (x, y), (end_x, end_y), 3)
                    pygame.display.update()
                    clicke2 = False
                    tr_done = True
            if cc_done == False:
                if pygame.Rect.collidepoint(cc, int_x, int_y) and clicke3 == False:
                    print("CLICKED YIPPEE")
                    init_x = int_x
                    init_y = int_y
                    x = init_x
                    y = init_y
                    print(str(init_x))
                    clicke3 = True
                    

                if pygame.Rect.collidepoint(cc2, int_x, int_y) and clicke3 == True:
                    print("clicked")
                    end_x = int_x
                    end_y = int_y
                    print(str(init_x))
                    pygame.draw.line(screen, (0, 0, 0), (x, y), (end_x, end_y), 3)
                    pygame.display.update()
                    clicke3 = False
                    cc_done = True
            
 

            
                
                



        # if event.type == pygame.MOUSEBUTTONUP:
        #     x, y = event.pos
        #     if pygame.Rect.collidepoint():

                
