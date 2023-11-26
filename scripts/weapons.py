import pygame
import Data

pygame.init()

sprites_shot = [
    pygame.transform.smoothscale(pygame.image.load("images/pistol_sprites/1.png"), (pygame.image.load("images/pistol_sprites/1.png").get_width() * Data.weapon_scale_wight, pygame.image.load("images/pistol_sprites/1.png").get_height() * Data.weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/pistol_sprites/2.png"), (pygame.image.load("images/pistol_sprites/2.png").get_width() * Data.weapon_scale_wight, pygame.image.load("images/pistol_sprites/2.png").get_height() * Data.weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/pistol_sprites/3.png"), (pygame.image.load("images/pistol_sprites/3.png").get_width() * Data.weapon_scale_wight, pygame.image.load("images/pistol_sprites/3.png").get_height() * Data.weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/pistol_sprites/4.png"), (pygame.image.load("images/pistol_sprites/4.png").get_width() * Data.weapon_scale_wight, pygame.image.load("images/pistol_sprites/4.png").get_height() * Data.weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/pistol_sprites/5.png"), (pygame.image.load("images/pistol_sprites/5.png").get_width() * Data.weapon_scale_wight, pygame.image.load("images/pistol_sprites/5.png").get_height() * Data.weapon_scale_height))
]

sprites_shot_scope = [
    pygame.transform.smoothscale(pygame.image.load("images/pistol_scope_shot/1.png"), (pygame.image.load("images/pistol_scope_shot/1.png").get_width() * Data.weapon_scale_wight, pygame.image.load("images/pistol_scope_shot/1.png").get_height() * Data.weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/pistol_scope_shot/2.png"), (pygame.image.load("images/pistol_scope_shot/2.png").get_width() * Data.weapon_scale_wight, pygame.image.load("images/pistol_scope_shot/2.png").get_height() * Data.weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/pistol_scope_shot/3.png"), (pygame.image.load("images/pistol_scope_shot/3.png").get_width() * Data.weapon_scale_wight, pygame.image.load("images/pistol_scope_shot/3.png").get_height() * Data.weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/pistol_scope_shot/4.png"), (pygame.image.load("images/pistol_scope_shot/4.png").get_width() * Data.weapon_scale_wight, pygame.image.load("images/pistol_scope_shot/4.png").get_height() * Data.weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/pistol_scope_shot/5.png"), (pygame.image.load("images/pistol_scope_shot/5.png").get_width() * Data.weapon_scale_wight, pygame.image.load("images/pistol_scope_shot/5.png").get_height() * Data.weapon_scale_height))
]

sprites_reload = [
    pygame.transform.smoothscale(pygame.image.load("images/reload/1.png"), (pygame.image.load("images/reload/1.png").get_width() * Data.weapon_scale_wight, pygame.image.load("images/reload/1.png").get_height() * Data.weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/2.png"), (pygame.image.load("images/reload/2.png").get_width() * Data.weapon_scale_wight, pygame.image.load("images/reload/2.png").get_height() * Data.weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/3.png"), (pygame.image.load("images/reload/3.png").get_width() * Data.weapon_scale_wight, pygame.image.load("images/reload/3.png").get_height() * Data.weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/4.png"), (pygame.image.load("images/reload/4.png").get_width() * Data.weapon_scale_wight, pygame.image.load("images/reload/4.png").get_height() * Data.weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/5.png"), (pygame.image.load("images/reload/5.png").get_width() * Data.weapon_scale_wight, pygame.image.load("images/reload/5.png").get_height() * Data.weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/6.png"), (pygame.image.load("images/reload/6.png").get_width() * Data.weapon_scale_wight, pygame.image.load("images/reload/6.png").get_height() * Data.weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/7.png"), (pygame.image.load("images/reload/7.png").get_width() * Data.weapon_scale_wight, pygame.image.load("images/reload/7.png").get_height() * Data.weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/8.png"), (pygame.image.load("images/reload/8.png").get_width() * Data.weapon_scale_wight, pygame.image.load("images/reload/8.png").get_height() * Data.weapon_scale_height)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/9.png"), (pygame.image.load("images/reload/9.png").get_width() * Data.weapon_scale_wight, pygame.image.load("images/reload/9.png").get_height() * Data.weapon_scale_height))
]

pistol_shot_sound = pygame.mixer.Sound("sounds/shot_pistol.mp3")
pistol_reload_sound = pygame.mixer.Sound("sounds/pistol_reload.mp3")

weapon_anim_count = 0
anim_frames = 0
anim_speed_for_shot = 5
anim_speed_for_reload = 5
shot_flag = False
reload_flag = False
scope_flag = False
ammo = 0
max_ammo = 6