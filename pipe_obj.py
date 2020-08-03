import pygame
import neat
import time
import os
import random
import random

PIPE_IMG = (pygame.image.load(os.path.join('images', 'pipe.png')))


class Pipe:
    VEL = 9
    HEIGHT = 10

    def __init__(self, x):
        self.x = x
        self.pipe = PIPE_IMG
        self.passed = False
        self.bottom = 250


    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        win.blit(self.pipe, (self.x, self.bottom))

    def collide(self, mario):
        mario_mask = mario.get_mask()
        pipe_mask = pygame.mask.from_surface(self.pipe)

        offset = (self.x - mario.x, self.bottom - round(mario.y))

        point = mario_mask.overlap(pipe_mask, offset)

        if point:
            return True

        return False
