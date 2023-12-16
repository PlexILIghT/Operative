import pygame
import data
import player
import weapon
import raycast
from math import *
def ray_cast_with_draw_line(ray, start_ray_pos_x, start_ray_pos_y, floor_start_pos_x, floor_start_pos_y, screen):
    ray_angle = ray * data.padding_of_rays + player.rotation
    x, dx = (floor_start_pos_x + data.blockSize, 1) if cos(ray_angle) >= 0 else (floor_start_pos_x, -1)
    magnitude = [10 ** 10, 10 ** 10]
    for i in range(0, int(data.depth_of_field), data.blockSize):
        if cos(ray_angle) != 0:
            magnitude[0] = (x - start_ray_pos_x) / cos(ray_angle)
        yv = start_ray_pos_y + magnitude[0] * sin(ray_angle)
        rounded = ((x + dx) // data.blockSize * data.blockSize, yv // data.blockSize * data.blockSize)
        current_texture_v = 0
        if rounded in data.worldMap:
            current_texture_v = data.worldMap[rounded]
            break
        x += dx * data.blockSize

    y, dy = (floor_start_pos_y + data.blockSize, 1) if sin(ray_angle) >= 0 else (floor_start_pos_y, -1)
    for i in range(0, int(data.depth_of_field), data.blockSize):
        if sin(ray_angle) != 0:
            magnitude[1] = (y - start_ray_pos_y) / sin(ray_angle)
        xh = start_ray_pos_x + magnitude[1] * cos(ray_angle)
        rounded = (xh // data.blockSize * data.blockSize, (y + dy) // data.blockSize * data.blockSize)
        current_texture_h = 0
        if rounded in data.worldMap:
            current_texture_h = data.worldMap[rounded]
            break
        y += dy * data.blockSize

    depth, offset, current_texture = (magnitude[0], yv, current_texture_v) if magnitude[0] < magnitude[1] else (
        magnitude[1], xh, current_texture_h)

    # drawing line of wall
    offset = int(offset) % data.blockSize
    depth = depth * cos(player.rotation - ray_angle)
    projection_height = data.blockSize * data.distance_from_screen / depth * data.projection_coefficient

    wall_column = data.textures[current_texture].subsurface(offset * data.textureScale, 0, data.textureScale,
                                                            data.textureHeight)
    wall_column = pygame.transform.scale(wall_column, (data.ray_thickness + 1, projection_height))
    screen.blit(wall_column,
                (ray * data.ray_thickness + data.screen_width / 2, data.screen_height // 2 - projection_height // 2))

enemies = [(12, 6)]
def draw_scene(screen):
    start_ray_pos_x, start_ray_pos_y = player.position[0], player.position[1]
    floor_start_pos_x, floor_start_pos_y = (start_ray_pos_x // data.blockSize * data.blockSize, start_ray_pos_y // data.blockSize * data.blockSize)
    for ray in range(-data.accuracy_of_draw // 2, data.accuracy_of_draw // 2):
        ray_cast_with_draw_line(ray, start_ray_pos_x, start_ray_pos_y, floor_start_pos_x, floor_start_pos_y, screen)

    for enemy in enemies:
        center_ray_vector = [cos(player.rotation), sin(player.rotation)]
        enemy_pos_vector = [enemy[0] - player.position[0], enemy[1] - player.position[1]]
        center_ray_vector_magnitude = (center_ray_vector[0]**2 + center_ray_vector[0]**2)**0.5
        enemy_pos_vector_magnitude = (enemy_pos_vector[0]**2 + enemy_pos_vector[1]**2)**0.5
        #...
    # drawing weapons
    weapon.weapons()