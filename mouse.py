from settings import *
from map import world_map
from positions_map import position_mission_1
from personages import hero, hero2, enemy, enemy2
import pygame


class Mouse:
    def __init__(self):
        self.hero_checked = False
        self.pers_type = ''
        self.zoa = []

    def movement(self):
        self.check_mouse_events()
        self.mouse_control()
        self.get_mouse_coordinates()
        self.get_object_type()
        self.is_hero_or_enemy()
        self.is_pers_can_move()
        self.get_speed()
        self.hero_attack(hero)
        # self.hero_attack(hero2)

    def check_mouse_events(self):
        self.left_click = False
        self.right_click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                self.left_click = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                self.right_click = True

    def mouse_control(self):
        if pygame.mouse.get_focused():
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

    def get_mouse_coordinates(self):
        for key, val in world_map.items():
            if self.mouse_x in range(key[0], key[0] + TILE) and \
                    self.mouse_y in range(key[1], key[1] + TILE):
                self.mouse_coordinates = key[0], key[1]
                # print('coord: ', self.mouse_coordinates)
                self.object_type = world_map[key][0]
                # print('type: ', self.object_type)
                self.map_coord = world_map[key][1]
                # print(self.map_coord)

                for key2, val2 in position_mission_1.all_personages.items():
                    if self.map_coord == val2[0]:
                        if 'hero' in key2:
                            self.pers_type = 'H'
                        elif 'enemy' in key2:
                            self.pers_type = 'E'

                    else:
                        self.pers_type = ''

                # self.pers_type = position_mission_1.all_personages[key]

    @property
    def get_pers_coordinates(self):
        if self.is_hero_checked and self.pers_type == 'H':
            if self.map_coord == hero.pos:
                self.coord = hero.pos
            elif self.map_coord == hero2.pos:
                self.coord = hero2.pos
        return self.coord

    def get_speed(self):
        if self.pers_type == 'H':
            self.speed = hero_speed
        elif self.pers_type == 'E' and not self.is_hero_checked:
            self.speed = enemy_speed

    @property
    def path_check(self):
        all_fields = set()
        self.can_move_fields = set()
        if self.pers_type == 'H' or self.pers_type == 'E' or self.is_ground or self.is_wall:
            min_x = self.map_coord[0] - self.speed
            max_x = self.map_coord[0] + self.speed + 1
            min_y = self.map_coord[1] - self.speed
            max_y = self.map_coord[1] + self.speed + 1

            if min_x < 0: min_x = 0
            if max_x > 12: max_x = 12
            if min_y < 0: min_y = 0
            if max_y > 8: max_y = 8

            for i in range(min_x, max_x):
                for j in range(min_y, max_y):
                    if abs(j - self.map_coord[1]) + abs(i - self.map_coord[0]) <= self.speed:
                        all_fields.add((i, j))

            for field in all_fields:
                for val in world_map.values():
                    if '.' in val[0] and val[1] == field and \
                            val[1] != hero.pos and \
                            val[1] != hero2.pos and \
                            val[1] != enemy.pos and \
                            val[1] != enemy2.pos:
                        self.can_move_fields.add(val[1])

            # print(self.can_move_fields)
            return self.can_move_fields

    @property
    def selected_hero_path_check(self):
        all_fields = set()
        self.can_move_fields = set()
        if self.pers_type == 'H' or self.pers_type == 'E' or self.is_ground or self.is_wall:
            min_x = self.get_pers_coordinates[0] - self.speed
            max_x = self.get_pers_coordinates[0] + self.speed + 1
            min_y = self.get_pers_coordinates[1] - self.speed
            max_y = self.get_pers_coordinates[1] + self.speed + 1
            if min_x < 0: min_x = 0
            if max_x > 12: max_x = 12
            if min_y < 0: min_y = 0
            if max_y > 8: max_y = 8

            for i in range(min_x, max_x):
                for j in range(min_y, max_y):
                    if abs(j - self.get_pers_coordinates[1]) + abs(i - self.get_pers_coordinates[0]) <= self.speed:
                        all_fields.add((i, j))

            for field in all_fields:
                for val in world_map.values():
                    if '.' in val and val[1] == field and \
                            val[1] != hero.pos and \
                            val[1] != hero2.pos and \
                            val[1] != enemy.pos and \
                            val[1] != enemy2.pos:
                        self.can_move_fields.add(val[1])

            # print(self.can_move_fields)
            return self.can_move_fields

    def get_object_type(self):
        if self.pers_type == 'H':
            pygame.mouse.set_cursor(*pygame.cursors.tri_right)
        if self.pers_type == 'E':
            pygame.mouse.set_cursor(*pygame.cursors.broken_x)
        if self.object_type == '.' and self.pers_type != 'H' and self.pers_type != 'E':
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
        if self.object_type == 'W' and self.pers_type != 'H' and self.pers_type != 'E':
            pygame.mouse.set_cursor(*pygame.cursors.diamond)

    @property
    def is_wall(self):
        """Проверка при наведеии, стена"""
        self.wall = False
        if self.object_type == 'W':
            # print('Wall')
            self.wall = True
        return self.wall

    @property
    def is_ground(self):
        """Проверка при наведеии, земля"""
        self.ground = False
        if self.object_type == '.':
            # print('Ground, digging OK')
            self.ground = True

        return self.ground

    def is_hero_or_enemy(self):
        """Проверка при наведеии, герой или враг"""
        self.pers_type = ''
        for key, val in position_mission_1.all_personages.items():
            if self.map_coord == val[0]:
                if 'hero' in key:
                    self.pers_type = 'H'
                elif 'enemy' in key:
                    self.pers_type = 'E'
        return self.pers_type

    def is_pers_can_move(self):
        """Проверка при нажатии, куда может пойти персонаж"""
        self.pers_can_move = ''
        pressed = pygame.mouse.get_pressed()
        if pressed[2] and self.pers_type == 'H':
            # print('Hero can move')
            self.pers_can_move = 'H'
            self.hero_checked = False
        # elif pressed[2] and self.pers_type == 'E':
        if not self.hero_checked and self.pers_type == 'E':
            # print('Enemy can move')
            self.pers_can_move = 'E'
            self.hero_checked = False
        return self.pers_can_move

    @property
    def is_hero_checked(self):
        """Проверка при нажатии, герой"""
        pressed = pygame.mouse.get_pressed()
        if pressed[0] and self.pers_type == 'H':
            self.hero_checked = True
        return self.hero_checked

    def zone_attack(self, pers):
        if self.is_hero_checked and self.coord == pers.pos:

            self.zoa = [
                        (int(self.coord[0]), int(self.coord[1] + pers.zone_of_attack)),
                        (int(self.coord[0]), int(self.coord[1] - pers.zone_of_attack)),
                        (int(self.coord[0] + pers.zone_of_attack), int(self.coord[1])),
                        (int(self.coord[0] - pers.zone_of_attack), int(self.coord[1]))
                        ]

        return self.zoa


    def hero_move(self):
        """Ходьба, герой"""
        pressed = pygame.mouse.get_pressed()
        if self.hero_checked:
            if pressed[0] and \
                    self.map_coord in self.can_move_fields and \
                    self.coord == position_mission_1.all_personages['hero'][0]:
                position_mission_1.all_personages['hero'] = self.map_coord, 'H'
                hero.pos = self.map_coord
                print(hero.pos)
                self.hero_checked = False

            elif pressed[0] and \
                    self.map_coord in self.can_move_fields and \
                    self.coord == position_mission_1.all_personages['hero2'][0]:
                position_mission_1.all_personages['hero2'] = self.map_coord, 'H'
                hero2.pos = self.map_coord
                print(hero2.pos)
                self.hero_checked = False


    def hero_attack(self, pers):
        """Атака, герой"""
        if self.hero_checked:
            if self.left_click and self.map_coord == enemy.pos and self.map_coord in self.zoa:
                print(enemy.pos)
                pers.attack_for_health(enemy)
            if self.right_click and self.map_coord == enemy.pos and self.map_coord in self.zoa:
                print(enemy.pos)
                pers.attack_for_armor(enemy)

            elif self.left_click and self.map_coord == enemy2.pos and self.map_coord in self.zoa:
                pers.attack_for_health(enemy2)
                print(enemy2.pos)
            elif self.right_click and self.map_coord == enemy2.pos and self.map_coord in self.zoa:
                pers.attack_for_armor(enemy2)
                print(enemy2.pos)
