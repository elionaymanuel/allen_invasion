import sys
from settings import Settings
from ship import Ship
import game_functions
import pygame

def run_game():
    #inicializa o jogo e cria um objeto na tela
    pygame.init()
    configs = Settings() #o livro chama de ai_settings
    screen = pygame.display.set_mode((configs.screen_width,configs.screen_height))
    ship = Ship(screen,configs)
    pygame.display.set_caption ("Allen Invasion")

    #incia o loop principal do jogo
    while True:
        #observa eventos de teclado e de mouse
        game_functions.check_events(ship)
        ship.update()
        game_functions.update_screen(configs,screen,ship)

        

run_game()