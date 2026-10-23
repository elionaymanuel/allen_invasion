import sys
from settings import Settings
from ship import Ship
import game_functions
import pygame
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #inicializa o jogo e cria objetos na tela
    pygame.init()
    configs = Settings() #o livro chama de ai_settings
    screen = pygame.display.set_mode((configs.screen_width,configs.screen_height))
    background = pygame.image.load("images/bg.bmp").convert()
    background = pygame.transform.scale(background, screen.get_size())
    pygame.transform.scale(background, screen.get_size())
    ship = Ship(screen,configs) #cria a nave
    aliens = Group()
    # Cria um grupo no qual serão armazenados os projéteis
    stats = GameStats(configs)
    score= Scoreboard(configs, screen, stats)
    bullets = Group()
    play_button = Button(configs,screen,"Play") #criando o botão de play
    pygame.display.set_caption ("Allen Invasion")
    game_functions.create_fleet (configs, screen,ship,aliens)
    #incia o loop principal do jogo
    
    while True:
        #observa eventos de teclado e de mouse
        game_functions.check_events(ship,configs,screen,bullets,stats,play_button,score,aliens)
        game_functions.update_screen(configs,screen,stats,score,ship,bullets,aliens,play_button,background)
        if stats.game_active:
            ship.update()
            game_functions.update_aliens(configs,stats,screen,score,ship,aliens,bullets)
            game_functions.update_bullets(configs,screen,stats,score,ship,aliens,bullets)
            

        

run_game()