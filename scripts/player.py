import data
from math import *
import pygame

x = (2 + 0.5) * data.blockSize
y = (2 + 0.5) * data.blockSize
position = [x, y]
rotation = -pi * 3 / 2
movement_speed = 10
rotation_speed = 5 * 10 ** 2

self_distance = data.blockSize
def movement():
    global rotation
    key_pressed = pygame.key.get_pressed()
    horizontal_input = -int(key_pressed[data.keys["left"]]) + int(key_pressed[data.keys["right"]])
    vertical_input = -int(key_pressed[data.keys["forward"]]) + int(key_pressed[data.keys["back"]])
    right_player_direction = [sin(rotation), -cos(rotation)]
    forward_player_direction = [cos(rotation), sin(rotation)]
    move_vector = [right_player_direction[0] * -horizontal_input + forward_player_direction[0] * -vertical_input,
                   right_player_direction[1] * -horizontal_input + forward_player_direction[1] * -vertical_input]

    if move_vector[0] != 0 and move_vector[1] != 0:
        magnitude = (move_vector[0] ** 2 + move_vector[1] ** 2) ** 0.5
        move_vector = [move_vector[0] / magnitude, move_vector[1] / magnitude]

    # collision

    move_vector_ray = [move_vector[0] * self_distance + position[0], move_vector[1] * self_distance + position[1]]

    if (move_vector_ray[0] // data.blockSize * data.blockSize, position[1] // data.blockSize * data.blockSize) not in data.worldMap:
        position[0] += move_vector[0] * movement_speed
    if (position[0] // data.blockSize * data.blockSize, move_vector_ray[1] // data.blockSize * data.blockSize) not in data.worldMap:
        position[1] += move_vector[1] * movement_speed

    mouse_rel = pygame.mouse.get_rel()
    mouse_direction = mouse_rel[0]
    pygame.mouse.set_pos(data.screen_width // 2, data.screen_height // 2)
    rotation += mouse_direction / rotation_speed
