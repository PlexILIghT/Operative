import pygame
import data
import raycast
from pygame import Surface
from random import random


# Bot needs a player detection system.
# Bot should be able to change animations.
# Needs dynamic images!!!

class Enemy:
    image: Surface

    def __init__(self, start_pos, damage, health, speed):
        self.start_pos = start_pos
        self.damage = damage
        self.health = health
        self.speed = speed
        self.image = pygame.image.load("images/textures/enemy.jpg").convert_alpha()
        self.accuracy = 0.1

    def update(self):
        pass

    def get_image(self):
        return self.image

    def shoot(self):
        if raycast.raycast_all(0)[1] in data.worldMap and self.accuracy > random():
            pass
        pass

    def dead(self):
        # animate death
        pass

    def loose_hp(self):
        pass


enemies = []
for i in range(len(data.enemies_position)):
    enemies[i] = Enemy(data.enemies_position[i], 20, 100, 0.03)
