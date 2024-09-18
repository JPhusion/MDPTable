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
        self.font = pygame.freetype.Font("./assets/fonts/FontsFree-Net-SFProDisplay-Bold.ttf")
        self.font_kontanter = pygame.freetype.Font("./assets/fonts/Kontanter-Bold.otf")
        self.font_bondi = pygame.freetype.Font("./assets/fonts/Bondi.ttf")
        self.font_potra = pygame.freetype.Font("./assets/fonts/Potra 300.ttf")
        self.font_orkney = pygame.freetype.Font("./assets/fonts/Orkney Regular.ttf")
        self.font_orkneyl = pygame.freetype.Font("./assets/fonts/Orkney Light.ttf")
        self.font_orkneym = pygame.freetype.Font("./assets/fonts/Orkney Medium.ttf")
        self.font_orkneyb = pygame.freetype.Font("./assets/fonts/Orkney Bold.ttf")

        self.descNow = "Loading..."
        self.tempNow = 0
        self.feelsNow = 0
        self.icon = None
        
        self.loading_animation = []
        for i in range(15):
            self.loading_animation.append(pygame.transform.scale(pygame.image.load(
                f"./assets/animations/loading_grad/TABLEC_LOADING-{i+1}.png"), (342, 256)))

    def draw(self, surface, frame_count):
        self.draw_border(surface, self.position)
        if self.icon is None:
            self.loading(surface, frame_count)
            return
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
        scale = min(self.width / 400, self.height / 380)
        self.write_centre(self.position, surface, f"Live Weather", self.font_orkneyb, 30*scale, -120*scale)
        self.write_centre(self.position, surface, f"{self.descNow}", self.font_orkneyl, 25*scale, -58*scale)
        self.write_centre(self.position, surface, f"Temperature: {self.tempNow}°C", self.font_orkneyl, 25*scale, 85*scale)
        self.write_centre(self.position, surface, f"Feels Like: {self.tempNow}°C", self.font_orkneyl, 25*scale, 120*scale)
        # self.write_centre(self.position, surface, f"Icon: {self.icon}", self.font_orkneyl, 27*scale, 100*scale)
        # self.draw_svg(self.position, surface, f"./assets/weather_icons/{self.icon}.svg", 130*scale, self.width/2 - 180*scale/2  + 30*scale, 140*scale)
        
    def update(self, frame_count):
        if frame_count % 60 != 0:
            return
        # data = call()
        # self.descNow = descNow(data)
        # self.tempNow = round(int(tempNow(data)), 3)
        # self.feelsNow = round(int(feelsNow(data)), 3)
        # self.icon =  pygame.image.load(io.BytesIO(urlopen(f"https://openweathermap.org/img/wn/{icon(data)}@2x.png").read()))
        # self.icon =  icon(data)
        # # self.icon =  icon()
        self.descNow = "Partly Cloudy"
        self.tempNow = 26
        self.feelsNow = 27
        self.icon = "10d"
  
