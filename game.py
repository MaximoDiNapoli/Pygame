import pygame
import sys

#Constantes
WIDTH = 800
HEIGHT = 600
COLOR_RED = (255,0,0)
COLOR_BLACK = (0,0,0)
COLOR_BLUE = (0,0,255)


#jugador

PLAYER_SIZE = 50
PLAYER_POSITION = [WIDTH/2, HEIGHT - PLAYER_SIZE * 2]


window = pygame.display.set_mode((WIDTH,HEIGHT)) #creo la ventana

gameOver = False

while not gameOver: #bucle principal 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #movimiento
        if event.type == pygame.KEYDOWN:
            x = PLAYER_POSITION[0]
            y = PLAYER_POSITION[1]
            if event.key == pygame.K_w:
                y -= PLAYER_SIZE
            if event.key == pygame.K_a:
                x -= PLAYER_SIZE
            if event.key == pygame.K_s:
                y += PLAYER_SIZE
            if event.key == pygame.K_d:
                x += PLAYER_SIZE

            PLAYER_POSITION[0] = x
            PLAYER_POSITION[1] = y


    #refrescar 
    window.fill(COLOR_BLACK)
    #dibujar jugador
    pygame.draw.rect(window , COLOR_RED,
                    (PLAYER_POSITION[0],PLAYER_POSITION[1],
                    PLAYER_SIZE, PLAYER_SIZE))
    pygame.display.update()