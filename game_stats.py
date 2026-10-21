
class GameStats():
    """Armazena dados estatísticos da Invasão Alienígena."""
    
    def __init__(self, configs):
        """Inicializa os dados estatísticos."""
        self.configs = configs
        self.reset_stats()
        # Inicia a Invasão Alienígena em um estado ativo
        self.game_active = True

    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo."""
        self.ships_left = self.configs.ship_limit