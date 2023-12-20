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
    "c": pygame.image.load("images/textures/breakable_brick_wall.jpg").convert(),
    "r": pygame.image.load("images/textures/brick_wall_rusty.jpg").convert(),
    "d": pygame.image.load("images/textures/brick_wall_with_board.jpg").convert(),
    "background": pygame.image.load("images/background.png").convert(),
    "alive_enemy": [pygame.image.load("images/alive_enemy/" + str(x) + ".png").convert_alpha() for x in range(1, 16)],
    "hurt_enemy": [pygame.image.load("images/hurt_enemy/" + str(x) + ".png").convert_alpha() for x in range(1, 27)],
    "dead_enemy": [pygame.image.load("images/dead_enemy/" + str(x) + ".png").convert_alpha() for x in range(1, 31)]
}


# map data
# b - Brick wall

flat_objects_prefabs = []

map = [
    "bbbbbbrrrbbb           ",
    "b          b           ",
    "b          d           ",
    "b          bbccbb      ",
    "r               b      ",
    "r e     e  b    c      ",
    "b     e    d    b      ",
    "bbbcbbrrrrbbb bbbbbbbbb",
    "       b              b",
    "       b              b",
    "       bbbbbbbbbbbb bbb",
    "                b     b",
    "                b     b",
    "                b     b",
    "                bb    b",
    "                b    bb",
    "                b     b",
    "            bbbbbb bbbb",
    "            b         b",
    "            b         b",
    "            b         b",
    "            b         b",
    "            bbbbbbbbbbb"]


def convert_map_to_list(cur_map):
    res_map = []
    for y in range(len(cur_map)):
        line = []
        for x in range(len(cur_map[0])):
            line.append(cur_map[y][x])
        res_map.append(line)
    return res_map


map = convert_map_to_list(map)


enemies = dict()
environment = []
worldMap = dict()
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] != " " and map[y][x] != "e" and map[y][x] not in flat_objects_prefabs:
            worldMap[(x * blockSize, y * blockSize)] = map[y][x]
        elif map[y][x] == "e":
            enemies[(x, y)] = AI.Enemy((x, y), 10, 100)
        elif map[y][x] in flat_objects_prefabs:
            environment.append([x, y])

distance_from_screen = accuracy_of_draw / (2 * tan(field_of_view / 2))
projection_coefficient = screen_height * 0.01 / accuracy_of_draw * 200
ray_thickness = screen_width / accuracy_of_draw

textureWidth = 800
textureHeight = 800
textureScale = textureWidth / blockSize
