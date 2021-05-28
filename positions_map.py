from mouse import *
from personages import *


class Position:
    def __init__(self, **kwargs):
        self.all_personages = {}
        for key, val in kwargs.items():
            self.all_personages[key] = val

    def normalize_pos(self, pos):
        return pos[0] * TILE, pos[1] * TILE


position_mission_1 = Position(hero=(hero.pos, 'H'),
                              hero2=(hero2.pos, 'H'),
                              enemy=(enemy.pos, 'E'),
                              enemy2=(enemy2.pos, 'E'))
