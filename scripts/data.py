import pygame
from math import *
import AI
# menu data
black = (0, 0, 0)
white = (255, 255, 255)
# general data
fps = 300
field_of_view = pi / 2.5
accuracy_of_draw = 500
padding_of_rays = field_of_view / accuracy_of_draw
blockSize = 100
depth_of_field = blockSize * 50
object_scale_coefficient = 150

screen = pygame.display.set_mode((0, 0), flags=pygame.FULLSCREEN)
screen_width = screen.get_width()
screen_height = screen.get_height()

game_clock = pygame.time.Clock()

keys = {"forward": pygame.K_w, "left": pygame.K_a, "back": pygame.K_s, "right": pygame.K_d}

textures = {
    "b": pygame.image.load("images/textures/brick_wall.jpg").convert(),
    "r": pygame.image.load("images/textures/ruins.png").convert_alpha(),
    "e": pygame.image.load("images/textures/enemy.jpg").convert_alpha(),
    "t": pygame.image.load("images/textures/table.png").convert_alpha(),
    "c": pygame.image.load("images/textures/chair.png").convert_alpha()
}

bots = [AI.Bot(10, 20, 0.03) ]

# map data
# b - Brick wall
# e - enemy
# r - ruins
# c - chair
# t - table

flat_objects_prefabs = {
    "environment": ["r", "c", "t"],
    "enemies": ["e"]}

map = [
    "bbbbbbbbbbbb           ",
    "b        r b           ",
    "b    r    rb           ",
    "b          bbbbbb      ",
    "b               b      ",
    "br         b    b      ",
    "b r       rb    b      ",
    "bbbbbbbbbbbbb bbbbbbbbb",
    "       b              b",
    "       b ctc          b",
    "       bbbbbbbbbbbb bbb",
    "                b     b",
    "                b e   b",
    "                b   e b",
    "                bb    b",
    "                b    bb",
    "                b     b",
    "            bbbbbb bbbb",
    "            b         b",
    "            b         b",
    "            br e      b",
    "            b r  e    b",
    "            bbbbbbbbbbb"]


enemies = []
environment = []
worldMap = dict()
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] != " " and map[y][x] not in flat_objects_prefabs["environment"] and map[y][x] not in flat_objects_prefabs["enemies"]:
            worldMap[(x * blockSize, y * blockSize)] = map[y][x]
        if map[y][x] in flat_objects_prefabs["enemies"]:
            enemies.append([x, y])
        elif map[y][x] in flat_objects_prefabs["environment"]:
            environment.append([x, y])

distance_from_screen = accuracy_of_draw / (2 * tan(field_of_view / 2))
projection_coefficient = screen_height * 0.01 / accuracy_of_draw * 200
ray_thickness = screen_width / accuracy_of_draw

textureWidth = 800
textureHeight = 800
textureScale = textureWidth / blockSize
