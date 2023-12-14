import pygame
from pygame import draw
import data
import player
from math import *
import weapon

pygame.init()

screen = pygame.display.set_mode(data.screen_size, flags=pygame.NOFRAME)
pygame.display.set_caption("raycasters2005")
# gameIcon = pygame.image.load("images/icon.png")
# pygame.display.set_icon(gameIcon)

game_running = True
game_clock = pygame.time.Clock()
pygame.mouse.set_visible(False)


def ray_cast(ray, ox, oy, xm, ym):
    ray_angle = ray * data.padding_of_rays + player.rotation
    x, dx = (xm + data.blockSize, 1) if cos(ray_angle) >= 0 else (xm, -1)
    magnitude = [10 ** 10, 10 ** 10]
    for i in range(0, int(data.depth_of_field), data.blockSize):
        if cos(ray_angle) != 0:
            magnitude[0] = (x - ox) / cos(ray_angle)
        yv = oy + magnitude[0] * sin(ray_angle)
        rounded = ((x + dx) // data.blockSize * data.blockSize, yv // data.blockSize * data.blockSize)
        current_texture_v = 0
        if rounded in data.worldMap:
            current_texture_v = data.worldMap[rounded]
            break
        x += dx * data.blockSize

    y, dy = (ym + data.blockSize, 1) if sin(ray_angle) >= 0 else (ym, -1)
    for i in range(0, data.screen_height, data.blockSize):
        if sin(ray_angle) != 0:
            magnitude[1] = (y - oy) / sin(ray_angle)
        xh = ox + magnitude[1] * cos(ray_angle)
        rounded = (xh // data.blockSize * data.blockSize, (y + dy) // data.blockSize * data.blockSize)
        current_texture_h = 0
        if rounded in data.worldMap:
            current_texture_h = data.worldMap[rounded]
            break
        y += dy * data.blockSize

    # if current_texture_h != 0 or current_texture_V != 0:
    depth, offset, current_texture = (magnitude[0], yv, current_texture_v) if magnitude[0] < magnitude[1] else (
        magnitude[1], xh, current_texture_h)

    offset = int(offset) % data.blockSize
    depth = depth * cos(player.rotation - ray_angle)
    projection_height = data.blockSize * data.distance_from_screen / depth * data.projection_coefficient

    wall_column = data.textures[current_texture].subsurface(offset * data.textureScale, 0, data.textureScale,
                                                            data.textureHeight)
    wall_column = pygame.transform.scale(wall_column, (data.ray_thickness + 1, projection_height))
    screen.blit(wall_column,
                (ray * data.ray_thickness + data.screen_width / 2, data.screen_height // 2 - projection_height // 2))


def draw():
    ox, oy = player.position[0], player.position[1]
    xm, ym = (ox // data.blockSize * data.blockSize, oy // data.blockSize * data.blockSize)
    for ray in range(-data.accuracy_of_draw // 2, data.accuracy_of_draw // 2):
        ray_cast(ray, ox, oy, xm, ym)

    # drawing a minimap
    pygame.draw.rect(screen, "black", (
        0, 0, data.blockSize * len(data.map[0]) / data.miniMapScale,
        data.blockSize * len(data.map) / data.miniMapScale))
    for y in range(len(data.map)):
        for x in range(len(data.map[0])):
            if data.map[y][x] != " ":
                pygame.draw.rect(screen, "white", (
                    x * data.blockSize / data.miniMapScale, y * data.blockSize / data.miniMapScale,
                    data.blockSize / data.miniMapScale, data.blockSize / data.miniMapScale))
    pygame.draw.circle(screen, "blue", (player.position[0] / data.miniMapScale, player.position[1] / data.miniMapScale),
                       4)
    # drawing weapons
    weapon.weapons()


while game_running:
    player.movement(background_position=0)
    draw()
    pygame.display.update()
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()

    game_clock.tick(data.fps)
