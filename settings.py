
class Settings():
    """armazenamento de todas as configs do game"""
    def __init__(self):
        """Inicializa as configurações estáticas do jogo."""
        #configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        # cor de fundo
        self.bg_color = (230,230,230)
        # quantos pixels por vez a nave se movimenta na direção pressionada
        self.ship_limit = 3
        #configuração dos projeteis
        self.bullet_width = 50 #largura do retangulo (3)
        self.bullet_height = 15 # altura do retangulo
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings() #configs dinamicas

        #vidas:
        
    def initialize_dynamic_settings(self):
        """Inicializa as configurações que mudam no decorrer do
        jogo."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1
        # fleet_direction igual a 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Aumenta as configurações de velocidade."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)