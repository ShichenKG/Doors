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
    def __init__(self,pos_x,pos_y):
        super().__init__()

def Hover(image1,image2,x,y):
    mouse_pos = pygame.mouse.get_pos()

    l = pygame.sprite.Sprite
    l.img1 = pygame.image.load(image1).convert_alpha()
    l.img2 = pygame.image.load(image2).convert_alpha()
    l.img_mask = pygame.mask.from_surface(l.img1)
    l.img_rect = l.img1.get_rect(center = (x,y))
    l.cur_img = l.img1

    if l.img_rect.collidepoint(mouse_pos):
        l.cur_img = l.img2
    else:
        l.cur_img = l.img1
    screen.blit(l.cur_img, (x,y))


def Title():
    title = True
    background = pygame.image.load('mmr.png').convert()
    start = pygame.image.load('DL1.png').convert_alpha()
    quit = pygame.image.load('P1.png').convert_alpha()

    screen.blit(background, (0, 0))
    screen.blit(quit, (325,175))
    screen.blit(start, (690,190))
    # Event Loop / Game Loop
    while title:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start.get_rect(center=(690,190)).collidepoint(mouse_pos):
                    title = False
                    Mainscreen()
                if quit.get_rect(center=(325,175)).collidepoint(mouse_pos):
                    title = False
                    quitanim()


        clock.tick(60)
        pygame.display.flip()


def quitanim():
    isquitting = True
    CLOSE = pygame.USEREVENT + 1
    pygame.time.set_timer(CLOSE, 1600)
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


def Mainscreen():
    main = True
    screen.fill((73, 166, 160))
    trash = pygame.image.load('Trash.png').convert_alpha()
    internet = pygame.image.load('E.png').convert_alpha()
    shop = pygame.image.load('Sh1.png').convert_alpha()
    doorgame = pygame.image.load('DoorG1.png').convert_alpha()
    bar = pygame.image.load('taskbar.png').convert_alpha()
    background = pygame.image.load('background.png').convert_alpha()
    start = pygame.image.load('dm1.png').convert_alpha()

    screen.blit(background, (0,0))
    screen.blit(bar, (0, 662))
    screen.blit(trash, (25, 10))
    screen.blit(internet, (20, 150))
    screen.blit(shop, (20, 270))
    screen.blit(doorgame, (20, 380))
    screen.blit(start, (0, 660))
    # Event Loop / Game Loop
    while main:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if trash.get_rect(center=(25, 10)).collidepoint(mouse_pos):
                    pass

                if internet.get_rect(center=(20, 150)).collidepoint(mouse_pos):
                    pass

                if shop.get_rect(center=(20, 279)).collidepoint(mouse_pos):
                    pass

                if doorgame.get_rect(center=(20, 380)).collidepoint(mouse_pos):
                    pass

                if start.get_rect(center=(0,660)).collidepoint(mouse_pos):
                    startbar = pygame.image.load('dm5.png').convert_alpha()
                    apps = pygame.image.load('apps1.png').convert_alpha()
                    games = pygame.image.load('games1.png').convert_alpha()
                    power = pygame.image.load('pow1.png').convert_alpha()
                    setting = pygame.image.load('set1.png').convert_alpha()
                    screen.blit(startbar, (0, 455))
                    screen.blit(apps, (20, 465))
                    screen.blit(games, (20, 535))
                    screen.blit(power, (10, 640))
                    screen.blit(setting, (115, 605))
                    if setting.get_rect(center=(115, 605)).collidepoint(mouse_pos):
                        Settings()
                    if power.get_rect(center=(10,640)).collidepoint(mouse_pos):
                        main = False
                        quitanim()


        clock.tick(60)
        pygame.display.flip()


def Settings():
    set = True
    background = pygame.image.load('settings.png').convert_alpha()
    customize = pygame.image.load('pdoor.png').convert_alpha()
    display = pygame.image.load('Ddoor.png').convert_alpha()
    sound = pygame.image.load('mdoor.png').convert_alpha()

    screen.blit(background, (0, 0))
    screen.blit(display, (150, 150))
    screen.blit(customize, (520, 150))
    screen.blit(sound, (890, 150))
    while set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if display.get_rect(center=(150, 150)).collidepoint(mouse_pos):
                    set = False
                    Display()

                if customize.get_rect(center=(520, 150)).collidepoint(mouse_pos):
                    pass

                if sound.get_rect(center=(890, 150)).collidepoint(mouse_pos):
                    pass

        clock.tick(60)
        pygame.display.flip()


def Display():
    screen.fill((50,50,50))

pygame.init()
pygame.mixer.init()
mainClock = pygame.time.Clock()
pygame.display.set_caption('DoorOS')
font = 'Comic Sans MS'

# Quitting the Game Animation
moving_sprites = pygame.sprite.Group()
bckgrnd = QuitAnim(0,0)
moving_sprites.add(bckgrnd)

# Image Variables
trash = 'Trash.png'
trash2 = 'Trash2.png'
internet = 'E.png'
internet2 = 'E2.png'
shop = 'Sh1.png'
shop2 = 'Sh2.png'
doorgame = 'DoorG1.png'
doorgame2 = 'DoorG2.png'
start = 'DL1.png'
start2 = 'DL2.png'
quit = 'P1.png'
quit2 = 'P2.png'

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

