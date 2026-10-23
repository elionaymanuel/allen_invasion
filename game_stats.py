
class GameStats():
    """Armazena dados estatísticos da Invasão Alienígena."""
    
    def __init__(self, configs):
        """Inicializa os dados estatísticos."""
        self.configs = configs
        self.reset_stats()
        # A pontuação máxima jamais deverá ser reiniciada
        self.high_score = 0
        self.level = 1
        # Inicia a Invasão Alienígena em um estado INativo
        self.game_active = False

    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo."""
        self.ships_left = self.configs.ship_limit
        self.score = 0
        