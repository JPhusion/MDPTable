import os

# os.environ['SDL_VIDEODRIVER'] = "dummy"
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

from gui.widgets.widgets import widget

from scrapers.clock import *

class widget_clock(widget):
    
    def __init__(self, width=1, height=1, position=(0, 0)):
        self.width = width*400
        self.height = height*380
        self.position = position
        
        self.font = pygame.freetype.Font("./assets/fonts/FontsFree-Net-SFProDisplay-Bold.ttf")
        self.font_kontanter = pygame.freetype.Font("./assets/fonts/Kontanter-Bold.otf")
        self.font_bondi = pygame.freetype.Font("./assets/fonts/Bondi.ttf")
        self.font_potra = pygame.freetype.Font("./assets/fonts/Potra 300.ttf")
        self.font_orkney = pygame.freetype.Font("./assets/fonts/Orkney Regular.ttf")
        self.font_orkneyl = pygame.freetype.Font("./assets/fonts/Orkney Light.ttf")
        self.font_orkneym = pygame.freetype.Font("./assets/fonts/Orkney Medium.ttf")
        self.font_orkneyb = pygame.freetype.Font("./assets/fonts/Orkney Bold.ttf")
        
    def draw(self, surface, frame_count):
        scale = min(self.width / 400, self.height / 380)
        self.draw_border(surface, self.position)
        self.write_centre(self.position, surface, f"{hour()}:{minutes()}", self.font_bondi, 100*scale, -62*scale)
        self.write_centre(self.position, surface, f"{seconds()}", self.font_orkneyl, 30*scale, 18*scale)
        self.write_centre(self.position, surface, f"{date(True)}", self.font_orkneyl, 35*scale, 88*scale)
