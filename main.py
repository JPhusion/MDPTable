import os
import sys

# os.environ['SDL_VIDEODRIVER'] = "dummy"
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from gui.widgets import *

# classes





# init window
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Smart Table GUI")
framerate = 60
# SCREEN_SIZE = (pygame.display.Info().current_w,
#                pygame.display.Info().current_h)
SCREEN_SIZE = (1200, 1920)
DISPLAY_SIZE = (1200, 1920)
WINDOW_SIZE = (1200, 1920)
win = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
display = pygame.Surface(DISPLAY_SIZE)

fullscreen = True
widget1 = widget(2, 1)

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


# Gameloop
while True:

    pygame.draw.rect(display, (0, 0, 0), pygame.Rect(
            0, 0, 120, 120))
    widget1.draw(display, (1, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            if not fullscreen:
                WINDOW_SIZE = (event.w, event.h)
                win = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                fullscreen = not fullscreen
                win = pygame.display.set_mode((SCREEN_SIZE), pygame.FULLSCREEN) if fullscreen else pygame.display.set_mode(
                    (1080, 1920), pygame.RESIZABLE)
    if fullscreen:
        win.blit(pygame.transform.scale(
            display, SCREEN_SIZE), (0, 0))
    else:
        win.blit(pygame.transform.scale(
            display, (scaled_win()[0])), scaled_win()[1])
    pygame.display.update()
    clock.tick(framerate)
