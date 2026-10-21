import sys
from settings import Settings
from ship import Ship
import game_functions
import pygame
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    #inicializa o jogo e cria objetos na tela
    pygame.init()
    configs = Settings() #o livro chama de ai_settings
    screen = pygame.display.set_mode((configs.screen_width,configs.screen_height))
    ship = Ship(screen,configs) #cria a nave
    aliens = Group()
    # Cria um grupo no qual serão armazenados os projéteis
    stats = GameStats(configs)
    bullets = Group()
    pygame.display.set_caption ("Allen Invasion")
    game_functions.create_fleet (configs, screen,ship,aliens)
    #incia o loop principal do jogo
    while True:
        #observa eventos de teclado e de mouse
        game_functions.check_events(ship,configs,screen,bullets)
        if stats.game_active:
            ship.update()
            game_functions.update_aliens(configs,stats,screen,ship,aliens,bullets)
            game_functions.update_bullets(configs,screen,ship,aliens,bullets)
            game_functions.update_screen(configs,screen,ship,bullets,aliens)

        

run_game()