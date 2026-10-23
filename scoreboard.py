import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():
    """Uma classe para mostrar informações sobre pontuação."""
    
    def __init__(self, configs, screen, stats):
        """Inicializa os atributos da pontuação."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.configs = configs
        self.stats = stats
              
        # Configurações de fonte para as informações de pontuação
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        self.prep_ships() 
        # Prepara a imagem da pontuação inicial
        self.prep_score()
        self.prep_level()
        self.prep_high_score()

    def prep_score(self):
        """Transforma a pontuação em uma imagem renderizada."""
        rounded_score = int(round(self.stats.score, -1)) 
        # se um número negativo for passado como segundo argumento, round() 
        # arredondará o valor para o múltiplo mais próximo de 10, 100, 1.000
        score_str = f"{rounded_score:,}".replace(",", ".")
        #score_str = str(self.stats.score)
        
        self.score_image = self.font.render(score_str, True,self.text_color,self.configs.bg_color)
       
        # Exibe a pontuação na parte superior direita da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Desenha a pontuação na tela."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        # Desenha as espaçonaves
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """Transforma a pontuação máxima em uma imagem renderizada."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = f"Record: {high_score:,}".format(high_score).replace(",",".")
        self.high_score_image = self.font.render(high_score_str, True,
        self.text_color, self.configs.bg_color)
                
        # Centraliza a pontuação máxima na parte superior da tela
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_ships(self):
        """Mostra quantas espaçonaves restam."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen, self.configs)
            ship.image = pygame.transform.scale(ship.image, (32, 24)) #tamanho menor que a do jogador
            ship.rect = ship.image.get_rect()
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_level(self):
        """Transforma o nível em uma imagem renderizada."""
        
        self.level_image = self.font.render(str(self.stats.level), True,
        self.text_color, self.configs.bg_color)
               
        # Posiciona o nível abaixo da pontuação
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10