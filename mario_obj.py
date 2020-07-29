import pygame
import neat
import time
import os
import random

MARIO_IMGS = [(pygame.image.load(os.path.join('images', 'mario.png'))),
              (pygame.image.load(os.path.join('images', 'mario2.png'))),
              (pygame.image.load(os.path.join('images', 'mario3.png')))]


class Mario:
    IMGS = MARIO_IMGS
    ROT_VEL = 20
    ANIMATION_TIME = 2.5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel =  -10.5
        self.tick_count = 0
        self.height = self.y

    def draw(self, win):
        self.img_count += 1

        # For animation of mario, loop through three images
        if self.img_count <= self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count <= self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]
        elif self.img_count <= self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.img_count <= self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        win.blit(self.img, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
