import pygame
import sys
from pygame.locals import *
from weather.weather import *

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

# INITIATE VARIABLE ========================================================= #
fullscreen = False
fadein = True
fadeout = False

# LOAD ASSETS =============================================================== #
wallpaper = pygame.image.load("./assets/wallpaper/wallpaperinuse.jpg")
loading = pygame.image.load("./assets/loading screen/loading.jpg")

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


# TRANSITIONS =============================================================== #
def fadein():
    frames = 32
    for i in range(frames):
        win.blit(pygame.transform.scale(
            loading, (scaled_win()[0])), scaled_win()[1])
        display.set_alpha((256/frames) * i)
        if fullscreen:
            win.blit(pygame.transform.scale(
                display, SCREEN_SIZE), (0, 0))
        else:
            win.blit(pygame.transform.scale(
                display, (scaled_win()[0])), scaled_win()[1])
        pygame.display.update()
        clock.tick(framerate)


def fadeout():
    frames = 32
    for i in range(frames):
        win.blit(pygame.transform.scale(
            loading, (scaled_win()[0])), scaled_win()[1])
        display.set_alpha(255 - (256/frames) * i)
        if fullscreen:
            win.blit(pygame.transform.scale(
                display, SCREEN_SIZE), (0, 0))
        else:
            win.blit(pygame.transform.scale(
                display, (scaled_win()[0])), scaled_win()[1])
        pygame.display.update()
        clock.tick(framerate)


# GAMELOOP ================================================================== #
display.blit(wallpaper, (0, 0))
for i in range(64):
    win.fill((0, 0, 0))
    display.set_alpha((256/64) * i)
    if fullscreen:
        win.blit(pygame.transform.scale(
            display, SCREEN_SIZE), (0, 0))
    else:
        win.blit(pygame.transform.scale(
            display, (scaled_win()[0])), scaled_win()[1])
    pygame.display.update()
    clock.tick(framerate)

while True:

    display.blit(wallpaper, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == VIDEORESIZE:
            if not fullscreen:
                WINDOW_SIZE = (event.w, event.h)
                win = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
        if event.type == KEYDOWN:
            if event.key == K_F11:
                fullscreen = not fullscreen
                win = pygame.display.set_mode((SCREEN_SIZE), pygame.FULLSCREEN) if fullscreen else pygame.display.set_mode(
                    (1024, 576), pygame.RESIZABLE)
            if event.key == K_w:
                fadeout()
                weather()
                fadein()
                pygame.display.set_caption("Smart Table GUI")

    if fullscreen:
        win.blit(pygame.transform.scale(
            display, SCREEN_SIZE), (0, 0))
    else:
        win.blit(pygame.transform.scale(
            display, (scaled_win()[0])), scaled_win()[1])
    pygame.display.update()
    clock.tick(framerate)
