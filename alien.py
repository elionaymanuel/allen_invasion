import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ classe que representa um unico alienigena da frota"""
    def __init__(self,configs, screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.configs = configs
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #inicia cada novo alien prox a parte superior esquerda
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #armazena a posição exata do alien
        self.x = float(self.rect.x)

    def update(self):
        "move o alien pra direita"
        self.x += self.configs.alien_speed_factor
        self.rect.x = self.x

    def blitme(self):
        """desenha a nave alien em sua posicao atual"""
        self.screen.blit(self.image, self.rect)
