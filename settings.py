
class Settings():
    """armazenamento de todas as configs do game"""
    def __init__(self):
        #configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        # cor de fundo
        self.bg_color = (230,230,230)
        # quantos pixels por vez a nave se movimenta na direção pressionada
        self.ship_speed_factor = 1.5 
        #configuração dos projeteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3 #largura do retangulo
        self.bullet_height = 15 # altura do retangulo
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.alien_speed_factor = 1