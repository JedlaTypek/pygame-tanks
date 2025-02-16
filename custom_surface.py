import pygame


class CustomSurface:
    '''Vlastní Surface s obrázkem'''
    def __init__(self, width, height, position):
        '''Konstruktor'''
        self.surface = pygame.Surface((width, height))  # Vytvoření vlastního Surface
        self.surface.fill((0, 255, 0))  # Vyplnění zelenou barvou
        self.position = position    # Pozice vlastního Surface

        # Načtení obrázku na Surface
        self.image = pygame.image.load("media/grass.jpg")  # Načtení obrázku pozadí
        self.image = pygame.transform.scale(self.image, (width, height))    # Změna velikosti obrázku

    def draw(self, target_surface):
        '''Vykreslení vlastního Surface na cílový Surface'''
        # Kreslení obrázku na vlastní Surface
        self.surface.blit(self.image, (0, 0))
        # Vykreslení vlastního Surface na cílový Surface
        target_surface.blit(self.surface, self.position)
