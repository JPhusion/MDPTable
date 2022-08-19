import os

# os.environ['SDL_VIDEODRIVER'] = "dummy"
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import io

from urllib.request import urlopen

from gui.widgets.widgets import widget
from scrapers.weather import *

class widget_weather(widget):

    def __init__(self, width=2, height=1, position=(0, 0)):
        self.width = width*400
        self.height = height*380
        self.position = position
        self.api_counter = 0
        
        self.font_200 = pygame.freetype.Font("./assets/fonts/FontsFree-Net-SFProDisplay-Bold.ttf", 200)
        self.font_32 = pygame.freetype.Font("./assets/fonts/FontsFree-Net-SFProDisplay-Bold.ttf", 32)

        self.descNow = "Sunny and Cloudy"
        self.tempNow = 0
        self.feelsNow = 0

    def draw(self, surface):
        self.draw_border(surface, self.position)
        # temp_text = f"{self.tempNow}°"
        # temp_pos = (self.position[0] * 400 + 80, self.position[1] * 380 + 80)
        # self.font_200.render_to(surface, temp_pos, temp_text, (255, 255, 255))
        # desc_text = f"{self.descNow}"
        # desc_pos = (self.position[0] * 400 + 80, self.position[1] * 380 + 300)
        # self.font_32.render_to(surface, desc_pos, desc_text, (255, 255, 255))
        # feels_text = f"Feels like: {self.feelsNow}°C"
        # feels_pos = (self.position[0] * 400 + 500, self.position[1] * 380 + 90)
        # self.font_32.render_to(surface, feels_pos, feels_text, (255, 255, 255))
        # icon_pos = (self.position[0] * 400 + 450, self.position[1] * 380 + 80)
        # surface.blit(pygame.transform.scale(self.icon, (300,300)), (icon_pos))
        self.draw_svg(self.position, surface, "./assets/weather_icons/weather_icons-01.svg", 400, 40, 40)
        
    def update(self, frame_count):
        if frame_count % 60 != 0:
            return
        data = call()
        self.descNow = descNow(data)
        self.tempNow = round(int(tempNow(data)), 3)
        self.feelsNow = round(int(feelsNow(data)), 3)
        self.icon =  pygame.image.load(io.BytesIO(urlopen(f"https://openweathermap.org/img/wn/{icon(data)}@2x.png").read()))
  