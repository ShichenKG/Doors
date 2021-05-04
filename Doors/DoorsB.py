import pygame, time, sys

from pygame.locals import *

# Plays an animation for
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

    def update(self):
        clock.tick(12)
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 4

        self.image = self.sprites[self.current_sprite]


class button():
    def __init__(self, color, x, y, width, height, text='', font = '',size = 60):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.size = size

    def draw(self, win, outline=None):
        pos = pygame.mouse.get_pos()
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont(self.font,self.size)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))


    if button_rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            clicked = True
            pygame.draw.rect(screen, self.click_col, button_rect)
        elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
            clicked = False
            action = True
        else:
            pygame.draw.rect(screen, self.hover_col, button_rect)
    else:
        pygame.draw.rect(screen, self.button_col, button_rect)

def main_menu():
    while True:

        screen.fill((70, 171, 97))
        title = button((70, 171, 97), 540, 50, 220, 100, 'Main Menu')
        title.draw(screen)

        button_1 = button((0,255,0), 540, 200, 220, 100, 'Start',('Comic Sans MS',60))
        button_2 = button((0,255,0), 540, 350, 220, 100, 'Options',('Comic Sans MS',60))
        button_3 = button((0,255,0), 540, 500, 220, 100, 'Quit',('Comic Sans MS',60))
        button_1.draw(screen)
        button_2.draw(screen)
        button_3.draw(screen)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                moving_sprites.draw(screen)
                moving_sprites.update()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.isOver(pos):
                    game()
                if button_2.isOver(pos):
                    options()
                if button_3.isOver(pos):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEMOTION:
                if button_1.isOver(pos):
                    button_1.color=(200,0,0)
                else:
                    button_1.color=(0,255,0)

        pygame.display.update()
        clock.tick(60)



def game():
    running = True
    player = Player()
    while running:
        dt = clock.tick(FPS) / 1000
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
                pygame.QUIT()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.velocity[1] = -200 * dt  # 200 pixels per second
                elif event.key == pygame.K_s:
                    player.velocity[1] = 200 * dt
                elif event.key == pygame.K_a:
                    player.velocity[0] = -200 * dt
                elif event.key == pygame.K_d:
                    player.velocity[0] = 200 * dt
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player.velocity[1] = 0
                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    player.velocity[0] = 0

        player.update()

        screen.blit(player.image, player.rect)
        pygame.display.update()


def options():
    running = True
    global num
    global fullscreen
    monitor_size = [pygame.display.Info().current_w,pygame.display.Info().current_h]
    if fullscreen:
        screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((1280,720))
    while running:
        screen.fill((70, 171, 97))

        title = button((70, 171, 97), 540, 50, 220, 100, 'Options',('Comic Sans MS'),60)
        title.draw(screen)
        button1 = button((0, 255, 0), 540, 500, 220, 100, 'Back',('Comic Sans MS'),60)
        button2 = button((0,255,0), 540, 200, 220, 100, 'FullScreen',('Comic Sans MS'),40)
        button1.draw(screen)
        button2.draw(screen)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if button1.isOver(pos):
                    running = False
                if button2.isOver(pos):
                    num += 1
                    if (num % 2) == 0:
                        fullscreen = True
                    else:
                        fullscreen = False
                    if fullscreen:
                        screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((1280,720))


        pygame.display.update()
        clock.tick(60)

pygame.init()
pygame.mixer.init()
mainClock = pygame.time.Clock()
pygame.display.set_caption('Pygame Test')
font = 'Comic Sans MS'

successes, failures = pygame.init()
print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))
pygame.time.delay(1000)
screen = pygame.display.set_mode((1280, 720))
global fullscreen
fullscreen = False
global num
num = 1
clock = pygame.time.Clock()
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

main_menu()
