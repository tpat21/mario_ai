import pygame
import neat
import time
import os
import random

WIN_WIDTH = 800
WIN_HEIGHT = 350

MARIO_IMGS = [(pygame.image.load(os.path.join('images', 'mario.png'))),
              (pygame.image.load(os.path.join('images', 'mario2.png'))),
              (pygame.image.load(os.path.join('images', 'mario3.png')))]

PIPE_IMG = (pygame.image.load(os.path.join('images', 'pipe.png')))

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
        self.vel = 0
        self.tick_count = 0
        self.height = self.y

    # def move(self):
    #     self.tick_count += 1
    #
    #     d = self.vel * self.tick_count + 1.5 * self.tick_count ** 2

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

        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2

        rotated_imgage = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_imgage.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)

        win.blit(rotated_imgage, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


class Pipe:
    VEL = 5
    HEIGHT = 10

    def __init__(self, x):
        self.x = x
        self.location = 0
        self.PIPE = PIPE_IMG
        self.passed = False
        self.bottom = 0

    def set_location(self):
        self.location = random.randint(50, 450)

    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        win.blit(self.PIPE, (self.x, self.bottom))

    def collide(self, mario):
        mario_mask = mario.get_mask()
        pipe_mask = pygame.mask.from_surface(self.PIPE)

        offset = (self.x - mario.x, self.top - round(mario.y))

        point = mario_mask.overlap(pipe_mask, offset)

        if point:
            return True

        return False


class Base:
    VEL = 5
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __int__(self, x):
        self.x = x
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):

        self.x1 -= self.VEL
        self.x2 -= self.VEL
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))

def draw_window(win, mario, pipes):
    win.blit(BG_IMG, (0, 0))

    for pipe in pipes:
        pipe.draw(win)

    # base.draw(win)

    mario.draw(win)
    pygame.display.update()


def main():
    mario = Mario(0, 200)
    # base = Base(730)
    pipes = [Pipe(700)]

    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # mario.move()
        draw_window(win, mario, pipes)

    pygame.quit()
    quit()


main()
