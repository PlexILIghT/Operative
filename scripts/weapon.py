import pygame
import data
import raycast
from data import screen, game_clock

pygame.init()


class Weapon:
    def __init__(self, damage, sprites_shot, sprites_reload, max_ammo, anim_speed_for_shot, anim_speed_for_reload,
                 shot_sound, reload_sound):
        self.damage = damage
        self.sprites_shot = list(sprites_shot)
        self.sprites_reload = list(sprites_reload)
        self.max_ammo = max_ammo
        self.anim_speed_for_shot = anim_speed_for_shot
        self.anim_speed_for_reload = anim_speed_for_reload
        self.true_anim_speed_for_shot = game_clock.get_fps() // self.anim_speed_for_shot + 1
        self.true_anim_speed_for_reload = game_clock.get_fps() // self.anim_speed_for_reload + 1
        self.shot_sound = shot_sound
        self.reload_sound = reload_sound
        self.reload_flag = False
        self.shot_flag = False
        self.ammo = 0
        self.anim_count = 0
        self.anim_frames = 0

    def events(self):
        keys = pygame.key.get_pressed()
        mouse_button = pygame.mouse.get_pressed()
        if keys[pygame.K_r] and not self.shot_flag and not data.swap_flag:
            self.reload_flag = True
        elif mouse_button[0] and not self.reload_flag and not data.swap_flag:
            self.shot_flag = True

    def static(self):
        screen.blit(self.sprites_shot[0], (
            data.screen_width / 2 - self.sprites_shot[0].get_width()/2,
            data.screen_height - self.sprites_shot[0].get_height()))

    def reload(self):
        self.true_anim_speed_for_reload = game_clock.get_fps() // self.anim_speed_for_reload + 1
        screen.blit(self.sprites_reload[self.anim_count], (
            data.screen_width / 2 - self.sprites_reload[self.anim_count].get_width()/2,
            data.screen_height - self.sprites_reload[self.anim_count].get_height()))
        if self.anim_frames == 1:
            self.reload_sound.play()
        if self.anim_count == len(self.sprites_reload) - 1 and self.anim_frames % self.true_anim_speed_for_reload == 0:
            self.anim_count = 0
            self.anim_frames = 0
            self.ammo = 0
            self.reload_flag = False
        elif self.anim_frames % self.true_anim_speed_for_reload == 0:
            self.anim_count += 1
        self.anim_frames += 1

    def check_for_hit(self):
        ray_hit_info = raycast.raycast_all(0)
        if ray_hit_info[1] == "e":
            data.enemies[tuple(ray_hit_info[2])].get_hit(self.damage)
        elif ray_hit_info[1] == "c" or ray_hit_info[1] == "f":
            data.map[ray_hit_info[2][1]][ray_hit_info[2][0]] = " "
            data.worldMap.pop((ray_hit_info[2][0] * data.blockSize, ray_hit_info[2][1] * data.blockSize))

    def shot(self):
        if self.ammo != self.max_ammo:
            self.true_anim_speed_for_shot = game_clock.get_fps() // self.anim_speed_for_shot + 1
            screen.blit(self.sprites_shot[self.anim_count], (
                data.screen_width / 2 - self.sprites_shot[0].get_width()/2,
                data.screen_height - self.sprites_shot[self.anim_count].get_height()))
            if self.anim_frames == 1:
                self.shot_sound.play()
                self.check_for_hit()
            if self.anim_count == len(self.sprites_shot) - 1 and self.anim_frames % self.true_anim_speed_for_shot == 0:
                self.anim_count = 0
                self.anim_frames = 0
                self.ammo += 1
                self.shot_flag = False
            elif self.anim_frames % self.true_anim_speed_for_shot == 0:
                self.anim_count += 1
            self.anim_frames += 1
        else:
            self.static()
            self.shot_flag = False

    def draw_weapon(self):
        self.events()
        if self.reload_flag:
            self.reload()
        elif self.shot_flag:
            self.shot()
        elif not self.shot_flag and not data.swap_flag:
            self.static()


class Selector:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.anim_count = 0
        self.anim_frames = 0
        self.swap_to_first = False
        self.swap_to_second = False
        self.true_anim_speed_for_swap = game_clock.get_fps() // data.anim_speed_for_swap + 1

    def swap_to_first_weapon(self):
        self.true_anim_speed_for_swap = game_clock.get_fps() // data.anim_speed_for_swap + 1
        screen.blit(data.swap_to_first[self.anim_count], (
            data.screen_width / 2 - data.swap_to_first[0].get_width() / 2,
            data.screen_height - data.swap_to_first[0].get_height()))
        if self.anim_count == 1:
            data.swap_sound.play()
            self.anim_count += 1
        elif self.anim_count == len(data.swap_to_first) - 1 and self.anim_frames % self.true_anim_speed_for_swap == 0:
            self.anim_count = 0
            self.anim_frames = 0
            self.swap_to_first = False
            data.swap_flag = False
            data.selection_flag = False
        elif self.anim_frames % self.true_anim_speed_for_swap == 0:
            self.anim_count += 1
        self.anim_frames += 1

    def swap_to_second_weapon(self):
        true_anim_speed_for_swap = game_clock.get_fps() // data.anim_speed_for_swap + 1
        screen.blit(data.swap_to_second[self.anim_count], (
            data.screen_width / 2 - data.swap_to_second[0].get_width() / 2,
            data.screen_height - data.swap_to_second[0].get_height()))
        if self.anim_count == 1:
            data.swap_sound.play()
            self.anim_count += 1
        elif self.anim_count == len(data.swap_to_second) - 1 and self.anim_frames % true_anim_speed_for_swap == 0:
            self.anim_count = 0
            self.anim_frames = 0
            self.swap_to_second = False
            data.swap_flag = False
            data.selection_flag = True
        elif self.anim_frames % true_anim_speed_for_swap == 0:
            self.anim_count += 1
        self.anim_frames += 1

    def selection(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] and data.selection_flag and not pistol.reload_flag:
            data.swap_flag = True
            self.swap_to_first = True
        if keys[pygame.K_2] and not data.selection_flag and not m4.reload_flag:
            data.swap_flag = True
            self.swap_to_second = True

    def draw_selected_weapon(self):
        self.selection()
        if self.swap_to_first:
            self.swap_to_first_weapon()
        elif self.swap_to_second:
            self.swap_to_second_weapon()
        elif data.selection_flag:
            pistol.draw_weapon()
        else:
            m4.draw_weapon()


pistol = Weapon(data.damage_for_pistol, data.sprites_pistol_shot, data.sprites_pistol_reload, data.max_ammo_pistol,
                data.anim_speed_for_shot_pistol, data.anim_speed_for_reload_pistol, data.pistol_shot_sound,
                data.pistol_reload_sound)
m4 = Weapon(data.damage_for_m4, data.m4_shot, data.m4_reload, data.max_ammo_m4, data.anim_speed_for_shot_m4,
            data.anim_speed_for_reload_m4, data.m4_shot_sound, data.m4_reload_sound)

selector = Selector(m4, pistol)
