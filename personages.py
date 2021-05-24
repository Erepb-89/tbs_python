from settings import *


class Pers:
    def __init__(self, name, type, speed, color, health, armor, pos):
        self.name = name
        self.type = type
        self.speed = speed
        self.color = color
        self.health = health
        self.armor = armor
        self.pos = pos


hero = Pers('Thanos', 'H', 3, PURPLE, 12, 10, (1, 4))
hero2 = Pers('Cap', 'H', 3, BLUE, 11, 9, (2, 2))
enemy = Pers('Bull', 'E', 2, RED, 10, 8, (3, 4))
enemy2 = Pers('Chicken', 'E', 3, RED, 10, 8, (7, 5))
