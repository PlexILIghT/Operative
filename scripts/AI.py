import pygame
from random import random
import player


# Bot needs a player detection system.
# Bot should be able to change animations.

class Enemy:

    def __init__(self, start_pos, damage, health):
        self.start_pos = start_pos
        self.damage = damage
        self.health = health
        self.state = "alive"
        self.accuracy = 0.1

    def dead(self):
        self.state = "dead_animation"
        pass

    def get_hit(self):
        self.health -= player.damage
        self.state = "hurt"
        if self.health <= 0:
            self.dead()
