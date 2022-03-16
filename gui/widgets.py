import os

# os.environ['SDL_VIDEODRIVER'] = "dummy"
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import io

from urllib.request import urlopen

from scrapers.weather import *
from scrapers.clock import *
from scrapers.covid import *


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

    def __init__(self, width=2, height=1):
        self.width = width*400
        self.height = height*384
        self.api_counter = 0
        
        self.font_200 = pygame.freetype.Font("./assets/fonts/FontsFree-Net-SFProDisplay-Bold.ttf", 200)
        self.font_32 = pygame.freetype.Font("./assets/fonts/FontsFree-Net-SFProDisplay-Bold.ttf", 32)

        self.descNow = "Sunny and Cloudy"
        self.tempNow = 0
        self.feelsNow = 0

    def draw(self, surface, position=(0, 0)):
        self.draw_border(surface, position)
        temp_text = f"{self.tempNow}°"
        temp_pos = (position[0] * 400 + 80, position[1] * 384 + 80)
        self.font_200.render_to(surface, temp_pos, temp_text, (255, 255, 255))
        desc_text = f"{self.descNow}"
        desc_pos = (position[0] * 400 + 80, position[1] * 384 + 300)
        self.font_32.render_to(surface, desc_pos, desc_text, (255, 255, 255))
        feels_text = f"Feels like: {self.feelsNow}°C"
        feels_pos = (position[0] * 400 + 500, position[1] * 384 + 90)
        self.font_32.render_to(surface, feels_pos, feels_text, (255, 255, 255))
        icon_pos = (position[0] * 400 + 450, position[1] * 384 + 80)
        surface.blit(pygame.transform.scale(self.icon, (300,300)), (icon_pos))
        
    def update(self):
        data = call()
        self.descNow = descNow(data)
        self.tempNow = round(int(tempNow(data)), 3)
        self.feelsNow = round(int(feelsNow(data)), 3)
        self.icon =  pygame.image.load(io.BytesIO(urlopen(f"https://openweathermap.org/img/wn/{icon(data)}@2x.png").read()))
        

class widget_time(widget):
    
    def __init__(self, width=1, height=1):
        self.width = width*400
        self.height = height*384
        
        self.font_100 = pygame.freetype.Font("./assets/fonts/FontsFree-Net-SFProDisplay-Bold.ttf", 100)
        self.font_32 = pygame.freetype.Font("./assets/fonts/FontsFree-Net-SFProDisplay-Bold.ttf", 42)
        
    def draw(self, surface, position=(0, 0)):
        self.draw_border(surface, position)
        text = f":"
        pos = (position[0] * 400 + self.width/2 - 10, position[1] * 384 + 80)
        self.font_100.render_to(surface, pos, text, (255, 255, 255))
        hour_text = f"{hour()}"
        hour_pos = (position[0] * 400 + self.width/2 - 130, position[1] * 384 + 70)
        self.font_100.render_to(surface, hour_pos, hour_text, (255, 255, 255))
        minutes_text = f"{minutes()}"
        minutes_pos = (position[0] * 400 + self.width/2 + 25, position[1] * 384 + 70)
        self.font_100.render_to(surface, minutes_pos, minutes_text, (255, 255, 255))
        seconds_text = f"{seconds()}"
        seconds_pos = (position[0] * 400 + self.width/2 - 30, position[1] * 384 + 180)
        self.font_32.render_to(surface, seconds_pos, seconds_text, (255, 255, 255))
        seconds_text = f"{date()}"
        seconds_pos = (position[0] * 400 + self.width/2 - 130, position[1] * 384 + 280)
        self.font_32.render_to(surface, seconds_pos, seconds_text, (255, 255, 255))
        
class widget_covid(widget):
    
    def __init__(self, width=1, height=1):
        self.width = width*400
        self.height = height*384
        
        self.font_100 = pygame.freetype.Font("./assets/fonts/FontsFree-Net-SFProDisplay-Bold.ttf", 100)
        self.font_32 = pygame.freetype.Font("./assets/fonts/FontsFree-Net-SFProDisplay-Bold.ttf", 32)
        
        self.cases = False
        self.last_updated = False
        self.deaths = False
        self.tests = False
        self.vaccines = False
        
    def draw(self, surface, position=(0, 0)):
        self.draw_border(surface, position)
        test_cases = f"New Cases: {self.cases}"
        cases_pos = (position[0] * 400 + self.width/2 - 10, position[1] * 384 + 80)
        self.font_32.render_to(surface, cases_pos, test_cases, (255, 255, 255))
        hour_text = f"Deaths: {self.deaths}"
        hour_pos = (position[0] * 400 + self.width/2 - 130, position[1] * 384 + 70)
        self.font_32.render_to(surface, hour_pos, hour_text, (255, 255, 255))
        minutes_text = f"Tests: {self.tests}"
        minutes_pos = (position[0] * 400 + self.width/2 + 25, position[1] * 384 + 70)
        self.font_32.render_to(surface, minutes_pos, minutes_text, (255, 255, 255))
        seconds_text = f"Vaccinated: {self.vaccines}"
        seconds_pos = (position[0] * 400 + self.width/2 - 30, position[1] * 384 + 180)
        self.font_32.render_to(surface, seconds_pos, seconds_text, (255, 255, 255))
        seconds_text = f"{self.last_updated}"
        seconds_pos = (position[0] * 400 + self.width/2 - 130, position[1] * 384 + 280)
        self.font_32.render_to(surface, seconds_pos, seconds_text, (255, 255, 255))
    
    def update(self):
        sp = get_soup()
        self.last_updated = time_update(sp)
        self.cases = det_cases(sp, 'daily')
        self.deaths = det_health(sp, 'deaths_d')
        self.tests = det_tests(sp, 'daily')
        self.vaccines = det_vaccines(sp, 'pc_second')
        