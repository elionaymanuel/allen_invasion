import sys
from settings import Settings
from ship import Ship
import game_functions
import pygame
from pygame.sprite import Group

def run_game():
    #inicializa o jogo e cria um objeto na tela
    pygame.init()
    configs = Settings() #o livro chama de ai_settings
    screen = pygame.display.set_mode((configs.screen_width,configs.screen_height))
    ship = Ship(screen,configs)
    # Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()
    pygame.display.set_caption ("Allen Invasion")

    #incia o loop principal do jogo
    while True:
        #observa eventos de teclado e de mouse
        game_functions.check_events(ship,configs,screen,bullets)
        ship.update()
        bullets.update()
        #apagar os projeteis que desabaparecem
        
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        game_functions.update_screen(configs,screen,ship,bullets)

        

run_game()