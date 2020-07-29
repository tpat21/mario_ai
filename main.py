import pygame
import neat
import time
import os
import random

pygame.font.init()

from mario_obj import *
from pipe_obj import *
from base_obj import *
from shell_obj import *

WIN_WIDTH = 800
WIN_HEIGHT = 350

BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('images', 'bg.png')))
STAT_FONT = pygame.font.SysFont('comicsans', 50)


def draw_window(win, mario, pipes, base, shells, score):
    win.blit(BG_IMG, (0, 0))

    for pipe in pipes:
        pipe.draw(win)

    for shell in shells:
        shell.draw(win)

    text = STAT_FONT.render('Score: ' + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    base.draw(win)
    mario.draw(win)

    pygame.display.update()


def main():
    mario = Mario(90, 180)
    base = Base(300)
    shells = [Shell(800, 275)]
    pipes = [Pipe(800)]

    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        add_pipe = False
        add_shell = False

        rem_shell = []
        rem = []

        for pipe in pipes:
            if pipe.collide(mario):
                pass

            if not pipe.passed and pipe.x < mario.x:
                pipe.passed = True
                add_pipe = True
            pipe.move()

        for shell in shells:
            if shell.collide(mario):
                pass

            if not shell.passed and shell.x < mario.x:
                shell.passed = True
                add_shell = True
            shell.move()

        rand_pipe = random.randint(800, 1200)

        if add_pipe:
            score += 1
            pipes.append(Pipe(rand_pipe))

        if add_shell:
            score += 1
            shells.append(Shell(rand_pipe, 275))

        for r in rem:
            pipe.remove(r)

        for rm in rem_shell:
            shell.remove(rm)

        base.move()
        draw_window(win, mario, pipes, base, shells, score)

    pygame.quit()
    quit()


main()
