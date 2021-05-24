from mouse import *
from personages import *


class Position:
    def __init__(self, **kwargs):
        self.all_personages = {}
        for key, val in kwargs.items():
            self.all_personages[key] = val

    def normalize_pos(self, pos):
        return pos[0] * TILE, pos[1] * TILE


position_mission_1 = Position(hero=((1, 4), 'H'),
                              hero2=((2, 2), 'H'),
                              enemy=((3, 4), 'E'),
                              enemy2=((7, 5), 'E'))
