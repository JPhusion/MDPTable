import os

# os.environ['SDL_VIDEODRIVER'] = "dummy"
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

from gui.widgets.widgets import widget

from scrapers.covid import *

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
        