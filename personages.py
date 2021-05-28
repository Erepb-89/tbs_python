from settings import *


class Pers:
    def __init__(self, name, type, speed, color, health, armor, break_armor, zone_of_attack, pos, checked):
        self.name = name
        self.type = type
        self.speed = speed
        self.color = color
        self.health = health
        self.armor = armor
        self.break_armor = break_armor
        self.zone_of_attack = zone_of_attack
        self.pos = pos
        self.checked = checked

    def attack_for_health(self, attacked_pers):
        damage = self.health - attacked_pers.armor
        if damage < 1:
            damage = 1
        attacked_pers.health -= damage

        if attacked_pers.health < 0:
            attacked_pers.health = 0

    def attack_for_armor(self, attacked_pers):
        damage = self.break_armor
        attacked_pers.armor -= damage

        if attacked_pers.armor < 0:
            attacked_pers.armor = 0


hero = Pers('Thanos', 'H', 3, PURPLE, 12, 10, 3, 1, (1, 4), False)
hero2 = Pers('Cap', 'H', 3, BLUE, 11, 9, 4, 1, (2, 2), False)
enemy = Pers('Bull', 'E', 2, RED, 13, 8, 2, 1, (3, 4), False)
enemy2 = Pers('Chicken', 'E', 3, RED, 10, 18, 1, 2, (7, 5), False)
