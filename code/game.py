#!/usr/bin/python
# -*- coding: utf-8 -*

# Importando o Pygame
import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):

        # Comando para inicializar o pygame
        pygame.init()

        # Variável para criar Janela
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):

        # Loop para manter a janela aberta
        while True:
            menu = Menu(self.window)
            menu.run()
            pass















