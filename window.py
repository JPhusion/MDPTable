import pygame
import time
import sys
from pygame.locals import *

# INITIATE WINDOW =========================================================== #
clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption("Smart Table GUI")

framerate = 60

SCREEN_SIZE = (pygame.display.Info().current_w,
               pygame.display.Info().current_h)
WINDOW_SIZE = (1024, 576)
DISPLAY_SIZE = (1920, 1080)

win = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
display = pygame.Surface(DISPLAY_SIZE)

# LOAD ASSETS =============================================================== #
wallpaper = pygame.image.load("./assets/wallpaper/wallpaperinuse.jpg")

# SCALING WINDOW ============================================================ #
def scaled_win():
    ratioX, ratioY = 16, 9
    if WINDOW_SIZE[0]/ratioX > WINDOW_SIZE[1]/ratioY:
        scaled_win = (WINDOW_SIZE[0], int(WINDOW_SIZE[0]/ratioX * ratioY))
        position = (0, -(scaled_win[1] - WINDOW_SIZE[1])/2)
    elif WINDOW_SIZE[0]/ratioX < WINDOW_SIZE[1]/ratioY:
        scaled_win = (int(WINDOW_SIZE[1]/ratioY * ratioX), WINDOW_SIZE[1])
        position = (-(scaled_win[0] - WINDOW_SIZE[0])/2, 0)
    else:
        scaled_win = WINDOW_SIZE
        position = (0, 0)
    return scaled_win, position

# GAMELOOP ================================================================== #
while True:
    
    display.blit(wallpaper, (0,0))
    # display.blit(pygame.transform.scale(wallpaper, (scaled_win()[0])), scaled_win()[1])
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == VIDEORESIZE:
            WINDOW_SIZE = (event.w, event.h)
            win = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
                
    win.blit(pygame.transform.scale(
        display, (scaled_win()[0])), scaled_win()[1])
    pygame.display.update()
    clock.tick(framerate)
