import os

# os.environ['SDL_VIDEODRIVER'] = "dummy"
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

from scrapers.weather import *


class widget:

    def __init__(self, width, height):
        self.width = width*400
        self.height = height*384

    def draw_border(self, surface, position=(0, 0)):
        origin = (position[0] * 400, position[1] * 384)
        pygame.draw.rect(surface, (255, 255, 255),
                         pygame.Rect(origin[0]+20, origin[1]+20, self.width-40, self.height-40))
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(
            origin[0]+24, origin[1]+24, self.width-48, self.height-48))


class widget_weather(widget):

    def __init__(self, width, height):
        self.width = width*400
        self.height = height*384
        self.api_counter = 0
        
        self.font_200 = pygame.freetype.Font("./assets/fonts/FontsFree-Net-SFProDisplay-Bold.ttf", 200)
        self.font_32 = pygame.freetype.Font("./assets/fonts/FontsFree-Net-SFProDisplay-Bold.ttf", 32)

        self.descNow = "Sunny and Cloudy"
        self.tempNow = 0git
        self.feelsNow = 0

    def draw(self, surface, position=(0, 0)):
        self.draw_border(surface, position)
        temp_text = f"{self.tempNow}°C"
        temp_pos = (position[0] * 400 + 80, position[1] * 384 + 80)
        self.font_200.render_to(surface, temp_pos, temp_text, (255, 255, 255))
        desc_text = f"{self.descNow}"
        desc_pos = (position[0] * 400 + 80, position[1] * 384 + 300)
        self.font_32.render_to(surface, desc_pos, desc_text, (255, 255, 255))
        feels_text = f"Feels like: {self.feelsNow}°C"
        feels_pos = (position[0] * 400 + 500, position[1] * 384 + 90)
        self.font_32.render_to(surface, feels_pos, feels_text, (255, 255, 255))
        
    def update(self):
        data = call()
        self.descNow = descNow(data)
        self.tempNow = round(int(tempNow(data)), 3)
        self.feelsNow = round(int(feelsNow(data)), 3)