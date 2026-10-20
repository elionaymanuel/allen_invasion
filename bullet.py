import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Uma classe que administra projéteis disparados pela nave"""
    def __init__(self, configs,screen, ship):
        """cria um objeto para o prjetil na posiçao atual da nave"""
        super().__init__()
        self.screen = screen
        # Cria um retângulo para o projétil em (0, 0) e, em seguida,define a
        # posição correta
        self.rect = pygame.Rect(0,0,configs.bullet_width, configs.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Armazena a posição do projétil como um valor decimal
        self.y = float(self.rect.y)
        self.color = configs.bullet_color
        self.speed_factor = configs.bullet_speed_factor
    
    def update(self):
        """Move o projetil para cima na tela."""
        self.y -= self.speed_factor
        #atualiza a posicao de rect
        self.rect.y = self.y

    def draw_bullet(self):
        """desenha o projetil na tela"""
        pygame.draw.rect(self.screen,self.color,self.rect)