import pygame
import data
import raycast
from data import screen, game_clock

pygame.init()

class Weapon:
    def __init__(self, damage, spritesShot, spritesReload, maxAmmo, animSpeedForShot, animSpeedForReload, shotSound, reloadSound):
        self.damage = damage
        self.spritesShot = list(spritesShot)
        self.spritesReload = list(spritesReload)
        self.maxAmmo = maxAmmo
        self.animSpeedForShot = animSpeedForShot
        self.animSpeedForReload = animSpeedForReload
        self.shotSound = shotSound
        self.reloadSound = reloadSound
        self.reloadFlag = False
        self.shotFlag = False
        self.meleeFlag = False
        self.ammo = 0
        self.animCount = 0
        self.animFrames = 0

    def events(self):
        keys = pygame.key.get_pressed()
        mouseButton = pygame.mouse.get_pressed()
        if keys[pygame.K_r] and not self.shotFlag and not self.meleeFlag and not data.swapFlag:
            self.reloadFlag = True
        elif mouseButton[0] and not self.reloadFlag and not self.meleeFlag and not data.swapFlag:
            self.shotFlag = True
        elif keys[pygame.K_c] and not self.reloadFlag and not self.shotFlag and not data.swapFlag:
            self.meleeFlag = True

    def static(self):
        screen.blit(self.spritesShot[0], (
            data.screen_width / 2 - self.spritesShot[0].get_width()/2,
            data.screen_height - self.spritesShot[0].get_height()))

    def reload(self):
        self.trueAnimSpeedForReload = game_clock.get_fps() // self.animSpeedForReload + 1
        screen.blit(self.spritesReload[self.animCount], (
            data.screen_width / 2 - self.spritesReload[self.animCount].get_width()/2,
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
        if self.ammo != self.maxAmmo:
            self.trueAnimSpeedForShot = game_clock.get_fps() // self.animSpeedForShot + 1
            screen.blit(self.spritesShot[self.animCount], (
                data.screen_width / 2 - self.spritesShot[0].get_width()/2,
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
        else:
            self.static()
            self.shotFlag = False

    def melee(self):
        self.trueAnimSpeedForMelee = game_clock.get_fps() // data.animSpeedForMelee + 1
        screen.blit(data.spritesMelee[self.animCount], (
            data.screen_width / 2 - data.spritesMelee[self.animCount].get_width() / 2,
            data.screen_height - data.spritesMelee[self.animCount].get_height()))
        if self.animFrames == 1:
            data.meleeSound.play()
        if self.animCount == len(data.spritesMelee) - 1 and self.animFrames % self.trueAnimSpeedForMelee == 0:
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
        elif not self.shotFlag and not data.swapFlag:
            self.static()


pistol = Weapon(data.damageForPistol, data.spritesPistolShot, data.spritesPistolReload, data.maxAmmoPistol, data.animSpeedForShotPistol, data.animSpeedForReloadPistol, data.pistolShotSound, data.pistolReloadSound)
m4 = Weapon(data.damageForM4, data.m4Shot, data.m4reload, data.maxAmmoM4, data.animSpeedForShotM4, data.animSpeedForReloadM4, data.m4shotSound, data.m4reloadSound)


class Selector:

    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.selectionFlag = False
        self.animCount = 0
        self.animFrames = 0
        self.swapToFirst = False
        self.swapToSecond = False

    def swap_to_first(self):
        trueAnimSpeedForSwap = game_clock.get_fps() // data.animSpeedForSwap + 1
        screen.blit(data.swapToFirst[self.animCount], (
            data.screen_width / 2 - data.swapToFirst[0].get_width() / 2,
            data.screen_height - data.swapToFirst[0].get_height()))
        if self.animCount == 1:
            data.swapSound.play()
            self.animCount += 1
        elif self.animCount == len(data.swapToFirst) - 1 and self.animFrames % trueAnimSpeedForSwap == 0:
            self.animCount = 0
            self.animFrames = 0
            self.swapToFirst = False
            data.swapFlag = False
            self.selectionFlag = False
        elif self.animFrames % trueAnimSpeedForSwap == 0:
            self.animCount += 1
        self.animFrames += 1

    def swap_to_second(self):
        trueAnimSpeedForSwap = game_clock.get_fps() // data.animSpeedForSwap + 1
        screen.blit(data.swapToSecond[self.animCount], (
            data.screen_width / 2 - data.swapToSecond[0].get_width() / 2,
            data.screen_height - data.swapToSecond[0].get_height()))
        if self.animCount == 1:
            data.swapSound.play()
            self.animCount += 1
        elif self.animCount == len(data.swapToSecond) - 1 and self.animFrames % trueAnimSpeedForSwap == 0:
            self.animCount = 0
            self.animFrames = 0
            self.swapToSecond = False
            data.swapFlag = False
            self.selectionFlag = True
        elif self.animFrames % trueAnimSpeedForSwap == 0:
            self.animCount += 1
        self.animFrames += 1

    def selection(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] and self.selectionFlag and not pistol.reloadFlag and not pistol.meleeFlag:
            data.swapFlag = True
            self.swapToFirst = True
        if keys[pygame.K_2] and not self.selectionFlag and not m4.reloadFlag and not pistol.meleeFlag:
            data.swapFlag = True
            self.swapToSecond = True

    def draw_selected_weapon(self):
        self.selection()
        if self.swapToFirst:
            self.swap_to_first()
        elif self.swapToSecond:
            self.swap_to_second()
        elif self.selectionFlag:
            pistol.draw_weapon()
        else:
            m4.draw_weapon()

selector = Selector(m4, pistol)
