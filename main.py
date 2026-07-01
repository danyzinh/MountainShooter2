# Importando o Pygame
import pygame

# Começando o código
print('Setup Start')

# Comando para inicializar o pygame
pygame.init()

# Variável para criar Janela
window = pygame.display.set_mode(size = (600, 480))

# Loop para manter a janela aberta
while True:
    # Cheque por todos os eventos (check for all events)
    for event in pygame.event.get(): # Vai checar eventos
        if event.type == pygame.QUIT: # Sair
            pygame.quit() # Fechar Janela
            quit() # Encerrar a inicialização do Pygame





