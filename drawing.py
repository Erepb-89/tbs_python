import pygame
from mouse import *


class Drawing:
    def __init__(self, sc, mouse):
        self.sc = sc
        self.mouse = mouse
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 36, bold=True)


    def world_map(self):
        for x, y in world_map:
            if world_map[(x, y)][0] == 'W':
                pygame.draw.rect(self.sc, DARK_ORANGE, (x, y, TILE, TILE), 2)

    def cursor_shadow(self):
        if self.mouse.object_type == '.' and not self.mouse.is_hero_checked:
            pygame.draw.rect(self.sc, WHITE, (int(self.mouse.map_coord[0]) * TILE,
                                              int(self.mouse.map_coord[1]) * TILE, TILE, TILE), 2)

    def marked_hero(self):
        if self.mouse.pers_type == 'H':
            pygame.draw.rect(self.sc, GREEN, (int(self.mouse.map_coord[0]) * TILE,
                                              int(self.mouse.map_coord[1]) * TILE, TILE, TILE), 2)

    def marked_hero_move(self):
        if self.mouse.is_hero_checked and \
                self.mouse.map_coord in self.mouse.selected_hero_path_check:
            for i in self.mouse.selected_hero_path_check:
                pygame.draw.rect(self.sc, GREEN, (i[0] * TILE, i[1] * TILE, TILE, TILE), 2)

            pygame.draw.rect(self.sc, BLUE, (int(self.mouse.map_coord[0]) * TILE,
                                             int(self.mouse.map_coord[1]) * TILE, TILE, TILE), 2)

    # def marked_pers_zone_attack(self):
    #     if self.mouse.is_hero_checked and \
    #             (self.mouse.map_coord == hero.pos or
    #              self.mouse.map_coord == hero2.pos):
    #         for zoa in self.mouse.zoa:
    #             pygame.draw.rect(self.sc, RED, (zoa[0] * TILE, zoa[1] * TILE, TILE, TILE), 2)

    def marked_hero_attack(self):
        if self.mouse.is_hero_checked and \
                (self.mouse.map_coord == enemy.pos or
                 self.mouse.map_coord == enemy2.pos) and \
                self.mouse.map_coord in self.mouse.zoa:
                    pygame.draw.rect(self.sc, BLUE, (int(self.mouse.map_coord[0]) * TILE,
                                             int(self.mouse.map_coord[1]) * TILE, TILE, TILE), 2)


    def marked_pers_move_range(self):
        if self.mouse.pers_can_move == 'H':
            for i in self.mouse.path_check:
                pygame.draw.rect(self.sc, GREEN, (i[0] * TILE, i[1] * TILE, TILE, TILE), 2)

            for zoa in self.mouse.zoa:
                pygame.draw.rect(self.sc, RED, (zoa[0] * TILE, zoa[1] * TILE, TILE, TILE), 2)

        elif self.mouse.pers_can_move == 'E':
            for i in self.mouse.path_check:
                pygame.draw.rect(self.sc, RED, (i[0] * TILE, i[1] * TILE, TILE, TILE), 2)

    def marked_enemy(self):
        if self.mouse.pers_type == 'E':
            pygame.draw.rect(self.sc, DARK_RED, (int(self.mouse.map_coord[0]) * TILE,
                                            int(self.mouse.map_coord[1]) * TILE, TILE, TILE), 2)


    def personage(self, pers):
        personage = pygame.Surface((100, 100))
        personage.fill(pers.color)
        rect = personage.get_rect()
        # print(rect)
        return personage

    def draw_personage_characteristics(self, pers):
        # self.sc.blit(self.font.render(str(pers.name), False, DARK_ORANGE),
        #              (pers.pos[0] * TILE, pers.pos[1] * TILE - 80))
        self.sc.blit(self.font.render(str(pers.health), False, DARK_RED),
                     (pers.pos[0] * TILE, pers.pos[1] * TILE - 40))
        self.sc.blit(self.font.render(str(pers.armor), False, DARK_BLUE),
                     (pers.pos[0] * TILE + 40, pers.pos[1] * TILE - 40))

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, False, DARK_ORANGE)
        self.sc.blit(render, FPS_POS)
