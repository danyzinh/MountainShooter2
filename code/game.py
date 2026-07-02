#!/usr/bin/python
# -*- coding: utf-8 -*

# Importando o Pygame
import pygame

from code.menu import Menu


class Game:
    def __init__(self):

        # Comando para inicializar o pygame
        pygame.init()

        # Variável para criar Janela
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self, ):

        # Loop para manter a janela aberta
        while True:
            menu = Menu(self.window)
            menu.run()
            pass




            ''' Cheque por todos os eventos (check for all events)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Fecha janela
                    quit() # Finaliza o pygame '''










