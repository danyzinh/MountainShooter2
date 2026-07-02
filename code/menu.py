#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE

# Comando para carregar sistema de áudio
pygame.mixer.init()

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png') # Carrega a imagem na tela
        self.rect = self.surf.get_rect(left = 0, top = 0) # Desenha um retângulo na tela

    def run(self, ):

        pygame.mixer.music.load('./asset/Menu.mp3')  # Carrega música
        pygame.mixer.music.play(-1) # Toca música indefinidamente
        while True:
            # Desenha uma imagem no retângulo
            self.window.blit(source=self.surf, dest=self.rect)
            # Desenha o nome na tela
            self.menu_text(50, 'Mountain', COLOR_ORANGE,((WIN_WIDTH / 2), 70))
            self.menu_text(50, 'Shooter', COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            # Cheque por todos os eventos (check for all events)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fecha janela
                    quit()  # Finaliza o pygame

    # Criando a Fonte
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name = 'Lucida Sans Type Writer', size = text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center = text_center_pos)
        self.window.blit(source = text_surf, dest = text_rect)



