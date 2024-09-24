import os

# os.environ['SDL_VIDEODRIVER'] = "dummy"
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

from gui.widgets.widgets import widget

from googleapi.gcal import get_formatted_events


class widget_cal(widget):

    def __init__(self, width=1, height=1, position=(0, 0)):
        self.width = width * 400
        self.height = height * 380
        self.position = position

        self.font = pygame.freetype.Font(
            "./assets/fonts/FontsFree-Net-SFProDisplay-Bold.ttf"
        )
        self.font_kontanter = pygame.freetype.Font("./assets/fonts/Kontanter-Bold.otf")
        self.font_bondi = pygame.freetype.Font("./assets/fonts/Bondi.ttf")
        self.font_potra = pygame.freetype.Font("./assets/fonts/Potra 300.ttf")
        self.font_orkney = pygame.freetype.Font("./assets/fonts/Orkney Regular.ttf")
        self.font_orkneyl = pygame.freetype.Font("./assets/fonts/Orkney Light.ttf")
        self.font_orkneym = pygame.freetype.Font("./assets/fonts/Orkney Medium.ttf")
        self.font_orkneyb = pygame.freetype.Font("./assets/fonts/Orkney Bold.ttf")

        self.events = None

        self.loading_animation = []
        for i in range(15):
            self.loading_animation.append(
                pygame.transform.scale(
                    pygame.image.load(
                        f"./assets/animations/loading_grad/TABLEC_LOADING-{i+1}.png"
                    ),
                    (342, 256),
                )
            )

    def draw(self, surface, frame_count):
        if self.events is None:
            self.loading(surface, frame_count)
            return
        scale = min(self.width / 400, self.height / 380)
        self.draw_border(surface, self.position)
        self.write_centre(
            self.position,
            surface,
            f"Upcoming Events",
            self.font_orkneyb,
            25 * scale,
            -150 * scale,
        )
        if len(self.events) < 1:
            self.write_centre(
                self.position,
                surface,
                f"No Events",
                self.font_orkneyb,
                15 * scale,
                0 * scale,
            )
        counter = 0
        for event in self.events:
            if counter > 5:
                break
            self.write_centre(
                self.position,
                surface,
                f"{event[0]}",
                self.font_orkneyb,
                15 * scale,
                -100 * scale + counter * 120,
            )
            self.write_centre(
                self.position,
                surface,
                f"{event[1]} at {event[2]}",
                self.font_orkneyb,
                10 * scale,
                -85 * scale + counter * 120,
            )
            counter += 1

    def update(self, frame_count):
        if frame_count % 60 != 0:
            return
        # self.events = list(get_formatted_events())
        self.events = [
            ["Hardware Flex", "Now", "EETG14"],
            ["Pubcrawl with Friends", "9pm", "The Argyle, The Rocks"],
            # ["MATH2069 Tutorial", "Tomorrow 12pm", "H13 Lawernce East 1041"],
            ["MATH2069 Lecture", "Tomorrow 2pm", "Keith Burrows Theatre"],
            ["Bouldering with Eric", "Tomorrow 5pm", "ClimbFit Macquarie"],
            ["rUNSWift Lab Session", "Saturday 10am", "Ainsworth Level 5"],
        ]
