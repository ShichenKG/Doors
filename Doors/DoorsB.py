######################################
# Shane Donivan
# PM Class
# Junior
# 5/0/21
# EOY Assignment - DoorsOS
# A Bootleg OS System, meant to be fun
#######################################
import pygame, sys, os, time
from pygame.locals import *


#####################################################
#
# Classes
#
#####################################################
# Does a flash to turn off the Game
class QuitAnim(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('an/B1.png'))
        self.sprites.append(pygame.image.load('an/B2.png'))
        self.sprites.append(pygame.image.load('an/B3.png'))
        self.sprites.append(pygame.image.load('an/B4.png'))
        self.sprites.append(pygame.image.load('an/B5.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self,speed):
        self.current_sprite += speed

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 4

        self.image = self.sprites[int(self.current_sprite)]


# Isn't Used. Yet.
class Zoom(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('an/zoom0.png'))
        self.sprites.append(pygame.image.load('an/zoom1.png'))
        self.sprites.append(pygame.image.load('an/zoom2.png'))
        self.sprites.append(pygame.image.load('an/zoom3.png'))
        self.sprites.append(pygame.image.load('an/zoom4.png'))
        self.sprites.append(pygame.image.load('an/zoom5.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self, speed):
        self.current_sprite += speed

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 10

        self.image = self.sprites[int(self.current_sprite)]


# Adds 1 frame per time clicked on  the "Click me" button
class dooradd(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.sprites = LoadDir("an/add/")
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def add(self):
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 88
    def update(self):
        self.image = self.sprites[self.current_sprite]
        screen.blit(self.image, (0, 0))


# Specifically controls the "Click Me" Button
class ClassHover(pygame.sprite.Sprite):
    def __init__(self, pos, image1, image2, image3,event=None):
        super().__init__()
        self.pos = pos
        self.img1 = pygame.image.load(image1).convert_alpha()
        self.img2 = pygame.image.load(image2).convert_alpha()
        self.img3 = pygame.image.load(image3).convert_alpha()
        self.img_mask = pygame.mask.from_surface(self.img1)
        self.rect = self.img1.get_rect(topleft=self.pos)
        self.cur_img = self.img1

        self.clicking = False
        self.click = False

    def update(self,click):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            # Click
            if click and self.clicking:
                screen.blit(self.img3, self.pos)
            # Click Hover
            elif click:
                screen.blit(self.img3, self.pos)
                self.clicking = True
                Score.inc()
                door.add()
            # Hover
            else:
                screen.blit(self.img2, self.pos)
                self.clicking = False
        # None
        else:
            screen.blit(self.img1, self.pos)
            self.clicking = False


# Makes the Score add 1 per "Click me" button click
class ClassScore():
    def __init__(self):
        self.value = 0

    def inc(self, i=1):
        self.value += i

    def __str__(self):
        return str(self.value)


#####################################################
#
# Functions #
#
# Loading Images - LoadDir
# Creates Buttons that switch between 2 images - Hover
# Plays a Quit Animation - quitanim
#
#####################################################
def LoadDir(dir):
    l = []
    for i in os.listdir(dir):
        l.append(pygame.image.load(dir + i))
    return l


def Hover(image1,image2,x,y):
    mouse_pos = pygame.mouse.get_pos()

    l = pygame.sprite.Sprite
    l.img1 = pygame.image.load(image1).convert_alpha()
    l.img2 = pygame.image.load(image2).convert_alpha()
    l.img_mask = pygame.mask.from_surface(l.img1)
    l.img_rect = l.img1.get_rect(topleft = (x,y))
    l.cur_img = l.img1

    if l.img_rect.collidepoint(mouse_pos):
        l.cur_img = l.img2
        screen.blit(l.cur_img, (x, y))
    else:
        l.cur_img = l.img1
        screen.blit(l.cur_img, (x,y))


def quitanim():
    isquitting = True
    CLOSE = pygame.USEREVENT + 1
    pygame.time.set_timer(CLOSE, 500)
    # Event Loop / Game Loop
    while isquitting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == CLOSE:
                pygame.quit()
                sys.exit()

        # Draw stuff
        screen.fill((240,240,240))
        moving_sprites.draw(screen)
        moving_sprites.update(0.40)
        pygame.display.flip()
        clock.tick(60)


#####################################################
#
# Game Screens
#
#####################################################
def Title():
    title = True
    background = pygame.image.load('mmr.png').convert()
    start = pygame.image.load('DL1.png').convert_alpha()
    quit = pygame.image.load('P1.png').convert_alpha()

    # Event Loop / Game Loop
    while title:
        screen.blit(background, (0, 0))
        Hover(quit1,quit2 ,325, 175)
        Hover(start1,start2,690,190)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start.get_rect(topleft=(690,190)).collidepoint(mouse_pos):
                    title = False
                    Mainscreen()
                if quit.get_rect(topleft=(325,175)).collidepoint(mouse_pos):
                    title = False
                    quitanim()

        clock.tick(60)
        pygame.display.flip()


# This is how you navigate between everything. It's like the Hub Area
def Mainscreen():
    main = True
    clicked = 1
    screen.fill((73, 166, 160))
    trash = pygame.image.load('Trash.png').convert_alpha()
    internet = pygame.image.load('E.png').convert_alpha()
    shop = pygame.image.load('Sh1.png').convert_alpha()
    doorgame = pygame.image.load('DoorG1.png').convert_alpha()
    bar = pygame.image.load('taskbar.png').convert_alpha()
    background = pygame.image.load('background.png').convert_alpha()
    start = pygame.image.load('dm1.png').convert_alpha()
    pong = pygame.image.load('pong1.png').convert_alpha()

    myFont = pygame.font.SysFont("Madeupfont", 35)
    Time_HourMin = myFont.render(time.strftime('%H:%M'), 1, BLACK)
    Time_Date = myFont.render(time.strftime("%d %b %Y"), 1, BLACK)

    # Event Loop / Game Loop
    while main:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))
        screen.blit(bar, (0, 662))
        Hover(trash1,trash2,25,10)
        Hover(internet1,internet2,20,150)
        Hover(shop1,shop2,20,270)
        Hover(doorgame1,doorgame2,150,10)
        Hover(pong1,pong2,32,380)
        screen.blit(start, (0, 660))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if trash.get_rect(topleft=(25, 10)).collidepoint(mouse_pos):
                    main = False
                    Unavailable()

                if internet.get_rect(topleft=(20, 150)).collidepoint(mouse_pos):
                    main = False
                    Unavailable()

                if shop.get_rect(topleft=(20, 279)).collidepoint(mouse_pos):
                    main = False
                    Unavailable()

                if doorgame.get_rect(topleft=(100, 10)).collidepoint(mouse_pos):
                    main = False
                    DoorGame()

                if pong.get_rect(topleft=(32,380)).collidepoint(mouse_pos):
                    main = False
                    Unavailable()

                if start.get_rect(topleft=(0,660)).collidepoint(mouse_pos):
                    clicked += 1
                    startbar = pygame.image.load('dm5.png').convert_alpha()
                    apps = pygame.image.load('apps1.png').convert_alpha()
                    games = pygame.image.load('games1.png').convert_alpha()
                    power = pygame.image.load('pow1.png').convert_alpha()
                    setting = pygame.image.load('set1.png').convert_alpha()


        if (clicked % 2) == 0:
            screen.blit(startbar, (0, 455))
            Hover(apps1,apps2,20,465)
            Hover(games1,games2,20,535)
            Hover(pow1,pow2,10,640)
            Hover(set1,set2,115,605)

            if setting.get_rect(topleft=(115, 605)).collidepoint(mouse_pos):
                main = False
                Settings()
            if power.get_rect(topleft=(10, 640)).collidepoint(mouse_pos):
                main = False
                Title()
        else:
            pass
        screen.blit(Time_HourMin, (1155, 672))
        screen.blit(Time_Date, (1120, 691))
        clock.tick(60)
        pygame.display.flip()


# My favorite screen because of Doors. Only Display works(Far Left Door)
def Settings():
    set = True
    background = pygame.image.load('settings.png').convert_alpha()
    customize = pygame.image.load('pdoor.png').convert_alpha()
    display = pygame.image.load('Ddoor.png').convert_alpha()
    sound = pygame.image.load('mdoor.png').convert_alpha()
    back = pygame.image.load('Back.png').convert_alpha()

    while set:
        screen.blit(background, (0, 0))
        Hover(pdoor1,pdoor2,520,150)
        Hover(Ddoor1,Ddoor2,150,150)
        Hover(mdoor1,mdoor2,890,150)
        Hover(back1,back2,1100,600)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if display.get_rect(topleft=(150, 150)).collidepoint(mouse_pos):
                    set = False
                    Display()

                if customize.get_rect(topleft=(520, 150)).collidepoint(mouse_pos):
                    set = False
                    Unavailable()

                if sound.get_rect(topleft=(890, 150)).collidepoint(mouse_pos):
                    set = False
                    Unavailable()

                if back.get_rect(topleft=(1100, 600)).collidepoint(mouse_pos):
                    set = False
                    Mainscreen()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    set = False
                    Mainscreen()

        clock.tick(60)
        pygame.display.flip()


# You can Fullscreen
def Display():
    dis = True
    back = pygame.image.load('Back.png').convert_alpha()
    while dis:
        screen.fill((50, 50, 50))
        Hover(back1, back2, 1100, 600)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back.get_rect(topleft=(1100, 600)).collidepoint(mouse_pos):
                    dis = False
                    Settings()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    dis = False
                    Settings()

        clock.tick(60)
        pygame.display.flip()


# The Actual Game of the Game. Not very fun huh?
def DoorGame():
    running = True
    green = (0, 80, 0)
    myFont = pygame.font.SysFont("Comicsans", 40)
    Score_Label = myFont.render("Score: ", 1, green)
    Score_Value = myFont.render(str(Score), 1, green)
    Goback = myFont.render("ESC to go back", 1, green)
    mouse_pos = pygame.mouse.get_pos()
    Button = ClassHover((500, 500), click1, click2,click3)
    click = pygame.image.load('loadbutton.png')
    back = pygame.image.load('Back.png').convert_alpha()
    while running:
        screen.fill((180, 50, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    Mainscreen()
            if event.type == MOUSEBUTTONDOWN:
                click = event.__dict__

            elif event.type == MOUSEBUTTONUP:
                click = False


        # print(event)
        Button.update(click)
        Score_Value = myFont.render(str(Score), 1, green)
        screen.blit(Score_Label, (1280 - 250, 2))
        screen.blit(Score_Value, (1280 - 120, 2))
        screen.blit(Goback,(1000,650))
        door.update()
        pygame.display.flip()

# Screen is called for every Window I didn't get to
def Unavailable():
    shadowrealm = True
    green = (0,100,0)
    myFont = pygame.font.SysFont("Comicsans", 40)
    Dumb = myFont.render("Hey! Sorry this Window is Currently Unavailable!", 1, green)
    Dumber = myFont.render('~Shane M.D.', 1, green)
    back = pygame.image.load('Back.png').convert_alpha()
    while shadowrealm:
        screen.fill((30,30,30))
        Hover(back1, back2, 1100, 600)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    Mainscreen()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back.get_rect(topleft=(1100, 600)).collidepoint(mouse_pos):
                    shadowrealm = False
                    Title()

        screen.blit(Dumb,(300,300))
        screen.blit(Dumber,(800,500))
        clock.tick(60)
        pygame.display.flip()


#####################################################
#
# Main Code
# Pygame Initialization, Variables, Sprites
#
#####################################################
pygame.init()
pygame.mixer.init()
mainClock = pygame.time.Clock()
pygame.display.set_caption('DoorOS')
screen = pygame.display.set_mode((1280, 720))
font = 'Comic Sans MS'

# Image Variables
trash1 = 'Trash.png'
trash2 = 'Trash2.png'
internet1 = 'E.png'
internet2 = 'E2.png'
shop1 = 'Sh1.png'
shop2 = 'Sh2.png'
doorgame1 = 'DoorG1.png'
doorgame2 = 'DoorG2.png'
start1 = 'DL1.png'
start2 = 'DL2.png'
quit1 = 'P1.png'
quit2 = 'P2.png'
apps1 = 'apps1.png'
apps2 = 'apps2.png'
games1 = 'games1.png'
games2 = 'games2.png'
set1 = 'set1.png'
set2 = 'set2.png'
pow1 = 'pow1.png'
pow2 = 'pow2.png'
pdoor1 = 'pdoor.png'
pdoor2 = 'pdoor2.png'
Ddoor1 = 'Ddoor.png'
Ddoor2 = 'Ddoor2.png'
mdoor1 = 'mdoor.png'
mdoor2 = 'mdoor2.png'
pong1 = 'pong1.png'
pong2 = 'pong2.png'
click1 = 'loadbutton.png'
click2 = 'loadbutton2.png'
click3 = 'loadbutton3.png'
back1 = 'Back.png'
back2 = 'Back2.png'

# Sprite Groups
moving_sprites = pygame.sprite.Group()
bckgrnd = QuitAnim(0,0)
moving_sprites.add(bckgrnd)
hover_sprites = pygame.sprite.Group()
Score = ClassScore()
door = dooradd((300, 0))

# Shows Errors, Fullscreen, and colors
successes, failures = pygame.init()
print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))
global fullscreen
fullscreen = False
global num
num = 1
clock = pygame.time.Clock()
BLACK = (0,0,0)
WHITE = (255,255,255)

# Game Start
Title()

