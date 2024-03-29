from commands.update import update as update_cmd
update_cmd()

from gui.widgets.weather import *
from gui.widgets.covid import *
from gui.widgets.clock import *
from gui.widgets.start import *
from commands.widget import widget as widget_cmd
from commands.signin import signin as signin_cmd

import pygame_textinput
import random
import os
import sys

# os.environ['SDL_VIDEODRIVER'] = "dummy"
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{-2},{-30}"
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

particles = []

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
    if 'login' in cmd.value:
        return signin_cmd()


def main():
    # instantiating display
    pygame.mixer.music.stop()
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
    widgets = [widget_start(3, 5, (0,0)), widget_start(3, 5, (3,0))]
    # widgets = [widget_clock(3, 5, (0,0)), widget_clock(3, 5, (3,0))]
    
    # program loop
    while True:

        if frame_count % 60 == 0:
            update_cmd()
            
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
                        if cmd.value.startswith('widget') or 'login' in cmd.value:
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
                if event.key == pygame.K_F2:
                    startup()
                            

        if fullscreen:
            win.blit(pygame.transform.scale(
                display, SCREEN_SIZE), (0, 0))
        else:
            win.blit(pygame.transform.scale(
                display, (scaled_win()[0])), scaled_win()[1])
        frame_count += 1
        pygame.display.update()
        clock.tick(framerate)

def update_particles(display):
    for particle in particles:
        try:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]*2
            particle[2] -= 0.03
            pygame.draw.circle(display, particle[3], [int(
                particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                particles.remove(particle)
        except ValueError:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]*2
            particle[2] -= 0.03
            pygame.draw.circle(display, (255, 255, 255), [int(
                particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                particles.remove(particle)

def startup():
    # instantiating display
    SCREEN_SIZE = (2400, 1920)
    DISPLAY_SIZE = (2400, 1920)
    WINDOW_SIZE = (2400, 1920)
    win = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
    display = pygame.Surface(DISPLAY_SIZE)

    # defining variables
    fullscreen = True
    frame_count = 0
    
    # starting sounds
    pygame.mixer.music.load("./assets/sounds/fire.mp3")
    pygame.mixer.music.play(loops=100000)
    
    # program loop
    while True:
        
        for i in range(20):
            # particles.append([[WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2], [random.randint(0, 1000)/100 - 5,
            #             random.randint(0, 1000)/100 - 5], random.randint(0, 10), (random.randint(100, 255), random.randint(0, 50), random.randint(0, 10))])
            particles.append([[random.randint(0, WINDOW_SIZE[0]), WINDOW_SIZE[1]], [random.randint(0, 1000)/100 - 5,
                        random.randint(0, 1000)/100 - 5], random.randint(0, 10), (random.randint(100, 255), random.randint(0, 50), random.randint(0, 10))])
        
        display.fill((0, 0, 0))
        update_particles(display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                if not fullscreen:
                    WINDOW_SIZE = (event.w, event.h)
                    win = pygame.display.set_mode(
                        WINDOW_SIZE, pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
        if fullscreen:
            win.blit(pygame.transform.scale(
                display, SCREEN_SIZE), (0, 0))
        else:
            win.blit(pygame.transform.scale(
                display, (scaled_win()[0])), scaled_win()[1])
        pygame.display.update()
        clock.tick(framerate)


if __name__ == "__main__":
    startup()
