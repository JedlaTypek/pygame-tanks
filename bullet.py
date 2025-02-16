import pygame
import math
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Bullet(pygame.sprite.Sprite):
    '''Třída představující střelu'''
    def __init__(self, x, y, direction, initial_energy=100):
        super().__init__()
        self.image = pygame.Surface((10, 10))  # Střela jako malá kulička
        self.image.fill((255, 0, 0))  # Červená barva
        self.rect = self.image.get_rect(center=(x, y)) # Střela na zadané pozici
        self.speed = 10 # Rychlost střely
        self.direction = direction # Směr střely
        self.dx, self.dy = self.get_velocity(direction) # Rychlost střely ve směru
        self.energy = initial_energy  # Počáteční energie střely


    def get_velocity(self, direction):
        '''Vrací směr pohybu střely'''
        return self.speed * math.cos(math.radians(direction)), self.speed * math.sin(math.radians(direction))
    def update(self, walls, targets):
        '''Aktualizace pozice střely'''
        # Pohyb střely
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Snížení energie
        self.energy -= 1
        if self.energy <= 0:
            self.kill()  # Střela zanikne, pokud nemá energii

        # Kontrola kolize se zdmi
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                wall.get_side(self.rect)
                if self.dx != 0:  # Odraz vodorovně
                    self.dx = -self.dx
                if self.dy != 0:  # Odraz svisle
                    self.dy = -self.dy
                # Ztráta energie při nárazu
                self.energy -= 10
                if self.energy <= 0:
                    self.kill()

        # Pokud střela opustí obrazovku, zničí se
        if not (0 <= self.rect.x <= SCREEN_WIDTH and 0 <= self.rect.y <= SCREEN_HEIGHT):
            self.kill()
