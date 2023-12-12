import pygame
import Data

pygame.init()

WeaponScaleWidth = Data.screenWidth/(Data.screenWidth * 0.3)
WeaponScaleHeight = Data.screenHeight/(Data.screenHeight * 0.3)
WeaponMeleeScaleHeight = Data.screenHeight/(Data.screenHeight * 0.5)
WeaponMeleeScaleWidth = Data.screenWidth/(Data.screenWidth * 0.5)

SpritesPistolShot = [
    pygame.transform.smoothscale(pygame.image.load("images/pistol_sprites/1.png"), (pygame.image.load("images/pistol_sprites/1.png").get_width() * WeaponScaleWidth, pygame.image.load("images/pistol_sprites/1.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/pistol_sprites/2.png"), (pygame.image.load("images/pistol_sprites/2.png").get_width() * WeaponScaleWidth, pygame.image.load("images/pistol_sprites/2.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/pistol_sprites/3.png"), (pygame.image.load("images/pistol_sprites/3.png").get_width() * WeaponScaleWidth, pygame.image.load("images/pistol_sprites/3.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/pistol_sprites/4.png"), (pygame.image.load("images/pistol_sprites/4.png").get_width() * WeaponScaleWidth, pygame.image.load("images/pistol_sprites/4.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/pistol_sprites/5.png"), (pygame.image.load("images/pistol_sprites/5.png").get_width() * WeaponScaleWidth, pygame.image.load("images/pistol_sprites/5.png").get_height() * WeaponScaleHeight))
]

SpritesPistolReload = [
    pygame.transform.smoothscale(pygame.image.load("images/reload/1.png"), (pygame.image.load("images/reload/1.png").get_width() * WeaponScaleWidth, pygame.image.load("images/reload/1.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/2.png"), (pygame.image.load("images/reload/2.png").get_width() * WeaponScaleWidth, pygame.image.load("images/reload/2.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/3.png"), (pygame.image.load("images/reload/3.png").get_width() * WeaponScaleWidth, pygame.image.load("images/reload/3.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/4.png"), (pygame.image.load("images/reload/4.png").get_width() * WeaponScaleWidth, pygame.image.load("images/reload/4.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/5.png"), (pygame.image.load("images/reload/5.png").get_width() * WeaponScaleWidth, pygame.image.load("images/reload/5.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/6.png"), (pygame.image.load("images/reload/6.png").get_width() * WeaponScaleWidth, pygame.image.load("images/reload/6.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/7.png"), (pygame.image.load("images/reload/7.png").get_width() * WeaponScaleWidth, pygame.image.load("images/reload/7.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/8.png"), (pygame.image.load("images/reload/8.png").get_width() * WeaponScaleWidth, pygame.image.load("images/reload/8.png").get_height() * WeaponScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/reload/9.png"), (pygame.image.load("images/reload/9.png").get_width() * WeaponScaleWidth, pygame.image.load("images/reload/9.png").get_height() * WeaponScaleHeight))
]

SpritesMelee = [
    pygame.transform.smoothscale(pygame.image.load("images/melee_sprites/1.png"), (pygame.image.load("images/melee_sprites/1.png").get_width() * WeaponMeleeScaleWidth, pygame.image.load("images/melee_sprites/1.png").get_height() * WeaponMeleeScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/melee_sprites/2.png"), (pygame.image.load("images/melee_sprites/2.png").get_width() * WeaponMeleeScaleWidth, pygame.image.load("images/melee_sprites/2.png").get_height() * WeaponMeleeScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/melee_sprites/1.png"), (pygame.image.load("images/melee_sprites/1.png").get_width() * WeaponMeleeScaleWidth, pygame.image.load("images/melee_sprites/1.png").get_height() * WeaponMeleeScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/melee_sprites/2.png"), (pygame.image.load("images/melee_sprites/2.png").get_width() * WeaponMeleeScaleWidth, pygame.image.load("images/melee_sprites/2.png").get_height() * WeaponMeleeScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/melee_sprites/1.png"), (pygame.image.load("images/melee_sprites/1.png").get_width() * WeaponMeleeScaleWidth, pygame.image.load("images/melee_sprites/1.png").get_height() * WeaponMeleeScaleHeight)),
    pygame.transform.smoothscale(pygame.image.load("images/melee_sprites/2.png"), (pygame.image.load("images/melee_sprites/2.png").get_width() * WeaponMeleeScaleWidth, pygame.image.load("images/melee_sprites/2.png").get_height() * WeaponMeleeScaleHeight))
]

MeleeAttackSound = pygame.mixer.Sound("sounds/MeleeSound.mp3")

MeleeAttackFlag = False

PistolShotSound = pygame.mixer.Sound("sounds/shot_pistol.mp3")
PistolReloadSound = pygame.mixer.Sound("sounds/pistol_reload.mp3")

WeaponAnimCount = 0
AnimFrames = 0
AnimSpeedForShot = 12
AnimSpeedForReload = 12
AnimSpeedForMelee = 4
ShotFlag = False
ReloadFlag = False
Ammo = 0
MaxAmmo = 6
