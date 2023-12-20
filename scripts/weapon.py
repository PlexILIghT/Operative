import pygame
import data
import raycast
from data import screen, game_clock

pygame.init()

#scale settings for sprites
weaponScaleWidth = data.screen_width / (data.screen_width * 1.6)
weaponScaleHeight = data.screen_height / (data.screen_height * 1.6)
weaponMeleeScaleWidth = data.screen_width/(data.screen_width * 0.5)
weaponMeleeScaleHeight = data.screen_height/(data.screen_height * 0.5)

#pistol settings
damageForPistol = 10
maxAmmoPistol = 6
animSpeedForShotPistol = 15
animSpeedForReloadPistol = 16
spritesPistolReload = []
spritesPistolShot = []

#M4 settings
maxAmmoM4 = 30
animSpeedForShotM4 = 100
animSpeedForReloadM4 = 12

#melee settings
animSpeedForMelee = 4
spritesMelee = []

# weapon animation

for i in range(1, 9, 1):
    spritesPistolShot.append(
        pygame.transform.smoothscale
        (pygame.image.load(f"images/pistol_sprites/{i}.png"),
         (pygame.image.load(f"images/pistol_sprites/{i}.png").get_width() * weaponScaleWidth,
         pygame.image.load(f"images/pistol_sprites/{i}.png").get_height() * weaponScaleHeight)))

for i in range(1, 32, 1):
    spritesPistolReload.append( pygame.transform.smoothscale(pygame.image.load(f"images/reload/{i}.png"), (
        pygame.image.load(f"images/reload/{i}.png").get_width() * weaponScaleWidth,
        pygame.image.load(f"images/reload/{i}.png").get_height() * weaponScaleHeight)))

for i in range(1, 7, 1):
    spritesMelee.append(
        pygame.transform.smoothscale(pygame.image.load(f"images/melee_sprites/{i}.png"), (
            pygame.image.load(f"images/melee_sprites/{i}.png").get_width() * weaponMeleeScaleWidth,
            pygame.image.load(f"images/melee_sprites/{i}.png").get_height() * weaponMeleeScaleHeight)))

pistol_shot_sound = pygame.mixer.Sound("sounds/shot_pistol.mp3")
pistol_reload_sound = pygame.mixer.Sound("sounds/pistol_reload.mp3")
meleeSound = pygame.mixer.Sound("sounds/MeleeSound.mp3")


