import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,ship,configs,screen,bullets):
    """responde a pressionamentos de tecla"""
    if event.key == pygame.K_RIGHT:
          ship.moving_right = True
    elif event.key == pygame.K_LEFT:
         ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #Cria um novo projetil
        new_bullet = Bullet(configs,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """ responde por soltura de tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship,configs,screen,bullets):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship,configs,screen,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
            
                

def update_screen (ai_settings,screen, ship,bullets):
    """atualiza as imagens da tela e alterna para a nova tela"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #redesenha a tela a cada passasem do laço
    
    ship.blitme()
    pygame.display.flip()