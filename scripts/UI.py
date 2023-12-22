import pygame
from datetime import time, timedelta
import data
from player import health
from weapon import selector, m4, pistol
# from game import start_time


def render_hp(health):
    text = data.font.render(f"HEALTH   {health}", True, "white")
    data.screen.blit(text, (data.screen_width * 0.8, data.screen_height * 0.9))


def render_ammo():
    if data.selection_flag:
        max_ammo = pistol.max_ammo
        cur_ammo = pistol.max_ammo - pistol.ammo
    else:
        max_ammo = m4.max_ammo
        cur_ammo = m4.max_ammo - m4.ammo

    text = data.font.render(f"MAG   {cur_ammo} / {max_ammo}", True, "white")
    data.screen.blit(text, (data.screen_width * 0.8, data.screen_height * 0.8))


# def render_for_refactor():
#     # text = data.font.render(f"ENEMIES POS   {} ", True, "white")
#     data.screen.blit(text, (data.screen_width // 8, data.screen_height // 6))

def display_time(start_time):
    time_since_enter = pygame.time.get_ticks() - start_time
    text = data.font.render(f"TIME:   {timedelta(milliseconds=time_since_enter)}"[:-7], True, "white")
    data.screen.blit(text, (data.screen_width // 8, data.screen_height // 14))

def render_enemy_amount():
    text = data.font.render(f"ENEMIES LEFT   {data.cur_amount_of_enemies} / {len(data.enemies)}", True, "white")
    data.screen.blit(text, (data.screen_width // 8, data.screen_height // 8))


def render_all_UI(health, start_time):
    render_enemy_amount()
    render_hp(health)
    render_ammo()
    display_time(start_time)
    # render_for_refactor()