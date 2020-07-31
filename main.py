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




# def draw_window(win, marios, pipes, base, shells, score):
def draw_window(win, marios, pipes, base, score):


    win.blit(BG_IMG, (0, 0))

    for pipe in pipes:
        pipe.draw(win)

    # for shell in shells:
    #     shell.draw(win)

    text = STAT_FONT.render('Score: ' + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    base.draw(win)
    for mario in marios:
        mario.draw(win)

    # alive
    score_label = STAT_FONT.render("Alive: " + str(len(marios)), 1, (255, 255, 255))
    win.blit(score_label, (10, 10))

    pygame.display.update()


def eval_genomes(genomes, config):


    nets = []
    ge = []
    marios = []


    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        genome.fitness = 0  # start with fitness level of 0

        nets.append(net)
        marios.append(Mario(90, 180))
        ge.append(genome)

    base = Base(300)
    # shells = [Shell(800, 275)]
    pipes = [Pipe(800)]
    score = 0

    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    run = True
    while run and len(marios) > 0:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break

        shell_ind = 0
        rem = []
        add_pipe = False

        for x, mario in enumerate(marios):
            ge[x].fitness += .10

            output = nets[marios.index(mario)].activate((mario.y, abs(mario.y - pipes[0].bottom)))

            if output[0] > .5:
                mario.jump()


        # add_shell = False
        # rem_shell = []

        base.move()


        for pipe in pipes:
            pipe.move()
            # check for collision
            for mario in marios:
                if pipe.collide(mario, win):
                    ge[marios.index(mario)].fitness -= 1
                    nets.pop(marios.index(mario))
                    ge.pop(marios.index(mario))
                    marios.pop(marios.index(mario))

                if not pipe.passed and pipe.x < mario.x:
                    pipe.passed = True
                    add_pipe = True

        rand_pos = random.randint(800, 1200)

        if add_pipe:
            score += 1
            for genome in ge:
                genome.fitness += 5
            pipes.append(Pipe(rand_pos))

        for r in rem:
            pipe.remove(r)

        for mario in marios:
            if not marios:
                nets.pop(marios.index(mario))
                ge.pop(marios.index(mario))
                marios.pop(marios.index(mario))
                run = False

        draw_window(win, marios, pipes, base, score)

        # Determins how many pipes are on the screen
        # if len(marios) > 0:
        #     if len(pipes) > 1 and marios[0] > pipes[0].x:
        #         pipe_ind = 1
        # else:
        #     run = False
        #     break

        # if len(marios) > 0:
        #     if len(pipes) > 1 and marios[0] > pipes[0].x:
        #         shell_ind = 1
        # else:
        #     run = False
        #     break

        # for shell in shells:
        #     for x, mario in enumerate(marios):
        #         if shell.collide(mario):
        #             ge[x].fitness -= 1
        #             marios.pop(x)
        #             nets.pop(x)
        #             ge.pop(x)
        #
        #         if not shell.passed and shell.x < mario.x:
        #             shell.passed = True
        #             add_shell = True
        #     shell.move()

        # if add_shell:
        #     score += 1
        #     for g in ge:
        #         g.fitness += 5
        #     shells.append(Shell(rand_pos, 275))

        # for rm in rem_shell:
        #     shell.remove(rm)

        # draw_window(win, marios, pipes, base, shells, score)


def running(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(eval_genomes, 10)

    print('\nBest genome:\n{!s}'.format(winner))


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    running(config_path)
