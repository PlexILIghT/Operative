import pygame
from math import *
import AI

pygame.init()

volume = 0.5

# menu data
back_flag = False
mein_menu_flag = False
dead = False
tryagain = False
win_flag = False
last_time = 0

# general data
fps = 300
field_of_view = pi / 2.5
accuracy_of_draw = 500
padding_of_rays = field_of_view / accuracy_of_draw
blockSize = 100
depth_of_field = blockSize * 50
object_scale_coefficient = 150

# fonts
font = pygame.font.Font("fonts/Disket-Mono-Regular.ttf", 50)
font2 = pygame.font.Font("fonts/Lazer-Game-Zone.ttf", 100)

screen = pygame.display.set_mode((1920, 1080))
screen_width = screen.get_width()
screen_height = screen.get_height()

game_clock = pygame.time.Clock()

keys = {"forward": pygame.K_w, "left": pygame.K_a, "back": pygame.K_s, "right": pygame.K_d}

textures = {
    "b": pygame.image.load("images/textures/brick_wall.jpg").convert(),
    "c": pygame.image.load("images/textures/breakable_brick_wall.jpg").convert(),
    "r": pygame.image.load("images/textures/brick_wall_rusty.jpg").convert(),
    "d": pygame.image.load("images/textures/brick_wall_with_board.jpg").convert(),
    "f": pygame.image.load("images/textures/door.png").convert(),
    "g": pygame.image.load("images/textures/metal_door.jpg").convert(),
    "x": pygame.image.load("images/textures/dungeon_door.jpg").convert(),
    "w": pygame.image.load("images/textures/cases1.png").convert_alpha(),
    "q": pygame.image.load("images/textures/cases2.png").convert_alpha(),
    "m": pygame.image.load("images/textures/metal_wall1.jpg").convert_alpha(),
    "background": pygame.image.load("images/background.png").convert(),
    "blood": pygame.image.load("images/blood.png").convert_alpha(),
    "alive_enemy": [pygame.image.load("images/alive_enemy/" + str(x) + ".png").convert_alpha() for x in range(1, 16)],
    "hurt_enemy": [pygame.image.load("images/hurt_enemy/" + str(x) + ".png").convert_alpha() for x in range(1, 27)],
    "dead_enemy": [pygame.image.load("images/dead_enemy/" + str(x) + ".png").convert_alpha() for x in range(1, 31)]
}

# scale settings for sprites
weapon_scale_width = screen_width / (screen_width * 2)
weapon_scale_height = screen_height / (screen_height * 2)
weapon_melee_scale_width = screen_width/(screen_width * 0.5)
weapon_melee_scale_height = screen_height/(screen_height * 0.5)

m4_shot = [pygame.transform.smoothscale(pygame.image.load(f"images/m4_shot/{i}.png"), (pygame.image.load(f"images/m4_shot/{i}.png").get_width() * weapon_scale_width,pygame.image.load(f"images/m4_shot/{i}.png").get_height() * weapon_scale_height)) for i in range(1, 4, 1)]
m4_reload = [pygame.transform.smoothscale(pygame.image.load(f"images/m4_reload/{i}.png"), (pygame.image.load(f"images/m4_reload/{i}.png").get_width() * weapon_scale_width,pygame.image.load(f"images/m4_reload/{i}.png").get_height() * weapon_scale_height)) for i in range(1, 53, 1)]
sprites_pistol_shot = [pygame.transform.smoothscale(pygame.image.load(f"images/pistol_sprites/{i}.png"), (pygame.image.load(f"images/pistol_sprites/{i}.png").get_width() * weapon_scale_width, pygame.image.load(f"images/pistol_sprites/{i}.png").get_height() * weapon_scale_height)) for i in range(1, 11, 1)]
sprites_pistol_reload = [pygame.transform.smoothscale(pygame.image.load(f"images/reload/{i}.png"), (pygame.image.load(f"images/reload/{i}.png").get_width() * weapon_scale_width,pygame.image.load(f"images/reload/{i}.png").get_height() * weapon_scale_height)) for i in range(1, 47, 1)]
swap_to_first = [pygame.transform.smoothscale(pygame.image.load(f"images/swap_to_first/{i}.png"), (pygame.image.load(f"images/swap_to_first/{i}.png").get_width() * weapon_scale_width,pygame.image.load(f"images/swap_to_first/{i}.png").get_height() * weapon_scale_height)) for i in range(1, 15, 1)]
swap_to_second = [pygame.transform.smoothscale(pygame.image.load(f"images/swap_to_second/{i}.png"), (pygame.image.load(f"images/swap_to_second/{i}.png").get_width() * weapon_scale_width,pygame.image.load(f"images/swap_to_second/{i}.png").get_height() * weapon_scale_height)) for i in range(1, 15, 1)]
pistol_shot_sound, pistol_reload_sound = pygame.mixer.Sound("sounds/shot_pistol.mp3"), pygame.mixer.Sound("sounds/pistol_reload.mp3")
m4_shot_sound = pygame.mixer.Sound("sounds/m4shot.mp3")
m4_reload_sound = pygame.mixer.Sound("sounds/m4reload.mp3")
swap_sound = pygame.mixer.Sound("sounds/swap_to_pistol.mp3")

