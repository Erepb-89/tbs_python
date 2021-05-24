import pygame
from settings import *
from mouse import *
from drawing import *
from positions_map import position_mission_1
from personages import hero, hero2, enemy, enemy2
from map import world_map


class RPGPython:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""

        self.sc = pygame.display.set_mode((WIDTH, HEIGHT))
        self.mouse = Mouse()
        self.drawing = Drawing(self.sc, self.mouse)
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 36, bold=True)

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        pygame.init()
        clock = pygame.time.Clock()
        pygame.mouse.set_visible(True)

        self.sc.fill(BLACK)

        self.mouse.movement()
        self.drawing.world_map()
        self.sc.blit(self.drawing.personage(hero),
                     position_mission_1.normalize_pos(position_mission_1.all_personages['hero'][0]))
        self.sc.blit(self.drawing.personage(hero2),
                     position_mission_1.normalize_pos(position_mission_1.all_personages['hero2'][0]))
        self.sc.blit(self.drawing.personage(enemy),
                     position_mission_1.normalize_pos(position_mission_1.all_personages['enemy'][0]))
        self.sc.blit(self.drawing.personage(enemy2),
                     position_mission_1.normalize_pos(position_mission_1.all_personages['enemy2'][0]))

        self.drawing.draw_personage_characteristics(hero)
        self.drawing.draw_personage_characteristics(hero2)
        self.drawing.draw_personage_characteristics(enemy)
        self.drawing.draw_personage_characteristics(enemy2)


        self.drawing.cursor_shadow()
        self.drawing.marked_hero()
        self.drawing.marked_pers_move_range()
        self.drawing.marked_hero_move()
        self.drawing.marked_enemy()
        self.mouse.hero_move()

        # self.drawing.fps(clock)

        clock.tick()
        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    rpg = RPGPython()
    rpg.run_game()
