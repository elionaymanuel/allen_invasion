import sys
from settings import Settings
from ship import Ship
import game_functions
import pygame
from pygame.sprite import Group

def run_game():
    #inicializa o jogo e cria objetos na tela
    pygame.init()
    configs = Settings() #o livro chama de ai_settings
    screen = pygame.display.set_mode((configs.screen_width,configs.screen_height))
    ship = Ship(screen,configs) #cria a nave
    aliens = Group()
    # Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()
    pygame.display.set_caption ("Allen Invasion")
    game_functions.create_fleet (configs, screen,ship,aliens)
    #incia o loop principal do jogo
    while True:
        #observa eventos de teclado e de mouse
        game_functions.check_events(ship,configs,screen,bullets)
        ship.update()
        game_functions.update_aliens(configs,aliens)
        game_functions.update_bullets(aliens,bullets)
        game_functions.update_screen(configs,screen,ship,bullets,aliens)

        

run_game()