# second weapon settings
damage_for_pistol = 45
max_ammo_pistol = 10
anim_speed_for_shot_pistol = 50
anim_speed_for_reload_pistol = 20

anim_speed_for_swap = 18

# first weapon settings
damage_for_m4 = 30
max_ammo_m4 = 30
anim_speed_for_shot_m4 = 90
anim_speed_for_reload_m4 = 20

selection_flag = False
swap_flag = False

# map data
# b - Brick wall
# r - rusty brick wall
# d - wall with board
# c - brick wall with boards (breakable)
# f - door (breakable)
# w - weapons cases 1 (flat)
# q - weapons cases 2 (flat)

flat_objects_prefabs = ["w", "q"]

map_level_1 = []
map_level_2 = []
map_level_3 = []

level_1_results = []
level_2_results = []
level_3_results = []


def load_data():
    global map_level_1, map_level_2, map_level_3, volume, level_1_results, level_2_results, level_3_results
    levels_data = open("levels_data.txt", "r")
    n = int(levels_data.readline())
    for i in range(n):
        map_level_1.append(levels_data.readline()[:-1])
    n = int(levels_data.readline())
    for i in range(n):
        map_level_2.append(levels_data.readline()[:-1])
    n = int(levels_data.readline())
    for i in range(n):
        map_level_3.append(levels_data.readline()[:-1])

    saved_data = open("saved_data.txt", "r")
    volume = float(saved_data.readline())
    for i in range(5):
        level_1_results.append(saved_data.readline())
    for i in range(5):
        level_2_results.append(saved_data.readline())
    for i in range(5):
        level_3_results.append(saved_data.readline())




def convert_map_to_list(cur_map):
    res_map = []
    for y in range(len(cur_map)):
        line = []
        for x in range(len(cur_map[0])):
            line.append(cur_map[y][x])
        res_map.append(line)
    return res_map


#map = convert_map_to_list(map_level_1)


enemies = dict()
environment = []
worldMap = dict()
cur_amount_of_enemies = 0

def generate_enemies_and_environment(map):
    global enemies, environment, worldMap, cur_amount_of_enemies
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] != " " and map[y][x] != "e" and map[y][x] not in flat_objects_prefabs:
                worldMap[(x * blockSize, y * blockSize)] = map[y][x]
            elif map[y][x] == "e":
                enemies[(x, y)] = AI.Enemy((x, y), 3, 100)
            elif map[y][x] in flat_objects_prefabs:
                environment.append((x, y))
    cur_amount_of_enemies = len(enemies)


#generate_enemies_and_environment(map)


distance_from_screen = accuracy_of_draw / (2 * tan(field_of_view / 2))
projection_coefficient = screen_height * 0.01 / accuracy_of_draw * 200
ray_thickness = screen_width / accuracy_of_draw

textureWidth = 800
textureHeight = 800
textureScale = textureWidth / blockSize

