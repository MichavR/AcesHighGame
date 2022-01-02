import os
import pygame
import random
import time


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


def counter():
    t = 3
    while t:
        time.sleep(1)
        t -= 1
    return t


current_display = "get_ready"


class Obstacle:
    def __init__(self, x, width):
        self.x = x
        self.width = width
        self.y_upper = 0
        self.height_upper = random.randint(250, 500)
        self.space = 290
        self.y_lower = self.height_upper + self.space
        self.height_lower = (screen_height / 0.5) - self.y_lower
        self.color = (0, 102, 153)
        self.shape_upper = pygame.Rect(self.x, self.y_upper, self.width, self.height_upper)
        self.shape_lower = pygame.Rect(self.x, self.y_lower, self.width, self.height_lower)

    def draw_obstacle(self):
        pygame.draw.rect(screen, self.color, self.shape_upper, 0)
        pygame.draw.rect(screen, self.color, self.shape_lower, 0)

    def obstacle_movement(self, v):
        self.x = self.x - v
        self.shape_upper = pygame.Rect(self.x, self.y_upper, self.width, self.height_upper)
        self.shape_lower = pygame.Rect(self.x, self.y_lower, self.width, self.height_lower)


class Plane:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 77
        self.shape = pygame.Rect(self.x, self.y, self.width-5, self.height-5)
        self.pic = pygame.image.load(os.path.join('img/plane.png'))

    def draw_plane(self):
        screen.blit(self.pic, (self.x, self.y))

    def plane_movement(self, v):
        self.y = self.y + v


obstacles = []

for i in range(21):
    obstacles.append(Obstacle(i * screen_width / 20, screen_width / 20))

player = Plane(620, 475)
dy = 0
points = 0

while True:  # game's main loop
    for event in pygame.event.get():
        dy = +0.23
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy = -0.5
            if event.key == pygame.K_DOWN:
                dy = +0.5

    screen.fill((0, 0, 0))
    if current_display == "menu":  # game's main screen
        texts("Press SPACE to begin", 500, 780, 30)
        game_logo = pygame.image.load(os.path.join("img/logo1.png"))
        screen.blit(game_logo, (450, 200))

    elif current_display == "get_ready":
        for p in obstacles:
            p.draw_obstacle()
        for p in obstacles:
            if p.x <= - p.width:
                obstacles.remove(p)
                obstacles.append(Obstacle(screen_width, screen_width/20))

        player.draw_plane()
        pygame.display.update()
        if counter() == 0:
            current_display = "gameplay"

    elif current_display == "gameplay":
        for p in obstacles:
            p.obstacle_movement(1)
            p.draw_obstacle()
        for p in obstacles:
            if p.x <= - p.width:
                obstacles.remove(p)
                obstacles.append(Obstacle(screen_width, screen_width / 20))

        player.draw_plane()
        player.plane_movement(dy)

    pygame.display.update()
