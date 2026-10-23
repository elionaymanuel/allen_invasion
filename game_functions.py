import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event,ship,configs,screen,bullets,stats,score,aliens):
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
    elif event.key ==pygame.K_RETURN or event.key ==pygame.K_KP_ENTER:
        iniciar_new_game(stats,score,configs,screen, ship,aliens,bullets)
    
def iniciar_new_game(stats,score,configs,screen,ship,aliens,bullets):
    pygame.mouse.set_visible(False)
    aliens.empty()
    bullets.empty()
    ship.center_ship()
    create_fleet(configs,screen,ship,aliens)
    stats.reset_stats()
    score.prep_score()
    score.prep_high_score()
    score.prep_ships()
    configs.initialize_dynamic_settings()
    stats.game_active = True

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


def check_events(ship,configs,screen,bullets,stats,play_button,score,aliens):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship,configs,screen,bullets,stats,score,aliens)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_mouse_play_button(configs,stats, play_button, mouse_x, mouse_y,score,screen,ship,aliens,bullets)
        


def check_mouse_play_button(configs,stats, play_button, mouse_x, mouse_y,score,screen,ship,aliens,bullets):
    """Inicia um novo jogo quando o jogador clicar em Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        iniciar_new_game(stats,score,configs,screen,ship,aliens,bullets)
                
def update_bullets(configs,screen,stats,score,ship,aliens,bullets):
    """atualiza a posicao dos projeteis e se livra dos projeteis antigos"""
    #atualiza a posição dos projeteis
    bullets.update()
    #livra-se dos projéteis que desapareceram
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(configs, screen,score,stats, ship, aliens,bullets)

def check_bullet_alien_collisions(configs,screen,score,stats,ship,aliens,bullets):
    "responde a colisoes entre projeteis e alienigenas"
    #remove qualquer projetil e alien que tenham colidido:
    collisions = pygame.sprite.groupcollide(bullets, aliens, True,True)
    if collisions:
        for aliens in collisions.values(): 
            #pra garantir que se um bala grande atingir 2 aliens ao mesmo tempo o score seja incrementado
            stats.score += configs.alien_points * len(aliens)
            score.prep_score()
        check_high_score(stats, score)
    if len(aliens) == 0:
        # Destrói os projéteis existentes e cria uma nova frota
        bullets.empty()
        configs.increase_speed()
        create_fleet(configs, screen, ship, aliens)




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

def check_fleet_edges(ai_settings, aliens):
    """Responde apropriadamente se algum alienígena alcançou uma  borda."""
    
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Faz toda a frota descer e muda a sua direção."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(configs,stats,screen,score,ship,aliens,bullets):
    """
        Verifica se a frota está em uma das bordas
        e então atualiza as posições de todos os alienígenas da frota.
    """
    check_fleet_edges(configs,aliens)
    aliens.update()
    # Verifica se houve colisões entre alienígenas e a espaçonave
    '''
            O método spritecollideany() aceita dois argumentos: um sprite e um
        grupo. O método verifica se algum membro do grupo colidiu com o sprite
        e para de percorrer o grupo assim que encontrar um membro que tenha
        colidido com o sprite. 
    '''
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(configs, stats, screen,score, ship, aliens, bullets)
    
    # Verifica se há algum alienígena que atingiu a parte inferior da tela
    check_aliens_bottom(configs, stats, screen, ship, aliens, bullets)

def ship_hit(configs, stats, screen,score, ship, aliens, bullets):
    """Responde ao fato de a espaçonave ter sido atingida por um alienígena."""
    # Decrementa ships_left
    if stats.ships_left > 0:
        stats.ships_left -= 1
        # Atualiza o painel de pontuações
        score.prep_ships() 
        # Esvazia a lista de alienígenas e de projéteis
        aliens.empty()
        bullets.empty()
        # Cria uma nova frota e centraliza a espaçonave
        create_fleet(configs, screen, ship, aliens)
        ship.center_ship() #centraliza pra iniciar um novo game
        # Faz uma pausa
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(configs, stats, screen, ship, aliens, bullets):
    """Verifica se algum alienígena alcançou a parte inferior da  tela."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
        # Trata esse caso do mesmo modo que é feito quando a espaçonave é atingida
            ship_hit(configs, stats, screen, ship, aliens, bullets)
            break

def check_high_score(stats, score):
    """Verifica se há uma nova pontuação máxima."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.prep_high_score()

def update_screen (configs,screen,stats,score, ship,bullets, aliens,play_button,background):
    """atualiza as imagens da tela e alterna para a nova tela"""
    screen.blit(background, (0, 0))
    if stats.game_active:
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        aliens.draw(screen)
        #redesenha a tela a cada passasem do laço
        ship.blitme()
        score.show_score()
    else:
        play_button.draw_button()
    pygame.display.flip()