import pygame
import neat
import time
import os
import random

from mario_obj import *
from pipe_obj import *
from base_obj import *

WIN_WIDTH = 800
WIN_HEIGHT = 350

BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'bg.png')))


def draw_window(win, mario, pipes, base):
    win.blit(BG_IMG, (0, 0))

    for pipe in pipes:
        pipe.draw(win)

    base.draw(win)
    mario.draw(win)

    pipe.move()
    base.move()

    pygame.display.update()


def main():
    mario = Mario(90, 180)
    base = Base(300)
    pipes = [Pipe(700)]

    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        # add_pipe = False
        # rem = []
        # for pipe in pipes:
        #     if pipe.collide(mario):
        #         pass
        #
        #     if pipe.x + pipe.bottom.get_width() < 0:
        #         rem.append(pipe)
        #
        #     if not pipe.passed and pipe.x < mario.x:
        #         pipe.passed = True
        #         add_pipe = True

    # pipe.move()
    #
    # base.move()

    # if add_pipe:
    #     score += 1
    #     pipes.append(Pipe(700))
    #
    # for r in rem:
    #     pipes.remove(random)
    #
    #
        draw_window(win, mario, pipes, base)

    pygame.quit()
    quit()


main()
