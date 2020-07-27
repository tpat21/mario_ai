import pygame
import neat
import time
import os
import random

WIN_WIDTH = 800
WIN_HEIGHT = 500

MARIO_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'mario.png'))),
             pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'mario2.png'))),
             pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'mario3.png')))]

PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'pipe.png')))

BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'bg.png')))

BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'base.png')))


class Mario:
    MAX_ROTATION = 25
    IMGS = MARIO_IMGS
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.tilt = 0  # degrees to tilt
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        """
        make the bird jump
        :return: None
        """
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        # for downward acceleration
        d = self.vel * self.tick_count + 1.5 * self.tick_count ** 2  # calculate displacement




    def draw(self, win):

        self.img_count += 1

        # For animation of bird, loop through three images
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

        # so when bird is nose diving it isn't flapping
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2

        rotated_imgage = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_imgage.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)

        win.blit(rotated_imgage, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


def draw_window(win, bird):
    win.blit(BG_IMG, (0,0))
    bird.draw(win)
    pygame.display.update()


def main():
    mario = Mario(0, 200 )
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        mario.move()
        draw_window(win, mario)


    pygame.quit()
    quit()


main()
