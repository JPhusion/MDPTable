import os

# os.environ['SDL_VIDEODRIVER'] = "dummy"
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import io


class widget:

    def __init__(self, width, height, position=(0,0)):
        self.width = width*400
        self.height = height*384
        self.position = position

        self.loading_animation = []
        for i in range(15):
            self.loading_animation.append(pygame.transform.scale(pygame.image.load(
                f"./assets/animations/loading_grad/TABLEC_LOADING-{i+1}.png"), (342, 256)))

    def draw_border(self, surface, position=(0, 0)):
        origin = (position[0] * 400, position[1] * 384)
        pygame.draw.rect(surface, (255, 255, 255),
                         pygame.Rect(origin[0]+20, origin[1]+20, self.width-40, self.height-40))
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(
            origin[0]+24, origin[1]+24, self.width-48, self.height-48))

    def write_centre(self, position, surface, text, font, size, y, color=(255, 255, 255), x=0):
        text_rect = font.get_rect(text, size=size)
        text_rect.center = (
            position[0] * 400 + self.width/2 + x, position[1] * 384 + self.height/2 + y)
        font.render_to(surface, text_rect, text, color, size=size)

    def write(self, position, surface, text, font, size, x, y, color=(255, 255, 255)):
        text_rect = font.get_rect(text, size=size)
        text_rect.center = (position[0] * 400 + x, position[1] * 384 + y)
        font.render_to(surface, (x, y), text, color, size=size)

    def draw_svg(self, position, surface, filename, size, x, y, color=(255, 255, 255)):
        svg_string = open(filename, "rt").read()
        start = svg_string.find('<svg')
        if start > 0:
            svg_string1 = svg_string[:start+4] + \
                f' transform="scale({size/96})"' + svg_string[start+4:]
        svg_string2 = svg_string1.replace('width="96px"', f'width="{size}"')
        svg_string3 = svg_string2.replace('height="96px"', f'height="{size}"')
        image = pygame.image.load(io.BytesIO(svg_string3.encode()))
        arr = pygame.PixelArray(image)
        arr.replace((0, 0, 0), color)
        del arr
        surface.blit(image, (position[0] * 400 + x, position[1] * 384 + y))

    def loading(self, surface, frame_count):
        self.draw_border(surface, self.position)
        surface.blit(self.loading_animation[int(frame_count % len(self.loading_animation))],
                     (self.position[0] * 400 + self.width/2 - 171, self.position[1] * 384 + self.height/2 - 128))
