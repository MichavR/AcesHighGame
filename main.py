import random
import pygame
import os

pygame.init()

# game window res setting
screen_width = 1280
screen_height = 1024
screen = pygame.display.set_mode((screen_width, screen_height))


def texts(txt, x, y, size):  # ingame texts function, default position: middle
    game_font = pygame.font.SysFont("Arial", size)
    txt_render = game_font.render(txt, True, (0, 200, 255))
    # x = (screen_width - txt_render.get_rect().width) / 2
    # y = (screen_height - txt_render.get_rect().height) / 2
    screen.blit(txt_render, (x, y))


current_display = "menu"


class Obstacle:
    def __init__(self, x, width):
        self.x = x
        self.width = width
        self.y_upper = 0
        self.height_upper = random.randint(150, 250)
        self.space = 100
        self.y_lower = self.height_upper + self.space
        self.height_lower = screen_height - self.y_lower
        self.color = (3, 252, 132)


while True:  # game's main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if current_display == "menu":  # game's main screen
        texts("Press SPACE to begin", 500, 780, 30)
        game_logo = pygame.image.load(os.path.join("logo1.png"))
        screen.blit(game_logo, (450, 200))

    pygame.display.update()
