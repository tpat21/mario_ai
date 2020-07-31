import pygame
import neat
import time
import os
import random
from main import *

MARIO_IMGS = [(pygame.image.load(os.path.join('images', 'mario.png'))),
              (pygame.image.load(os.path.join('images', 'mario2.png'))),
              (pygame.image.load(os.path.join('images', 'mario3.png'))),
              (pygame.image.load(os.path.join('images', 'mario4.png')))]


class Mario:
    IMGS = MARIO_IMGS
    ANIMATION_TIME = 2.5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tick_count = 0
        self.vel = 0
        self.img_count = 0
        self.img = self.IMGS[0]
        self.height = self.y
        self.tilt = 0

        self.isJump = False
        self.jumpCount = 13

    def jump(self):

        self.isJump = True

        if self.isJump:
            if self.jumpCount >= -14:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= self.jumpCount ** 2 * 0.1 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 14



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

        # if self.isJump:
        #     self.img = self.IMGS[3]


        win.blit(self.img, (self.x, self.y))

    def get_mask(self, win):

        return pygame.mask.from_surface(self.img)
