import data
from math import *
import pygame
import weapon


x = (2 + 0.5) * data.blockSize
y = (2 + 0.5) * data.blockSize
position = [x, y]
rotation = -pi * 3 / 2
movement_speed = 11
rotation_speed = 5 * 10 ** 2

damage = 35
health = 100

flag_time = False
start_time = 0
paused_time = 0
self_distance = data.blockSize // 5
blood_animation_frame = 0
bleed = 0


def clear_level():
    global health, position, rotation, flag_time, start_time
    health = 100
    data.map = data.convert_map_to_list(data.map_level_1)
    data.generate_enemies_and_environment(data.map)
    weapon.pistol.ammo = 0
    weapon.m4.ammo = 0
    x = (2 + 0.5) * data.blockSize
    y = (2 + 0.5) * data.blockSize
    position = [x, y]
    rotation = -pi * 3 / 2
    flag_time = True
    start_time = 0
    data.cur_amount_of_enemies = len(data.enemies)




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

    if (move_vector_ray[0] // data.blockSize * data.blockSize,
        position[1] // data.blockSize * data.blockSize) not in data.worldMap:
        position[0] += move_vector[0] * movement_speed
    if (position[0] // data.blockSize * data.blockSize,
        move_vector_ray[1] // data.blockSize * data.blockSize) not in data.worldMap:
        position[1] += move_vector[1] * movement_speed

    mouse_rel = pygame.mouse.get_rel()
    mouse_direction = mouse_rel[0]
    pygame.mouse.set_pos(data.screen_width // 2, data.screen_height // 2)
    rotation += mouse_direction / rotation_speed


def get_hit(damage):
    global health, bleed
    health -= damage
    bleed = 1



def blood_animation():
    global blood_animation_frame, bleed
    if bleed == 1:
        blood_texture = data.textures["blood"].convert_alpha()
        surface = pygame.Surface((data.screen_width, data.screen_height), flags=pygame.SRCALPHA)
        if blood_animation_frame < 255:
            surface.blit(blood_texture, (0, 0, data.screen_width, data.screen_height))
            surface.set_alpha(blood_animation_frame)
            data.screen.blit(surface, (0, 0, 0, 0))
            blood_animation_frame += 100
        elif blood_animation_frame >= 255:
            blood_animation_frame = 255
            bleed = 2
    if bleed == 2:
        blood_texture = data.textures["blood"].convert_alpha()
        pygame.transform.scale(blood_texture, (data.screen_width, data.screen_height))
        surface = pygame.Surface((data.screen_width, data.screen_height), flags=pygame.SRCALPHA)
        if blood_animation_frame > 0:
            surface.blit(blood_texture, (0, 0, data.screen_width, data.screen_height))
            surface.set_alpha(blood_animation_frame)
            data.screen.blit(surface, (0, 0, 0, 0))
            blood_animation_frame -= 100
        elif blood_animation_frame <= 0:
            blood_animation_frame = 0
            bleed = 0
