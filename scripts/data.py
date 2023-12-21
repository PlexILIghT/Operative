import pygame
from math import *
import AI

pygame.init()

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

#fonts
font = pygame.font.SysFont('impact', 50)

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
    "w": pygame.image.load("images/textures/cases1.png").convert_alpha(),
    "q": pygame.image.load("images/textures/cases2.png").convert_alpha(),
    "background": pygame.image.load("images/background.png").convert(),
    "blood": pygame.image.load("images/blood.png").convert_alpha(),
    "alive_enemy": [pygame.image.load("images/alive_enemy/" + str(x) + ".png").convert_alpha() for x in range(1, 16)],
    "hurt_enemy": [pygame.image.load("images/hurt_enemy/" + str(x) + ".png").convert_alpha() for x in range(1, 27)],
    "dead_enemy": [pygame.image.load("images/dead_enemy/" + str(x) + ".png").convert_alpha() for x in range(1, 31)]
}

#scale settings for sprites
weaponScaleWidth = screen_width / (screen_width * 2)
weaponScaleHeight = screen_height / (screen_height * 2)
weaponMeleeScaleWidth = screen_width/(screen_width * 0.5)
weaponMeleeScaleHeight = screen_height/(screen_height * 0.5)

m4Shot = [pygame.transform.smoothscale(pygame.image.load(f"images/m4_shot/{i}.png"), (pygame.image.load(f"images/m4_shot/{i}.png").get_width() * weaponScaleWidth,pygame.image.load(f"images/m4_shot/{i}.png").get_height() * weaponScaleHeight)) for i in range(1, 4, 1)]
m4reload = [pygame.transform.smoothscale(pygame.image.load(f"images/m4_reload/{i}.png"), (pygame.image.load(f"images/m4_reload/{i}.png").get_width() * weaponScaleWidth,pygame.image.load(f"images/m4_reload/{i}.png").get_height() * weaponScaleHeight)) for i in range(1, 53, 1)]

spritesPistolShot = [pygame.transform.smoothscale(pygame.image.load(f"images/pistol_sprites/{i}.png"), (pygame.image.load(f"images/pistol_sprites/{i}.png").get_width() * weaponScaleWidth, pygame.image.load(f"images/pistol_sprites/{i}.png").get_height() * weaponScaleHeight)) for i in range(1, 11, 1)]
spritesPistolReload = [pygame.transform.smoothscale(pygame.image.load(f"images/reload/{i}.png"), (pygame.image.load(f"images/reload/{i}.png").get_width() * weaponScaleWidth,pygame.image.load(f"images/reload/{i}.png").get_height() * weaponScaleHeight)) for i in range(1, 47, 1)]
spritesMelee = [pygame.transform.smoothscale(pygame.image.load(f"images/melee_sprites/{i}.png"), (pygame.image.load(f"images/melee_sprites/{i}.png").get_width() * weaponMeleeScaleWidth, pygame.image.load(f"images/melee_sprites/{i}.png").get_height() * weaponMeleeScaleHeight)) for i in range(1, 7, 1)]
swapToFirst = [pygame.transform.smoothscale(pygame.image.load(f"images/swap_to_first/{i}.png"), (pygame.image.load(f"images/swap_to_first/{i}.png").get_width() * weaponScaleWidth,pygame.image.load(f"images/swap_to_first/{i}.png").get_height() * weaponScaleHeight)) for i in range(1, 15, 1)]
swapToSecond = [pygame.transform.smoothscale(pygame.image.load(f"images/swap_to_second/{i}.png"), (pygame.image.load(f"images/swap_to_second/{i}.png").get_width() * weaponScaleWidth,pygame.image.load(f"images/swap_to_second/{i}.png").get_height() * weaponScaleHeight)) for i in range(1, 15, 1)]
meleeSound = pygame.mixer.Sound("sounds/MeleeSound.mp3")
pistolShotSound, pistolReloadSound = pygame.mixer.Sound("sounds/shot_pistol.mp3"), pygame.mixer.Sound("sounds/pistol_reload.mp3")
m4shotSound = pygame.mixer.Sound("sounds/m4shot.mp3")
m4reloadSound = pygame.mixer.Sound("sounds/m4reload.mp3")
swapSound = pygame.mixer.Sound("sounds/swap_to_pistol.mp3")


#second weapon settings
damageForPistol = 10
maxAmmoPistol = 6
animSpeedForShotPistol = 50
animSpeedForReloadPistol = 20

animSpeedForSwap = 18

#first weapon settings
maxAmmoM4 = 30
animSpeedForShotM4 = 140
animSpeedForReloadM4 = 20

#melee weapon settings
animSpeedForMelee = 4

swapFlag = False

# map data
# b - Brick wall
# r - rusty brick wall
# d - wall with board
# c - breakable wall
# w - weapons cases 1 (flat)
# q - weapons cases 2 (flat)

flat_objects_prefabs = ["w", "q"]

map = [
    "bbbbbbrrrbbb           ",
    "b        w b           ",
    "b         qd           ",
    "bbbbbbb bbbbbccbb      ",
    "r               b      ",
    "r e     e  b    c      ",
    "b  q  e    d   eb      ",
    "bbbcbbrrrrbbb bbbbbbbbb",
    "       b           e  b",
    "       b e            b",
    "       bbbbbbbbbbbb bbb",
    "                b     b",
    "                b     b",
    "                b     b",
    "                bb    b",
    "                be   bb",
    "                b    eb",
    "            bbbbbb bbbb",
    "            b  e      b",
    "            b       e b",
    "            b e       b",
    "            b   e     b",
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
            environment.append((x, y))

distance_from_screen = accuracy_of_draw / (2 * tan(field_of_view / 2))
projection_coefficient = screen_height * 0.01 / accuracy_of_draw * 200
ray_thickness = screen_width / accuracy_of_draw

textureWidth = 800
textureHeight = 800
textureScale = textureWidth / blockSize
