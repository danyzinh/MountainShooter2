#!/usr/bin/python
# -*- coding: utf-8 -*

# Importando o Pygame
import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):

        # Comando para inicializar o pygame
        pygame.init()

        # Variável para criar Janela
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):

        # ‘Loop’ para manter a janela aberta
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0] # [Player1, Player2]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)



            elif menu_return == MENU_OPTION[4]:
                pygame.quit() # Close window
                quit() # End pygame
            else:
                pass
















