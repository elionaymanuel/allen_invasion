import pygame

class Ship():
    def __init__(self,screen,configs):
        """inicializa a nave colocando-a em sua posiçao inicial"""
        self.screen = screen
        self.configs = configs
        #carregar a imagem da nave e obter seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #inicia cada nova espaçonave na parte inferior central da tela
    
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float (self.rect.centerx)
        #flags de movimento
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        

    def update(self):
        """atualiza a posição da nave de acordo com as flags de movimento self.moving_"""
        if self.moving_right and self.rect.right<self.screen_rect.right and not self.moving_left:
            self.center += self.configs.ship_speed_factor
        elif self.moving_left and self.rect.left>0 and not self.moving_right:
            self.center -= self.configs.ship_speed_factor

        self.rect.centerx = self.center


    def blitme(self):
        """Desenha a nave em sua posição atual"""
        self.screen.blit(self.image, self.rect)