# Test to see if it auto update - ignore this comment

from gui.widgets.weather import *
from gui.widgets.covid import *
from gui.widgets.clock import *
from gui.widgets.start import *
from commands.widget import widget as widget_cmd
from commands.update import update as update_cmd

import pygame_textinput
import os
import sys

# os.environ['SDL_VIDEODRIVER'] = "dummy"
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{-10},{-30}"
os.environ['PYGAME_FREETYPE'] = '1'

import pygame
import pygame.freetype

# init window
clock = pygame.time.Clock()
pygame.init()
pygame.key.set_repeat(400, 25)
pygame.display.set_caption("Smart Table GUI")
framerate = 30

SCREEN_SIZE = (2400, 1920)
DISPLAY_SIZE = (2400, 1920)
WINDOW_SIZE = (2400, 1920)
win = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
display = pygame.Surface(DISPLAY_SIZE)

cmd_font = pygame.font.Font("./assets/fonts/JetBrainsMonoNL-Regular.ttf", 16)
cmd = pygame_textinput.TextInputVisualizer(font_color=(255, 255, 255), cursor_color=(
    255, 255, 255), cursor_blink_interval=500, cursor_width=2, antialias=True, font_object=cmd_font)
cmd_bullet = pygame_textinput.TextInputVisualizer(font_color=(255, 255, 255), cursor_color=(
    255, 255, 255), cursor_width=2, antialias=True, font_object=cmd_font)
cmd_bullet.cursor_visible = False
cmd_bullet.value = ""


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


def process_cmd(widgets):
    if cmd.value.startswith('widget'):
        return widget_cmd(cmd.value, widgets)
    if cmd.value == 'update':
        return update_cmd()


def main():
    # instantiating display
    SCREEN_SIZE = (2400, 1920)
    DISPLAY_SIZE = (2400, 1920)
    WINDOW_SIZE = (2400, 1920)
    win = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
    display = pygame.Surface(DISPLAY_SIZE)

    # defining variables
    fullscreen = True
    cmd_active = False
    frame_count = 0
    cmd_hist = []
    cmd_hist_popped = []

    # instantiating widgets
    # widgets = [widget_covid(3, 2, (0,3)), widget_covid(3, 2, (0,0))]
    # widgets = [widget_start(3, 5, (0,0)), widget_start(3, 5, (3,0))]
    widgets = [widget_clock(3, 5, (0,0)), widget_clock(3, 5, (3,0))]
    
    # program loop
    while True:

        # reset frame
        display.fill((0, 0, 0))
        events = pygame.event.get()

        # Command prompt location
        display.blit(cmd.surface, (60, 1890))
        display.blit(cmd_bullet.surface, (20, 1890))

        # Command prompt event handler
        if cmd_active:
            cmd.update(events)

        # draw widgets and update
        for widget in widgets:
            widget.draw(display, frame_count)
            widget.update(frame_count)

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                if not fullscreen:
                    WINDOW_SIZE = (event.w, event.h)
                    win = pygame.display.set_mode(
                        WINDOW_SIZE, pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    fullscreen = not fullscreen
                    win = pygame.display.set_mode((SCREEN_SIZE), pygame.FULLSCREEN) if fullscreen else pygame.display.set_mode(
                        (1080, 1920), pygame.RESIZABLE)
                if event.key == pygame.K_RETURN:
                    if cmd_active:
                        cmd_hist.append(cmd.value)
                        if cmd.value.startswith('widget'):
                            widgets = process_cmd(widgets)
                        else:
                            process_cmd(widgets)
                        cmd.value = ""
                        cmd.cursor_visible = False
                        cmd_bullet.value = ""
                    else:
                        cmd_active = True
                        cmd_bullet.value = ">>> "
                        cmd_bullet.cursor_visible = False
                if event.key == pygame.K_ESCAPE:
                    cmd_active = False
                    cmd_bullet.cursor_visible = False
                    cmd.value = ""
                    cmd.cursor_visible = False
                    cmd_bullet.value = ""
                if event.key == pygame.K_UP:
                    if cmd_active:
                        if len(cmd_hist) > 0:
                            cmd.value = cmd_hist[-1]
                            cmd_hist_popped.append(cmd_hist.pop())
                if event.key == pygame.K_DOWN:
                    if cmd_active:
                        if len(cmd_hist_popped) > 0:
                            cmd.value = cmd_hist_popped[-1]
                            cmd_hist.append(cmd_hist_popped[-1]) 
                            cmd_hist_popped.pop()
                            

        if fullscreen:
            win.blit(pygame.transform.scale(
                display, SCREEN_SIZE), (0, 0))
        else:
            win.blit(pygame.transform.scale(
                display, (scaled_win()[0])), scaled_win()[1])
        frame_count += 1
        pygame.display.update()
        clock.tick(framerate)


def loading_screen():
    # instantiating display
    SCREEN_SIZE = (2400, 1920)
    DISPLAY_SIZE = (2400, 1920)
    WINDOW_SIZE = (2400, 1920)
    win = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
    display = pygame.Surface(DISPLAY_SIZE)

    # defining variables
    fullscreen = True
    frame_count = 0
    loading_animation = []
    for i in range(15):
        loading_animation.append(pygame.image.load(
            f"./assets/animations/loading_grad/TABLEC_LOADING-{i+1}.png"))
    
    # program loop
    while True:
        
        display.fill((0, 0, 0))
        display.blit(loading_animation[int(frame_count%len(loading_animation))], (0, 0))
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                if not fullscreen:
                    WINDOW_SIZE = (event.w, event.h)
                    win = pygame.display.set_mode(
                        WINDOW_SIZE, pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    fullscreen = not fullscreen
                    win = pygame.display.set_mode((SCREEN_SIZE), pygame.FULLSCREEN) if fullscreen else pygame.display.set_mode(
                        (1080, 1920), pygame.RESIZABLE)
        frame_count += 1
        if fullscreen:
            win.blit(pygame.transform.scale(
                display, SCREEN_SIZE), (0, 0))
        else:
            win.blit(pygame.transform.scale(
                display, (scaled_win()[0])), scaled_win()[1])
        pygame.display.update()
        clock.tick(framerate)


if __name__ == "__main__":
    main()
