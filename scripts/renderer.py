import pygame
import data
import player
import raycast
import weapon
from math import *

animation_frame = 0


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
    if projection_height > data.screen_height * 7:
        projection_height = data.screen_height * 7

    if current_texture != 0:
        wall_column = data.textures[current_texture].subsurface(offset * data.textureScale, 0, data.textureScale,
                                                                data.textureHeight)
        wall_column = pygame.transform.scale(wall_column, (data.ray_thickness + 1, projection_height))
        wall_column_surface = pygame.Surface((wall_column.get_width(), wall_column.get_height()), pygame.SRCALPHA)
        color_of_depth = depth // 10
        if color_of_depth > 255:
            color_of_depth = 255
        pygame.draw.rect(wall_column_surface, (0, 0, 0, color_of_depth),
                         (0, 0, wall_column.get_width(), wall_column.get_height()))
        screen.blit(wall_column,
                    (
                    ray * data.ray_thickness + data.screen_width / 2, data.screen_height // 2 - projection_height // 2))
        screen.blit(wall_column_surface, (
        ray * data.ray_thickness + data.screen_width / 2, data.screen_height // 2 - projection_height // 2))


def draw_weapon():
    weapon.selector.draw_selected_weapon()


def draw_scene(screen):
    background_texture = pygame.transform.scale(data.textures["background"], (data.screen_width, data.screen_height))
    screen.blit(background_texture, (0, 0))

    start_ray_pos_x, start_ray_pos_y = player.position[0], player.position[1]
    floor_start_pos_x, floor_start_pos_y = (
    start_ray_pos_x // data.blockSize * data.blockSize, start_ray_pos_y // data.blockSize * data.blockSize)
    for ray in range(-data.accuracy_of_draw // 2, data.accuracy_of_draw // 2):
        ray_cast_with_draw_line(ray, start_ray_pos_x, start_ray_pos_y, floor_start_pos_x, floor_start_pos_y, screen)

    flat_objects_queue_to_render = []
    for objects_list in (data.environment, data.enemies):
        for object in objects_list:
            object_pos_vector = [object[0] * data.blockSize + data.blockSize // 2 - player.position[0],
                                 object[1] * data.blockSize + data.blockSize // 2 - player.position[1]]
            object_pos_vector_magnitude = (object_pos_vector[0] ** 2 + object_pos_vector[1] ** 2)
            flat_objects_queue_to_render.append((object_pos_vector_magnitude, data.map[object[1]][object[0]], object))
    flat_objects_queue_to_render.sort(reverse=True)
    for i in range(len(flat_objects_queue_to_render)):
        flat_objects_queue_to_render[i] = flat_objects_queue_to_render[i][2]

    draw_objects(screen, flat_objects_queue_to_render)
    draw_weapon()


def draw_objects(screen, objects):
    for object in objects:
        center_ray_vector = [cos(player.rotation), sin(player.rotation)]
        object_pos_vector = [object[0] * data.blockSize + data.blockSize // 2 - player.position[0],
                             object[1] * data.blockSize + data.blockSize // 2 - player.position[1]]
        object_pos_vector_magnitude = (object_pos_vector[0] ** 2 + object_pos_vector[1] ** 2) ** 0.5
        if object_pos_vector_magnitude != 0:
            angle_between = acos(
                (center_ray_vector[0] * object_pos_vector[0] + center_ray_vector[1] * object_pos_vector[1]) / (
                    object_pos_vector_magnitude))

        if atan2(*object_pos_vector) > atan2(*center_ray_vector):
            angle_between = -angle_between
        if atan2(*object_pos_vector) < (-1.57) and atan2(*center_ray_vector) > 1.57 or atan2(
                *object_pos_vector) > 1.57 and atan2(*center_ray_vector) < (-1.57):
            angle_between = -angle_between

        if abs(angle_between) <= ((data.field_of_view + pi / 4) / 2):
            if object_pos_vector_magnitude != 0:
                texture_pixel_size = data.textureWidth * (data.object_scale_coefficient / object_pos_vector_magnitude)
                if texture_pixel_size > round(data.screen_height * 1.5):
                    texture_pixel_size = round(data.screen_height * 1.5)
                if object in data.enemies:
                    texture = pygame.transform.scale(data.enemies[object].get_frame(),
                                                     (texture_pixel_size, texture_pixel_size))
                else:
                    texture = pygame.transform.scale(data.textures[data.map[object[1]][object[0]]],
                                                     (texture_pixel_size, texture_pixel_size))
            offset = angle_between / data.padding_of_rays * data.ray_thickness + data.screen_width // 2

            for i in range(-round(texture_pixel_size // data.ray_thickness // 2),
                           round(texture_pixel_size // data.ray_thickness // 2 - 1)):
                angle = degrees(angle_between + i * data.padding_of_rays)
                if raycast.raycast_walls(angle)[0] > object_pos_vector_magnitude:
                    enemy_column = texture.subsurface(((
                                                                   i + texture_pixel_size // data.ray_thickness // 2) * data.ray_thickness,
                                                       0, data.ray_thickness + 1, texture_pixel_size))
                    screen.blit(enemy_column,
                                (offset + i * data.ray_thickness, data.screen_height // 2 - texture_pixel_size // 2))


def debug():
    blockSize = data.blockSize // 4
    for y in range(len(data.map)):
        for x in range(len(data.map[0])):
            if data.map[y][x] != " ":
                pygame.draw.rect(data.screen, "white", (x * blockSize, y * blockSize, blockSize, blockSize))

    pygame.draw.circle(data.screen, "blue", (player.position[0] // 4, player.position[1] // 4), 10)
    pygame.draw.line(data.screen, "green", (player.position[0] // 4, player.position[1] // 4), (cos(player.rotation) * 1000 + player.position[0] // 4, sin(player.rotation) * 1000 + player.position[1] // 4))