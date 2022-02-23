import os

# os.environ['SDL_VIDEODRIVER'] = "dummy"
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

from scrapers.weather import *


class widget:

    def __init__(self, width, height):
        self.width = width*400
        self.height = height*384

    def draw(self, surface, position=(0, 0)):
        origin = (position[0] * 400, position[1] * 384)
        pygame.draw.rect(surface, (255, 255, 255),
                         pygame.Rect(origin[0]+20, origin[1]+20, self.width-40, self.height-40))
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(
            origin[0]+24, origin[1]+24, self.width-48, self.height-48))


class widget_weather:

    def __init__(self, width, height):
        self.width = width*400
        self.height = height*384
        self.api_counter = 0

        self.descNow = 0
        self.tempNow = 0
        self.feelsNow = 0

    def draw(self, surface, position=(0, 0)):
        origin = (position[0] * 400, position[1] * 384)
        pygame.draw.rect(surface, (255, 255, 255),
                         pygame.Rect(origin[0]+20, origin[1]+20, self.width-40, self.height-40))
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(
            origin[0]+24, origin[1]+24, self.width-48, self.height-48))

        text = pygame.font.render(
            f"{self.descNow}\nCurrent Temperature {self.tempNow}\nFeels Like {self.feelsNow}", True, "BLUE")
