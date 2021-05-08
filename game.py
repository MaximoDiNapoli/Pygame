import pygame
from pygame.locals import *
import sys
import random
import os
#Constantes
WIDTH = 1000
HEIGHT = 800
COLOR_RED = (255,0,0)
COLOR_BLACK = (0,0,0)
COLOR_BLUE = (0,0,255)
SPEED = 10
SCOREINT = 0
SCORE = str(SCOREINT + 1)

COLOR_WHITE = (255, 255, 255)

#jugador

PLAYER_SIZE = 50
PLAYER_POSITION = [WIDTH/2, HEIGHT - PLAYER_SIZE * 2]

#enemigos

ENEMY_SIZE = random.randint(30, 70)
ENEMY_POSITION = [random.randint(0, WIDTH - ENEMY_SIZE), 0]
os.environ['SDL_VIDEO_CENTERED'] = '1'
window = pygame.display.set_mode((WIDTH,HEIGHT)) #creo la ventana

gameOver = False
clock = pygame.time.Clock()

#detecctar colociones
def detectCollision(PLAYER_POSITION,ENEMY_POSITION):
    jx = PLAYER_POSITION[0]
    jy = PLAYER_POSITION[1]
    ex = ENEMY_POSITION[0]
    ey = ENEMY_POSITION[1]

    if(ex >= jx and ex <(jx + PLAYER_SIZE)) or (jx >= ex and jx < (ex + ENEMY_SIZE)):
        if(ey >= jy and ey <(jy + PLAYER_SIZE)) or (jy >= ey and jy < (ey + ENEMY_SIZE)):
            return True
    return False

pygame.init()
while not gameOver: #bucle principal 
    FUENTE = pygame.font.Font(None, 20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #movimiento
        if event.type == pygame.KEYDOWN:
            x = PLAYER_POSITION[0]
            y = PLAYER_POSITION[1]
            if event.key == pygame.K_w and y != 0: 
                y -= PLAYER_SIZE 
            if event.key == pygame.K_a and x != 0:
                x -= PLAYER_SIZE 
            if event.key == pygame.K_s and y != HEIGHT - PLAYER_SIZE:
                y += PLAYER_SIZE 
            if event.key == pygame.K_d and x != WIDTH - PLAYER_SIZE:
                x += PLAYER_SIZE 

            PLAYER_POSITION[0] = x
            PLAYER_POSITION[1] = y

    #refrescar 
    window.fill(COLOR_BLACK)

    if ENEMY_POSITION[1] >=0 and ENEMY_POSITION[1] < HEIGHT:
        ENEMY_POSITION[1] += SPEED
    else:
        ENEMY_POSITION[0] = random.randint(0, WIDTH - ENEMY_SIZE)
        ENEMY_POSITION[1] = 0
    SCOREINT += 1
    SCORE = str(SCOREINT + 1)
    #coliciones
    if detectCollision(PLAYER_POSITION, ENEMY_POSITION):
        gameOver = True
    
    #dibujar enemigo
    ScoreShow = FUENTE.render(SCORE, 1, COLOR_WHITE)
    window.blit(ScoreShow, (15, 10))
    pygame.draw.rect(window , COLOR_BLUE,
                    (ENEMY_POSITION[0],ENEMY_POSITION[1],
                    ENEMY_SIZE, ENEMY_SIZE))
    #dibujar jugador
    pygame.draw.rect(window , COLOR_RED,
                    (PLAYER_POSITION[0],PLAYER_POSITION[1],
                    PLAYER_SIZE, PLAYER_SIZE))
    clock.tick(60)
    SPEED += 0.001
    pygame.display.update()