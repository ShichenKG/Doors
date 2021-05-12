import pygame, sys
from pygame.locals import *


class QuitAnim(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('B1.png'))
        self.sprites.append(pygame.image.load('B2.png'))
        self.sprites.append(pygame.image.load('B3.png'))
        self.sprites.append(pygame.image.load('B4.png'))
        self.sprites.append(pygame.image.load('B5.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self,speed):
        self.current_sprite += speed

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 4

        self.image = self.sprites[int(self.current_sprite)]


class Images(pygame.sprite.Sprite):
    def __init__(self,image1,image2,x,y):
        self.x = x
        self.y = y
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load(image1))
        self.sprites.append(pygame.image.load(image2))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]
        self.rect.x = self.x
        self.rect.y = self.y

        self.mask = pygame.mask.from_surface(self.image)




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

    # Event Loop / Game Loop
    while main:
        screen.blit(background, (0, 0))
        screen.blit(bar, (0, 662))
        Hover(trash1,trash2,25,10)
        Hover(internet1,internet2,20,150)
        Hover(shop1,shop2,20,270)
        Hover(doorgame1,doorgame2,150,10)
        screen.blit(start, (0, 660))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if trash.get_rect(topleft=(25, 10)).collidepoint(mouse_pos):
                    pass

                if internet.get_rect(topleft=(20, 150)).collidepoint(mouse_pos):
                    pass

                if shop.get_rect(topleft=(20, 279)).collidepoint(mouse_pos):
                    pass

                if doorgame.get_rect(topleft=(100, 10)).collidepoint(mouse_pos):
                    main = False
                    DoorGame()

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
        clock.tick(60)
        pygame.display.flip()


def Settings():
    set = True
    background = pygame.image.load('settings.png').convert_alpha()
    customize = pygame.image.load('pdoor.png').convert_alpha()
    display = pygame.image.load('Ddoor.png').convert_alpha()
    sound = pygame.image.load('mdoor.png').convert_alpha()

    while set:
        screen.blit(background, (0, 0))
        Hover(pdoor1,pdoor2,520,150)
        Hover(Ddoor1,Ddoor2,150,150)
        Hover(mdoor1,mdoor2,890,150)
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
                    pass

                if sound.get_rect(topleft=(890, 150)).collidepoint(mouse_pos):
                    pass
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    set = False
                    Mainscreen()

        clock.tick(60)
        pygame.display.flip()


def Display():
    dis = True
    while dis:
        screen.fill((50, 50, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    dis = False
                    Settings()

        clock.tick(60)
        pygame.display.flip()

def DoorGame():
    running = True
    while running:
        screen.fill((50, 200, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    Mainscreen()

        clock.tick(60)
        pygame.display.flip()

pygame.init()
pygame.mixer.init()
mainClock = pygame.time.Clock()
pygame.display.set_caption('DoorOS')
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

# Quitting the Game Animation
moving_sprites = pygame.sprite.Group()
bckgrnd = QuitAnim(0,0)
moving_sprites.add(bckgrnd)
hover_sprites = pygame.sprite.Group()


# Random Variables
successes, failures = pygame.init()
print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))
pygame.time.delay(1000)
screen = pygame.display.set_mode((1280, 720))
global fullscreen
fullscreen = False
global num
num = 1
clock = pygame.time.Clock()

Title()

