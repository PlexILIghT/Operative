import player
import data


class Enemy:

    def __init__(self, start_pos, damage, health):
        self.start_pos = start_pos
        self.damage = damage
        self.health = health
        self.state = "alive"
        self.accuracy = 0.1
        self.frame = 0

    def shoot(self):
        player.get_hit(self.damage)
        print(player.health)

    def dead(self):
        self.state = "dead_animation"
        self.frame = 0
        data.map[self.start_pos[1]][self.start_pos[0]] = " "

    def get_hit(self):
        self.frame = 0
        self.health -= player.damage
        self.state = "hurt"
        if self.health <= 0:
            self.dead()

    def get_frame(self):
        if self.state == "alive":
            if self.frame < 14:
                self.frame += 1
                if self.frame == 5:
                    self.shoot()
            else:
                self.frame = 0
            return data.textures["alive_enemy"][self.frame]
        elif self.state == "hurt":
            if self.frame < 25:
                self.frame += 1
            else:
                self.frame = 0
                self.state = "alive"
            return data.textures["hurt_enemy"][self.frame]
        elif self.state == "dead_animation":
            if self.frame < 29:
                self.frame += 1
            else:
                self.state = "dead"
            return data.textures["dead_enemy"][self.frame]
        elif self.state == "dead":
            return data.textures["dead_enemy"][-1]
