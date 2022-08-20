import os

# os.environ['SDL_VIDEODRIVER'] = "dummy"
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

from gui.widgets.widgets import widget

from scrapers.covid import *

class widget_covid(widget):
    
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
        
        self.cases = None
        self.last_updated = None
        self.deaths = None
        self.tests = None
        self.vaccines = None
        
        self.loading_animation = []
        for i in range(15):
            self.loading_animation.append(pygame.transform.scale(pygame.image.load(
                f"./assets/animations/loading_grad/TABLEC_LOADING-{i+1}.png"), (342, 256)))
        
    def draw(self, surface, frame_count):
        if self.cases is None:
            self.loading(surface, frame_count)
            return
        scale = min(self.width / 400, self.height / 380)
        self.draw_border(surface, self.position)
        self.write_centre(self.position, surface, f"Covid Update - NSW", self.font_orkneyb, 30*scale, -102*scale)
        self.write_centre(self.position, surface, f"Cases: {self.cases}", self.font_orkneyl, 25*scale, -52*scale)
        self.write_centre(self.position, surface, f"Deaths: {self.deaths}", self.font_orkneyl, 25*scale, 2*scale)
        self.write_centre(self.position, surface, f"Tests: {self.tests}", self.font_orkneyl, 25*scale, 52*scale)
        self.write_centre(self.position, surface, f"Vaccinated: {self.vaccines}", self.font_orkneyl, 27*scale, 100*scale)
        self.write(self.position, surface, f"Last Updated: {self.last_updated}", self.font_orkneyl, 16*scale, 40*scale + (self.position[0] - 1)*400, 335*(self.height / 380)+380*(self.position[1]))
    
    def update(self, frame_count):
        if frame_count % 60 != 0:
            return
        sp = get_soup()
        self.last_updated = time_update(sp)
        self.cases = det_cases(sp, 'daily')
        self.deaths = det_health(sp, 'deaths_d')
        self.tests = det_tests(sp, 'daily')
        self.vaccines = det_vaccines(sp, 'pc_second')
        