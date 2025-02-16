import pygame


class Enemy(pygame.sprite.Sprite):
    '''Třída reprezentující nepřátelský objekt'''
    def __init__(self, x, y, size=30):
        super().__init__()
        self.image = pygame.Surface((size, size))  # Nepřítel jako čtverec
        self.image.fill((255, 0, 0))  # Červená barva
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        '''Aktualizace nepřítele (zatím prázdné, lze přidat pohyb nebo AI)'''
        pass