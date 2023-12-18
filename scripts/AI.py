# Bot should have weapon with him.
# Bot needs to navigate through map.
# Bot needs a player detection system.
# Bot should be able to change animations.
# rename for enemies


class Bot:

    def __init__(self, damage, health, speed):
        self.damage = damage
        self.health = health
        self.speed = speed

    def move(self, x, y):
        pass
    def look_for_player(self):
        pass

    def shooting(self):
        pass

    def dead(self):
        pass

    def lose_hp(self, other: int):
        self.health -= int


