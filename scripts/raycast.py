import player
import data
from math import *

# how to use:
# в аргументы подается угол луча в градусах относительно игрока
# то есть 0 градусов, это прямо по центру экрана, что-то отрицательное - слева, что-то положительное - справа
# функция возвращает список, где 0 элемент - это расстояние до объекта, а 1 - это его номер
def raycast(angle):
    ray_angle = radians(angle) + player.rotation
    start_ray_pos_x, start_ray_pos_y = player.position[0], player.position[1]
    floor_start_pos_x, floor_start_pos_y = (start_ray_pos_x // data.blockSize * data.blockSize, start_ray_pos_y // data.blockSize * data.blockSize)
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
    return [depth, current_texture]