class Weapon:
    def __init__(self, damage, spritesShot, spritesReload, maxAmmo, animSpeedForShot, animSpeedForReload, spritesMelee, shotSound, reloadSound, meleeSound, animSpeedForMelee):
        self.damage = damage
        self.spritesShot = list(spritesShot)
        self.spritesReload = list(spritesReload)
        self.maxAmmo = maxAmmo
        self.animSpeedForShot = animSpeedForShot
        self.animSpeedForReload = animSpeedForReload
        self.animSpeedForMelee = animSpeedForMelee
        self.trueAnimSpeedForShot = game_clock.get_fps() // self.animSpeedForShot
        self.trueAnimSpeedForReload = game_clock.get_fps() // self.animSpeedForReload
        self.trueAnimSpeedForMelee = game_clock.get_fps() // self.animSpeedForMelee
        self.spritesMelee = list(spritesMelee)
        self.shotSound = shotSound
        self.reloadSound = reloadSound
        self.meleeSound = meleeSound
        self.reloadFlag = False
        self.shotFlag = False
        self.meleeFlag = False
        self.ammo = 0
        self.animCount = 0
        self.animFrames = 0
        self.number = raycast.raycast_walls(0)

    def events(self):
        keys = pygame.key.get_pressed()
        mouseButton = pygame.mouse.get_pressed()
        self.trueAnimSpeedForShot = game_clock.get_fps() // self.animSpeedForShot + 1
        self.trueAnimSpeedForReload = game_clock.get_fps() // self.animSpeedForReload + 1
        self.trueAnimSpeedForMelee = game_clock.get_fps() // self.animSpeedForMelee + 1
        if (self.maxAmmo == self.ammo or keys[pygame.K_r]) and not self.shotFlag:
            self.reloadFlag = True
        elif mouseButton[0] and not self.reloadFlag:
            self.shotFlag = True
        elif keys[pygame.K_c]:
            self.meleeFlag = True

    def static(self):
        screen.blit(self.spritesShot[0], (
            data.screen_width / 2 - self.spritesShot[0].get_width()/4,
            data.screen_height - self.spritesShot[0].get_height()))

    def reload(self):
        self.trueAnimSpeedForReload = game_clock.get_fps() // self.animSpeedForReload + 1
        screen.blit(self.spritesReload[self.animCount], (
            data.screen_width / 2 - self.spritesReload[self.animCount].get_width()/4,
            data.screen_height - self.spritesReload[self.animCount].get_height()))
        if self.animFrames == 1:
            self.reloadSound.play()
        if self.animCount == len(self.spritesReload) - 1 and self.animFrames % self.trueAnimSpeedForReload == 0:
            self.animCount = 0
            self.animFrames = 0
            self.ammo = 0
            self.reloadFlag = False
        elif self.animFrames % self.trueAnimSpeedForReload == 0:
            self.animCount += 1
        self.animFrames += 1

    def check_for_hit(self):
        ray_hit_info = raycast.raycast_all(0)
        if ray_hit_info[1] == "e":
            data.enemies[tuple(ray_hit_info[2])].get_hit()
        elif ray_hit_info[1] == "c":
            data.map[ray_hit_info[2][1]][ray_hit_info[2][0]] = " "
            data.worldMap.pop((ray_hit_info[2][0] * data.blockSize, ray_hit_info[2][1] * data.blockSize))

    def shot(self):
        self.trueAnimSpeedForShot = game_clock.get_fps() // self.animSpeedForShot + 1
        screen.blit(self.spritesShot[self.animCount], (
            data.screen_width / 2 - self.spritesShot[0].get_width()/4,
            data.screen_height - self.spritesShot[self.animCount].get_height()))
        if self.animFrames == 1:
            self.shotSound.play()
            self.check_for_hit()
        if self.animCount == len(self.spritesShot) - 1 and self.animFrames % self.trueAnimSpeedForShot == 0:
            self.animCount = 0
            self.animFrames = 0
            self.ammo += 1
            self.shotFlag = False
        elif self.animFrames % self.trueAnimSpeedForShot == 0:
            self.animCount += 1
        self.animFrames += 1

    def melee(self):
        self.trueAnimSpeedForMelee = game_clock.get_fps() // self.animSpeedForMelee + 1
        screen.blit(self.spritesMelee[self.animCount], (
            data.screen_width / 2 - self.spritesMelee[self.animCount].get_width() / 2,
            data.screen_height - self.spritesMelee[self.animCount].get_height()))
        if self.animFrames == 1:
            self.meleeSound.play()
        if self.animCount == len(self.spritesMelee) - 1 and self.animFrames % self.trueAnimSpeedForMelee == 0:
            self.meleeFlag = False
            self.animCount = 0
            self.animFrames = 0
        elif self.animFrames % self.trueAnimSpeedForMelee == 0:
            self.animCount += 1
        self.animFrames += 1

    def draw_weapon(self):
        self.events()
        if self.reloadFlag:
            self.reload()
        elif self.shotFlag:
            self.shot()
        elif self.meleeFlag:
            self.melee()
        elif not self.shotFlag:
            self.static()

pistol = Weapon(damage=damageForPistol, spritesShot=spritesPistolShot, spritesReload=spritesPistolReload, maxAmmo=maxAmmoPistol, animSpeedForShot=animSpeedForShotPistol, animSpeedForReload=animSpeedForReloadPistol, spritesMelee=spritesMelee, shotSound=pistol_shot_sound, reloadSound=pistol_reload_sound, meleeSound=meleeSound, animSpeedForMelee=animSpeedForMelee)
m4 = Weapon(damage=damageForPistol, spritesShot=spritesPistolShot, spritesReload=spritesPistolReload, maxAmmo=maxAmmoM4, animSpeedForShot=animSpeedForShotM4, animSpeedForReload=animSpeedForReloadM4, spritesMelee=spritesMelee, shotSound=pistol_shot_sound, reloadSound=pistol_reload_sound, meleeSound=meleeSound, animSpeedForMelee=animSpeedForMelee)

class Selector:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.selectionFlag = False
    def selection(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.selectionFlag = False
        if keys[pygame.K_2]:
            self.selectionFlag = True

    def draw_selected_weapon(self):
        self.selection()
        if self.selectionFlag:
            self.second.draw_weapon()
        elif not self.selectionFlag:
            self.first.draw_weapon()

selector = Selector(m4, pistol)
