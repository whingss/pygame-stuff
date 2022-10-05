import pygame, sys
from pygame.locals import *
import random
import math
import time

pygame.init()

SCREENHEIGHT = 600
SCREENWIDTH = 400

FPSTICKRATE = 60

SPEED = 5

FPS = pygame.time.Clock()


black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
grey = pygame.Color(128, 128, 128)
red = pygame.Color(255, 0, 0)

DISPLAYSURF = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
DISPLAYSURF.fill(white)
pygame.display.set_caption("Title")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (math.floor(SCREENWIDTH/2),SCREENHEIGHT - 80)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < SCREENWIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREENWIDTH - 40), 0)

    def move(self):
        if SPEED > 15:
            self.rect.move_ip(0,15)
        else:
            self.rect.move_ip(0,SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, SCREENWIDTH-30), 0)

P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 2
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    DISPLAYSURF.fill(white)

    for sprite in all_sprites:
        DISPLAYSURF.blit(sprite.image, sprite.rect)
        sprite.move()
    
    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURF.fill(red)
        pygame.display.update()
        for sprite in all_sprites:
            sprite.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    pygame.display.update()
    FPS.tick(FPSTICKRATE)
