from pygame import *
import pygame
from math import *
import sys

# menu data
black = (0, 0, 0)
white = (255, 255, 255)
# general data
screen_width = 1536
screen_height = screen_width // 16 * 9
screen_size = (screen_width, screen_height)
fps = 60
field_of_view = pi / 2.5
accuracy_of_draw = 750
padding_of_rays = field_of_view / accuracy_of_draw
depth_of_field = screen_width

textures = {
    "1": pygame.image.load("images/textures/1.jpg"),
    "2": pygame.image.load("images/textures/2.jpg"),
    "3": pygame.image.load("images/textures/3.jpg"),
    "4": pygame.image.load("images/textures/4.jpg")}
# background1 = pygame.image.load("images/background1.jpeg")
# background2 = pygame.image.load("images/background1.jpeg")

keys = {"forward": pygame.K_w, "left": pygame.K_a, "back": pygame.K_s, "right": pygame.K_d}

# map data
map = [
    "1111111111111111",
    "14      3     41",
    "1    11    22221",
    "1            3 1",
    "1            3 1",
    "1222   2222    1",
    "14            41",
    "1111111111111111"]

blockSize = 100

worldMap = dict()
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] != " ":
            worldMap[(x * blockSize, y * blockSize)] = map[y][x]

distance_from_screen = accuracy_of_draw / (2 * tan(field_of_view / 2))
projection_coefficient = screen_height * 0.01 / accuracy_of_draw * 200
ray_thickness = screen_width / accuracy_of_draw

miniMapScale = 4

textureWidth = 800
textureHeight = 800
textureScale = textureWidth / blockSize
