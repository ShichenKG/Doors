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




def Title():
    background = pygame.image.load('mmr.png').convert()
    start = pygame.image.load('DL1.png').convert_alpha()
    quit = pygame.image.load('P1.png').convert_alpha()

    screen.blit(background, (0, 0))
    screen.blit(quit, (300,150))
    screen.blit(start, (650, 100))
    # Event Loop / Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start.get_rect(center=(650,100)).collidepoint(mouse_pos):
                    Mainscreen()


        clock.tick(60)
        pygame.display.flip()




def quitanim():
    CLOSE = pygame.USEREVENT + 1
    pygame.time.set_timer(CLOSE, 1600)
    # Event Loop / Game Loop
    while True:
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
    screen.fill((73, 166, 160))
    trash = pygame.image.load('Trash.png').convert_alpha()
    internet = pygame.image.load('E.png').convert_alpha()
    shop = pygame.image.load('Sh1.png').convert_alpha()
    doorgame = pygame.image.load('DoorG1.png').convert_alpha()

    screen.blit(trash, (50, 50))
    screen.blit(internet, (50, 200))
    screen.blit(shop, (50, 300))
    screen.blit(doorgame, (50, 400))
    # Event Loop / Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if trash.get_rect(center=(650, 100)).collidepoint(mouse_pos):
                    pass

                if internet.get_rect(center=(650, 100)).collidepoint(mouse_pos):
                    pass

                if shop.get_rect(center=(650, 100)).collidepoint(mouse_pos):
                    pass

                if doorgame.get_rect(center=(650, 100)).collidepoint(mouse_pos):
                    pass
        clock.tick(60)
        pygame.display.flip()


def Settings():
    pass


def Display():
    pass

pygame.init()
pygame.mixer.init()
mainClock = pygame.time.Clock()
pygame.display.set_caption('DoorOS')
font = 'Comic Sans MS'

# Quitting the Game Animation
moving_sprites = pygame.sprite.Group()
bckgrnd = QuitAnim(0,0)
moving_sprites.add(bckgrnd)

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

