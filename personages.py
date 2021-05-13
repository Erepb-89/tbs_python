from settings import *


class Pers:
    def __init__(self, name, type, speed, color, health, armor):
        self.name = name
        self.type = type
        self.speed = speed
        self.color = color
        self.health = health
        self.armor = armor


hero = Pers('Thanos', 'H', 3, BLUE, 12, 10)
enemy = Pers('Bull', 'E', 2, RED, 10, 8)
enemy2 = Pers('Chicken', 'E', 3, RED, 10, 8)
