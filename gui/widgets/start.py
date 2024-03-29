import os

# os.environ['SDL_VIDEODRIVER'] = "dummy"
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

from gui.widgets.widgets import widget

class widget_start(widget):
    
    def __init__(self, width=1, height=1, position=(0, 0)):
        self.width = width*400
        self.height = height*380
        self.position = position
        
        self.loading_animation = []
        for i in range(15):
            self.loading_animation.append(pygame.transform.scale(pygame.image.load(
                f"./assets/animations/loading_grad/TABLEC_LOADING-{i+1}.png"), (342, 256)))
        
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
        # self.draw_border(surface, self.position)
        if frame_count < 30*1:
            self.loading(surface, frame_count)
            return
        self.write_centre(self.position, surface, f"Sign In", self.font_orkney, 100*scale, -62*scale)
        self.write_centre(self.position, surface, f"Press [ENTER] to bring up the command line", self.font_orkneyl, 30, 18*scale)
        self.write_centre(self.position, surface, f"Type \"Login [username (mdptable)]\" to login", self.font_orkneyl, 30, 80*scale)
