#import necessary modules
import pygame
import random

pygame.init()
pygame.font.init()

#set display size
screen = pygame.display.set_mode((800, 800))

#main font
font = pygame.font.SysFont('freesansbold.ttf', 50)

#instruction font
instuction_font = pygame.font.SysFont('freesansbold.ttf', 30)
clock = pygame.time.Clock()

def render_board(squares, size):
    storage = []
    x = int(((800 - (size[0] * squares[0])) / 2))
    y = int(((800 - (size[1] * squares[1])) / 2))

    for a in range(squares[0]):
        for b in range(squares[1]):
            pygame.draw.rect(screen, (0,5,0), (x+(a*size[0]), y+(b*size[1]), size[0], size[1]), 2)
            storage.append((x + (a*size[0]), y + (b*size[1]), size[0], size[1], 1))
    return storage


squares = (5,5)
size = (70,70)
score = 0
counter = 30

#countdown timer from 30 seconds.
#e.g. counter means the timer going down from 30, 29, ...
def pre_time(counter):
    if counter > 9:
        return '0:'
    elif (counter < 10 and counter > -1):
        return '0:0'
    else:
        print('Final Score was: ' + str(score))

reset = True
running = True
storage = render_board(squares, size)

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)
#font rendering
score_text = font.render('Score: ' + str(score), True, (0,0,0))
timer_text = font.render(pre_time(counter) + str(counter), True, (0,0,0))
title_text = font.render('Clicker Game!', True, (0, 64, 0))
instruction_text = instuction_font.render('GREEN:LEFT, ORANGE:RIGHT', True, (0, 2, 0))

while running:
    clock.tick(60)

    mouse = pygame.mouse.get_pos()

    if reset:
        number = random.randint(0, (squares[0] * squares[1]) - 1)
        target = (storage[number][0], storage[number][1])
        if random.randint(1, 2) == 1:
            colour = (20, 100, 0)
            click = 'left'
        else: 
            colour = (221, 151, 20)
            click = 'right'
        reset = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse[0] > target[0] and mouse[0] < target[0] + size[0] and mouse[1] > target[1] and mouse[1] < target[1] + size[1]:
                if (event.button == 1 and click == 'left') or (event.button == 3 and click == 'right'):
                    score = score + 1
                    print(str(score))
                    score_text = font.render('Score: ' + str(score), True, (0,0,0))
                reset = True
        if event.type == timer_event:
            counter = counter - 1
            timer_text = font.render(pre_time(counter) + str(counter), True, (0,0,0))

    #updating screen
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, colour, (target[0], target[1], size[0], size[1]))
    storage = render_board(squares, size)
    screen.blit(title_text, (300, 10))
    screen.blit(score_text,(10, 10))
    screen.blit(timer_text, (700, 10))
    screen.blit(instruction_text, (250, 100))

    pygame.display.flip()

pygame.quit()