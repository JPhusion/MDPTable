import pygame
import sys
import io
from datetime import datetime
from urllib.request import urlopen
from pygame.locals import *
try:
    from api import *
except:
    from weather.api import *

def weather():
    # INITIATE WINDOW =========================================================== #
    clock = pygame.time.Clock()

    pygame.init()

    pygame.display.set_caption("Weather App")

    framerate = 60

    SCREEN_SIZE = (pygame.display.Info().current_w,
                pygame.display.Info().current_h)
    WINDOW_SIZE = (1024, 576)
    DISPLAY_SIZE = (1920, 1080)

    win = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
    display = pygame.Surface(DISPLAY_SIZE)

    # UPDATE DATA =============================================================== #
    def update():
        global icon
        global tempNow
        global feelsNow
        global descNow
        data = call()
        image_url = f"https://openweathermap.org/img/wn/{icon(data)}@2x.png"
        image_str = urlopen(image_url).read()
        image_file = io.BytesIO(image_str)
        icon = pygame.image.load(image_file)
        tempNow = tempNow(data)
        feelsNow = feelsNow(data)
        descNow = descNow(data)
        
    update()
    
    # INITIATE VARIABLE ========================================================= #
    fullscreen = False
    font = pygame.font.SysFont("Ariel", 48)

    # LOAD ASSETS =============================================================== #
    wallpaper = pygame.image.load("./assets/wallpaper/292342-landscape-lake.jpg")

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
        
        if int(datetime.now().strftime("%M"))%3 == 0:
            update()
            print("updated")

        text = font.render(f"{descNow}\nCurrent Temperature {tempNow}\nFeels Like {feelsNow}", True, "BLUE")
        display.blit(wallpaper, (0, 0))
        display.blit(icon, (100,100))
        display.blit(text, (200, 200))
        
        # display.blit(pygame.transform.scale(wallpaper, (scaled_win()[0])), scaled_win()[1])

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
                    return

        if fullscreen:
            win.blit(pygame.transform.scale(
                display, SCREEN_SIZE), (0, 0))
        else:
            win.blit(pygame.transform.scale(
                display, (scaled_win()[0])), scaled_win()[1])
        pygame.display.update()
        clock.tick(framerate)

if __name__ == "__main__":
    weather()
