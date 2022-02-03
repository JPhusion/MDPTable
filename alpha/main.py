import pygame
import threading
import sys
import os
from pygame.locals import *
from weather.weather import *
from newapp.app import *
from browser import notion

# INITIATE WINDOW =========================================================== #
clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption("Smart Table GUI")

framerate = 60

SCREEN_SIZE = (pygame.display.Info().current_w,
               pygame.display.Info().current_h)
# WINDOW_SIZE = (1024, 576)
DISPLAY_SIZE = (1920, 1080)
WINDOW_SIZE = (1920, 1080)

win = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
display = pygame.Surface(DISPLAY_SIZE)

# INITIATE VARIABLE ========================================================= #
fullscreen = False
fadein = True
fadeout = False
loading_animation = []

# LOAD ASSETS =============================================================== #
wallpaper = pygame.image.load("./assets/wallpaper/wallpaperinuse.jpg")
loading = pygame.image.load("./assets/loading screen/loading.jpg")
for filename in os.listdir("./assets/loading screen/infinity-loader"):
    loading_animation.append(pygame.image.load(
        f"./assets/loading screen/infinity-loader/{filename}"))

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
loading_animation = []
for filename in os.listdir("./assets/loading screen/infinity-loader"):
    loading_animation.append(pygame.image.load(
        f"./assets/loading screen/infinity-loader/{filename}"))

loaded = False
loadframe = 0


def loading(start=0):
    global loadframe
    i = 0
    while not loaded:
        i += 1
        if start + i > 179:
            i = 0 - start
        win.fill((43, 45, 47))
        win.blit(loading_animation[start + i], (560, 240))
        pygame.display.update()
        clock.tick(framerate)
        loadframe = start + i


def fadein(start=0):
    frames = 32
    for i in range(frames):
        win.fill((43, 45, 47))
        win.blit(loading_animation[(start + i) % 179], (560, 240))
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
        win.fill((43, 45, 47))
        win.blit(loading_animation[179 - frames + i], (560, 240))
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
                threading.Thread(target=fadeout).start()
                threading.Thread(target=weather()).start()
                fadein()
                pygame.display.set_caption("Smart Table GUI")
            if event.key == K_a:
                threading.Thread(target=fadeout).start()
                threading.Thread(target=app()).start()
                fadein()
                pygame.display.set_caption("Smart Table GUI")
            if event.key == K_n:
                running = True
                threading.Thread(target=fadeout).start()
                notion()
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
