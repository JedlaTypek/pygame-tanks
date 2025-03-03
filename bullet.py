import pygame
import math
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Bullet(pygame.sprite.Sprite):
    '''Třída představující střelu'''
    def __init__(self, x, y, direction, player, initial_energy=100):
        super().__init__()
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)  # Povolení průhlednosti
        self.image.fill((255, 0, 0))  # Červená barva střely
        self.rect = self.image.get_rect(center=(x, y))  # Střela na zadané pozici
        self.speed = 10  # Rychlost střely
        self.direction = direction  # Směr střely
        self.dx, self.dy = self.get_velocity(direction)  # Rychlost střely ve směru
        self.energy = initial_energy  # Počáteční energie střely
        self.firing_player = player

        # Vytvoření masky pro pixel-perfect kolize
        self.mask = pygame.mask.from_surface(self.image)

    def get_velocity(self, direction):
        '''Vrací směr pohybu střely'''
        return self.speed * math.cos(math.radians(direction)), self.speed * math.sin(math.radians(direction))

    def update(self, walls, targets):
        '''Aktualizace pozice střely'''

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                # Horní odraz
                if self.rect.bottom > wall.rect.top and self.rect.top < wall.rect.top and self.rect.centerx >= wall.rect.left and self.rect.centerx <= wall.rect.right:
                    self.direction = 360 - self.direction
                    self.dx, self.dy = self.get_velocity(self.direction)
                    self.rect.bottom = wall.rect.top  # Posunutí střely nad zeď

                # spodní odraz
                elif self.rect.top < wall.rect.bottom and self.rect.bottom > wall.rect.bottom and self.rect.centerx >= wall.rect.left and self.rect.centerx <= wall.rect.right:
                    self.direction = 360 - self.direction
                    self.dx, self.dy = self.get_velocity(self.direction)
                    self.rect.top = wall.rect.bottom  # Posunutí střely pod zeď

                # levý odraz
                elif self.rect.right > wall.rect.left and self.rect.left < wall.rect.left and self.rect.centery >= wall.rect.top and self.rect.centery <= wall.rect.bottom:
                    self.direction = 180 - self.direction
                    self.dx, self.dy = self.get_velocity(self.direction)
                    self.rect.right = wall.rect.left  # Posunutí střely vlevo od zdi

                # pravý odraz
                elif self.rect.left < wall.rect.right and self.rect.right > wall.rect.right and self.rect.centery >= wall.rect.top and self.rect.centery <= wall.rect.bottom:
                    self.direction = 180 - self.direction
                    self.dx, self.dy = self.get_velocity(self.direction)
                    self.rect.left = wall.rect.right  # Posunutí střely vpravo od zdi

            # Ztráta energie při nárazu
                self.energy -= 10
                if self.energy <= 0:
                    self.kill()

        # Pohyb střely
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Snížení energie
        self.energy -= 1
        if self.energy <= 0:
            self.kill()  # Střela zanikne, pokud nemá energii

        # Pokud střela opustí obrazovku, zničí se
        if not (0 <= self.rect.x <= SCREEN_WIDTH and 0 <= self.rect.y <= SCREEN_HEIGHT):
            self.kill()
