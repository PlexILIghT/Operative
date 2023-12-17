import pygame
import data
from data import screen

pygame.init()

weapon_scale_wight = data.screen_width / (data.screen_width * 0.4)
weapon_scale_height = data.screen_height / (data.screen_height * 0.4)
weapon_scale_scope_wight = data.screen_width / (data.screen_width * 0.276)
weapon_scale_scope_height = data.screen_height / (data.screen_height * 0.276)

# weapon animation
SpritesPistolShot = [
    pygame.transform.smoothscale
    (pygame.image.load("images/pistol_sprites/1.png"),
     (pygame.image.load("images/pistol_sprites/1.png").get_width() * weapon_scale_wight,
      pygame.image.load("images/pistol_sprites/1.png").get_height() * weapon_scale_height)),
    pygame.transform.smoothscale
    (pygame.image.load("images/pistol_sprites/2.png"),
     (pygame.image.load("images/pistol_sprites/2.png").get_width() * weapon_scale_wight,
      pygame.image.load("images/pistol_sprites/2.png").get_height() * weapon_scale_height)),
    pygame.transform.smoothscale
    (pygame.image.load("images/pistol_sprites/3.png"),
     (pygame.image.load("images/pistol_sprites/3.png").get_width() * weapon_scale_wight,
      pygame.image.load("images/pistol_sprites/3.png").get_height() * weapon_scale_height)),
    pygame.transform.smoothscale
    (pygame.image.load("images/pistol_sprites/4.png"),
     (pygame.image.load("images/pistol_sprites/4.png").get_width() * weapon_scale_wight,
      pygame.image.load("images/pistol_sprites/4.png").get_height() * weapon_scale_height)),
    pygame.transform.smoothscale
    (pygame.image.load("images/pistol_sprites/5.png"),
     (pygame.image.load("images/pistol_sprites/5.png").get_width() * weapon_scale_wight,
      pygame.image.load("images/pistol_sprites/5.png").get_height() * weapon_scale_height))
]

SpritesPistolShotScope = [
    pygame.transform.smoothscale
    (pygame.image.load("images/pistol_scope_shot/1.png"),
     (pygame.image.load("images/pistol_scope_shot/1.png").get_width() * weapon_scale_scope_wight,
      pygame.image.load("images/pistol_scope_shot/1.png").get_height() * weapon_scale_scope_height)),
    pygame.transform.smoothscale
    (pygame.image.load("images/pistol_scope_shot/2.png"),
     (pygame.image.load(
         "images/pistol_scope_shot/2.png").get_width() * weapon_scale_scope_wight,
      pygame.image.load(
          "images/pistol_scope_shot/2.png").get_height() * weapon_scale_scope_height)),
    pygame.transform.smoothscale
    (pygame.image.load("images/pistol_scope_shot/3.png"),
     (pygame.image.load(
         "images/pistol_scope_shot/3.png").get_width() * weapon_scale_scope_wight,
      pygame.image.load(
          "images/pistol_scope_shot/3.png").get_height() * weapon_scale_scope_height)),
    pygame.transform.smoothscale
    (pygame.image.load("images/pistol_scope_shot/4.png"),
     (pygame.image.load(
         "images/pistol_scope_shot/4.png").get_width() * weapon_scale_scope_wight,
      pygame.image.load(
          "images/pistol_scope_shot/4.png").get_height() * weapon_scale_scope_height)),
    pygame.transform.smoothscale
    (pygame.image.load("images/pistol_scope_shot/5.png"),
     (pygame.image.load(
         "images/pistol_scope_shot/5.png").get_width() * weapon_scale_scope_wight,
      pygame.image.load(
          "images/pistol_scope_shot/5.png").get_height() * weapon_scale_scope_height))
]

SpritesPistolReload = [
    pygame.transform.smoothscale(pygame.image.load("images/reload/1.png"), (
        pygame.image.load("images/reload/1.png").get_width() * weapon_scale_wight,
        pygame.image.load("images/reload/1.png").get_height() * weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/2.png"), (
        pygame.image.load("images/reload/2.png").get_width() * weapon_scale_wight,
        pygame.image.load("images/reload/2.png").get_height() * weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/3.png"), (
        pygame.image.load("images/reload/3.png").get_width() * weapon_scale_wight,
        pygame.image.load("images/reload/3.png").get_height() * weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/4.png"), (
        pygame.image.load("images/reload/4.png").get_width() * weapon_scale_wight,
        pygame.image.load("images/reload/4.png").get_height() * weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/5.png"), (
        pygame.image.load("images/reload/5.png").get_width() * weapon_scale_wight,
        pygame.image.load("images/reload/5.png").get_height() * weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/6.png"), (
        pygame.image.load("images/reload/6.png").get_width() * weapon_scale_wight,
        pygame.image.load("images/reload/6.png").get_height() * weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/7.png"), (
        pygame.image.load("images/reload/7.png").get_width() * weapon_scale_wight,
        pygame.image.load("images/reload/7.png").get_height() * weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/8.png"), (
        pygame.image.load("images/reload/8.png").get_width() * weapon_scale_wight,
        pygame.image.load("images/reload/8.png").get_height() * weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/9.png"), (
        pygame.image.load("images/reload/9.png").get_width() * weapon_scale_wight,
        pygame.image.load("images/reload/9.png").get_height() * weapon_scale_height))
]

