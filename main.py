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

while True:  # game's main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if current_display == "menu":
        texts("Press SPACE to begin", 500, 780, 30)
        game_logo = pygame.image.load(os.path.join("logo1.png"))
        screen.blit(game_logo, (450, 200))

    pygame.display.update()
