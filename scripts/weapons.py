import pygame
import Data

pygame.init()

WeaponScaleWight = Data.screenWidth/(Data.screenWidth * 0.4)
WeaponScaleHeight = Data.screenHeight/(Data.screenHeight * 0.4)
WeaponScaleScopeWight = Data.screenWidth/(Data.screenWidth * 0.276)
WeaponScaleScopeHeight = Data.screenHeight/(Data.screenHeight * 0.276)

SpritesPistolShot = [
    pygame.transform.smoothscale(pygame.image.load("images/pistol_sprites/1.png"), (pygame.image.load("images/pistol_sprites/1.png").get_width() * WeaponScaleWight, pygame.image.load("images/pistol_sprites/1.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/pistol_sprites/2.png"), (pygame.image.load("images/pistol_sprites/2.png").get_width() * WeaponScaleWight, pygame.image.load("images/pistol_sprites/2.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/pistol_sprites/3.png"), (pygame.image.load("images/pistol_sprites/3.png").get_width() * WeaponScaleWight, pygame.image.load("images/pistol_sprites/3.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/pistol_sprites/4.png"), (pygame.image.load("images/pistol_sprites/4.png").get_width() * WeaponScaleWight, pygame.image.load("images/pistol_sprites/4.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/pistol_sprites/5.png"), (pygame.image.load("images/pistol_sprites/5.png").get_width() * WeaponScaleWight, pygame.image.load("images/pistol_sprites/5.png").get_height() * WeaponScaleHeight))
]

SpritesPistolShotScope = [
    pygame.transform.smoothscale(pygame.image.load("images/pistol_scope_shot/1.png"), (pygame.image.load("images/pistol_scope_shot/1.png").get_width() * WeaponScaleScopeWight, pygame.image.load("images/pistol_scope_shot/1.png").get_height() * WeaponScaleScopeHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/pistol_scope_shot/2.png"), (pygame.image.load("images/pistol_scope_shot/2.png").get_width() * WeaponScaleScopeWight, pygame.image.load("images/pistol_scope_shot/2.png").get_height() * WeaponScaleScopeHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/pistol_scope_shot/3.png"), (pygame.image.load("images/pistol_scope_shot/3.png").get_width() * WeaponScaleScopeWight, pygame.image.load("images/pistol_scope_shot/3.png").get_height() * WeaponScaleScopeHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/pistol_scope_shot/4.png"), (pygame.image.load("images/pistol_scope_shot/4.png").get_width() * WeaponScaleScopeWight, pygame.image.load("images/pistol_scope_shot/4.png").get_height() * WeaponScaleScopeHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/pistol_scope_shot/5.png"), (pygame.image.load("images/pistol_scope_shot/5.png").get_width() * WeaponScaleScopeWight, pygame.image.load("images/pistol_scope_shot/5.png").get_height() * WeaponScaleScopeHeight))
]

SpritesPistolReload = [
    pygame.transform.smoothscale(pygame.image.load("images/reload/1.png"), (pygame.image.load("images/reload/1.png").get_width() * WeaponScaleWight, pygame.image.load("images/reload/1.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/2.png"), (pygame.image.load("images/reload/2.png").get_width() * WeaponScaleWight, pygame.image.load("images/reload/2.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/3.png"), (pygame.image.load("images/reload/3.png").get_width() * WeaponScaleWight, pygame.image.load("images/reload/3.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/4.png"), (pygame.image.load("images/reload/4.png").get_width() * WeaponScaleWight, pygame.image.load("images/reload/4.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/5.png"), (pygame.image.load("images/reload/5.png").get_width() * WeaponScaleWight, pygame.image.load("images/reload/5.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/6.png"), (pygame.image.load("images/reload/6.png").get_width() * WeaponScaleWight, pygame.image.load("images/reload/6.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/7.png"), (pygame.image.load("images/reload/7.png").get_width() * WeaponScaleWight, pygame.image.load("images/reload/7.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/8.png"), (pygame.image.load("images/reload/8.png").get_width() * WeaponScaleWight, pygame.image.load("images/reload/8.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/9.png"), (pygame.image.load("images/reload/9.png").get_width() * WeaponScaleWight, pygame.image.load("images/reload/9.png").get_height() * WeaponScaleHeight))
]

PistolShotSound = pygame.mixer.Sound("sounds/shot_pistol.mp3")
PistolReloadSound = pygame.mixer.Sound("sounds/pistol_reload.mp3")

WeaponAnimCount = 0
AnimFrames = 0
AnimSpeedForShot = 12
AnimSpeedForReload = 12
ShotFlag = False
ReloadFlag = False
ScopeFlag = False
Ammo = 0
MaxAmmo = 6