pistol_shot_sound = pygame.mixer.Sound("sounds/shot_pistol.mp3")
pistol_reload_sound = pygame.mixer.Sound("sounds/pistol_reload.mp3")


shot_flag = False
reload_flag = False
scope_flag = False
scope_toggle = False


def reload():
    weapon_anim_count = 0
    anim_frames = 0
    anim_speed_for_shot = 12
    anim_speed_for_reload = 12
    shot_flag = False
    reload_flag = False
    scope_flag = False
    scope_toggle = False
    ammo = 0
    max_ammo = 6
    true_anim_speed_for_reload = game_clock.get_fps() // anim_speed_for_reload
    screen.blit(SpritesPistolReload[weapon_anim_count], (
        data.screen_width / 2 + SpritesPistolReload[weapon_anim_count].get_width(),
        data.screen_height - SpritesPistolReload[weapon_anim_count].get_height()))
    if anim_frames == 1:
        pistol_reload_sound.play()
    elif weapon_anim_count == len(SpritesPistolReload) - 1 and anim_frames % true_anim_speed_for_reload == 0:
        weapon_anim_count = 0
        ammo = 0
        anim_frames = 0
        weapon_anim_count = 0
        reload_flag = False
    elif anim_frames % true_anim_speed_for_reload == 0:
        weapon_anim_count += 1
    anim_frames += 1


def weapon_static():
    if not scope_flag:
        screen.blit(SpritesPistolShot[0], (
            data.screen_width / 2 + SpritesPistolShot[0].get_width(),
            data.screen_height - SpritesPistolShot[0].get_height()))
    else:
        screen.blit(SpritesPistolShotScope[0], (
            data.screen_width / 2 - SpritesPistolShotScope[0].get_width() / 2 + 26,
            data.screen_height - SpritesPistolShotScope[0].get_height()))


def shot():
    weapon_anim_count = 0
    anim_frames = 0
    anim_speed_for_shot = 12
    anim_speed_for_reload = 12
    shot_flag = False
    reload_flag = False
    scope_flag = False
    scope_toggle = False
    ammo = 0
    max_ammo = 6
    true_anim_speed_for_shot = game_clock.get_fps() // anim_speed_for_shot
    screen.blit(SpritesPistolShot[weapon_anim_count],
                (data.screen_width / 2 + SpritesPistolShot[weapon_anim_count].get_width(),
                 data.screen_height - SpritesPistolShot[weapon_anim_count].get_height())) if not scope_flag \
        else screen.blit(SpritesPistolShotScope[weapon_anim_count],
                         (data.screen_width / 2 - SpritesPistolShotScope[weapon_anim_count].get_width() / 2 + 26,
                          data.screen_height - SpritesPistolShotScope[weapon_anim_count].get_height()))
    if anim_frames == 1:
        pistol_shot_sound.play()
    elif weapon_anim_count == len(SpritesPistolShot) - 1 and anim_frames % true_anim_speed_for_shot == 0:
        weapon_anim_count = 0
        ammo += 1
        shot_flag = False
        anim_frames = 0
    elif anim_frames % true_anim_speed_for_shot == 0:
        weapon_anim_count += 1
    anim_frames += 1


def weapon_events():
    shot_flag = False
    reload_flag = False
    scope_flag = False
    scope_toggle = False
    ammo = 0
    max_ammo = 6
    pushed_mouse_button = pygame.mouse.get_pressed()
    key_pressed = pygame.key.get_pressed()
    if not pushed_mouse_button[2]:
        scope_toggle = False
    if ammo == max_ammo or key_pressed[pygame.K_r]:
        reload_flag = True
    if not scope_toggle:
        if pushed_mouse_button[2] and not reload_flag and not shot_flag:
            scope_flag = not scope_flag
            scope_toggle = True
    if pushed_mouse_button[0] and not reload_flag and not shot_flag:
        shot_flag = True


def weapons():
    weapon_events()
    if reload_flag and not shot_flag:
        reload()
    else:
        shot() if shot_flag else weapon_static()
