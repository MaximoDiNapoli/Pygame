import pygame
import sys
import random
import os
#Constantes
WIDTH = 800
HEIGHT = 600
COLOR_RED = (255,0,0)
COLOR_BLACK = (0,0,0)
COLOR_BLUE = (0,0,255)
SPEED = 20


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

while not gameOver: #bucle principal 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #movimiento
        if event.type == pygame.KEYDOWN:
            x = PLAYER_POSITION[0]
            y = PLAYER_POSITION[1]
            if event.key == pygame.K_w:
                y -= PLAYER_SIZE * SPEED / 10
            if event.key == pygame.K_a:
                x -= PLAYER_SIZE * SPEED / 10
            if event.key == pygame.K_s:
                y += PLAYER_SIZE * SPEED / 10
            if event.key == pygame.K_d:
                x += PLAYER_SIZE * SPEED / 10

            PLAYER_POSITION[0] = x
            PLAYER_POSITION[1] = y

    #refrescar 
    window.fill(COLOR_BLACK)

    if ENEMY_POSITION[1] >=0 and ENEMY_POSITION[1] < HEIGHT:
        ENEMY_POSITION[1] += SPEED
    else:
        ENEMY_POSITION[0] = random.randint(0, WIDTH - ENEMY_SIZE)
        ENEMY_POSITION[1] = 0

    #coliciones
    if detectCollision(PLAYER_POSITION, ENEMY_POSITION):
        gameOver = True
    
    #dibujar enemigo
    pygame.draw.rect(window , COLOR_BLUE,
                    (ENEMY_POSITION[0],ENEMY_POSITION[1],
                    ENEMY_SIZE, ENEMY_SIZE))
    #dibujar jugador
    pygame.draw.rect(window , COLOR_RED,
                    (PLAYER_POSITION[0],PLAYER_POSITION[1],
                    PLAYER_SIZE, PLAYER_SIZE))
    clock.tick(30)
    SPEED += 0.01
    pygame.display.update()