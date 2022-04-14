import pygame

pygame.init()
 
# THE MAIN SCREEN (surface)
WIDTH = HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Arial", 128)
clock = pygame.time.Clock()

def write(text, x, y, color="Coral",):
    "returns a text on a surface with the position in a rect"
    text = font.render(text, 0, pygame.Color(color))
    text_rect = text.get_rect(center=(WIDTH//2 + x, y))
    return text, text_rect

text, text_rect = write("Hello", 0, 70, (255, 255, 255))
text2, text_rect2 = write("World", 0, 180)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
    screen.blit(text, text_rect)
    screen.blit(text2, text_rect2)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
