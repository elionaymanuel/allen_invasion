import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ship,configs,screen,bullets):
    """responde a pressionamentos de tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #Cria um novo projetil
        fire_bullet(configs, screen, ship,bullets)
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
        sys.exit()
    
       

def fire_bullet (configs,screen, ship, bullets):
    """Dispara um projétil se o limite ainda nao foi alcançado"""
    if len(bullets)< configs.bullets_allowed:
        new_bullet = Bullet(configs,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """ responde por soltura de tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ship,configs,screen,bullets):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship,configs,screen,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
            
                
def update_bullets(bullets):
    """atualiza a posicao dos projeteis e se livra dos projeteis antigos"""
    #atualiza a posição dos projeteis
    bullets.update()
    #livra-se dos projéteis que desapareceram
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            #print(len(bullets))




def get_number_aliens_x(configs, alien_width):
    """Determina o número de alienígenas que cabem em uma linha."""
    available_space_x = configs.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determina o número de linhas com alienígenas que cabem na tela."""
    
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number,row_number):
    # Cria um alienígena e o posiciona na linha
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(configs,screen,ship,aliens):
    """cria frota completa de aliens"""
    alien = Alien(configs,screen)
    number_rows = get_number_rows (configs, ship.rect.height, alien.rect.height)
    #cria a primeira linha de aliens
    for row_number in range(number_rows):
        for alien_number in range(get_number_aliens_x(configs,alien.rect.width)):
            create_alien (configs,screen,aliens,alien_number,row_number)

def update_aliens(aliens):
    """Atualiza as posições de todos os alienígenas da frota."""
    aliens.update()
    
def update_screen (ai_settings,screen, ship,bullets, aliens):
    """atualiza as imagens da tela e alterna para a nova tela"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    aliens.draw(screen)
    #redesenha a tela a cada passasem do laço
    ship.blitme()
    pygame.display.flip()