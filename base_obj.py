import pygame
import neat
import time
import os
import random

BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'base1.png')))


class Base:
    VEL = 7
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH
        self.x3 = self.WIDTH * 2

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL
        self.x3 -= self.VEL

        if self.x1 + self.WIDTH <= 0:
            self.x1 = self.x2 + self.x3 +  self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.x3 + self.WIDTH

        if self.x3 + self.WIDTH < 0:
            self.x3 = self.x1 + self.x2 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))
        win.blit(self.IMG, (self.x3, self.y))