import os

# os.environ['SDL_VIDEODRIVER'] = "dummy"
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import io

from urllib.request import urlopen

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

    def write_centre(self, position, surface, text, font, size, y, color=(255, 255, 255), x=0):
        text_rect = font.get_rect(text, size=size)
        text_rect.center = (position[0] * 400 + self.width/2 + x, position[1] * 384 + self.height/2 + y)
        font.render_to(surface, text_rect, text, color, size=size)
