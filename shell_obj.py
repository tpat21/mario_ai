import pygame
import neat
import time
import os
import random
import random

SHELL_IMGS = [(pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'shell_1.png')))),
              (pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'shell_2.png')))),
              (pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'shell_3.png')))),
              (pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'shell_4.png'))))]


class Shell:
    IMGS = SHELL_IMGS
    VEL = 15
    ANIMATION_TIME = 4

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.passed = False
        self.tick_count = 0
        self.shell = self.IMGS[0]
        self.img_count = 0

    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        self.img_count += 1
        if self.img_count <= self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count <= self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]
        elif self.img_count <= self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.img_count <= self.ANIMATION_TIME * 4:
            self.img = self.IMGS[3]
        elif self.img_count == self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        win.blit(self.img, (self.x, self.y))

    def collide(self, mario):
        mario_mask = mario.get_mask()
        shell_mask = pygame.mask.from_surface(self.shell)

        offset = (self.x - mario.x, self.y - round(mario.y))

        point = mario_mask.overlap(shell_mask, offset)

        if point:
            return True

        return False
