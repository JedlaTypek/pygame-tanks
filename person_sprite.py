import math

import pygame

from bullet import Bullet
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from random import randint

class PersonSprite(pygame.sprite.Sprite):
    '''Třída reprezentující animovanou postavu'''
    def __init__(self, x, y, bullets_group, player_color):
        super().__init__()

        self.width = 196 / 4  # Šířka tanku
        self.height = 196 / 4  # Výška tanku
        self.image_orig = pygame.image.load(f"media/{player_color}.png")  # Načtení obrázku
        self.image_orig = pygame.transform.scale(self.image_orig,
                                                 (int(self.width), int(self.height)))  # Změna velikosti
        self.image_orig.set_colorkey((0, 0, 0))  # Nastavení průhledné barvy (pokud je potřeba)

        #self.image_orig = pygame.Surface((self.width, self.height))
        #self.image_orig.set_colorkey((0, 0, 0))
        #self.image_orig.fill((255 if player_color == 'red' else 0, 0, 255 if player_color == 'blue' else 0))  # Barva podle hráče

        self.direction = randint(0, 355)  # Náhodná počáteční rotace

        # Otočení původního obrázku na náhodný směr
        self.image = pygame.transform.rotate(self.image_orig, self.direction)
        self.rect = self.image.get_rect(center=(x, y))  # Nastavení středu na zadané souřadnice

        self.player_color = player_color
        self.speed = 4  # Rychlost postavy
        self.fire_key_pressed = False  # Příznak, zda byla mezerník předtím stisknut
        self.bullets_group = bullets_group  # Skupina střel
        self.score = 0

    def update(self, keys, walls):
        '''Aktualizace postavy (pohyb + animace)'''
        dx, dy = 0, 0
        steps = 0
        direction = self.direction  # Aktuální směr

        # Pohyb postavy
        if self.player_color == 'red':  # červený hráč
            if keys[pygame.K_LEFT]:
                direction = (direction - self.speed) % 360
            if keys[pygame.K_RIGHT]:
                direction = (direction + self.speed) % 360
            if keys[pygame.K_UP]:
                steps += self.speed
            if keys[pygame.K_DOWN]:
                steps -= self.speed
        if self.player_color == 'blue':  # modrý hráč
            if keys[pygame.K_a]:
                direction = (direction - self.speed) % 360
            if keys[pygame.K_d]:
                direction = (direction + self.speed) % 360
            if keys[pygame.K_w]:
                steps += self.speed
            if keys[pygame.K_s]:
                steps -= self.speed

        # Výpočet posunutí podle úhlu
        dx = steps * math.cos(math.radians(direction))
        dy = steps * math.sin(math.radians(direction))
        new_rect = self.rect.move(dx, dy)

        # Kontrola kolize se zdmi
        if not any(new_rect.colliderect(wall.rect) for wall in walls):
            self.rect = new_rect

        # **Aktualizace úhlu a otočení obrázku**
        self.direction = direction
        self.image = pygame.transform.rotate(self.image_orig, -self.direction)  # Otočení obrázku
        self.rect = self.image.get_rect(center=self.rect.center)  # Oprava středu

        # Střelba při uvolnění mezerníku
        if (keys[pygame.K_SPACE] and self.player_color == 'blue') or (keys[pygame.K_RSHIFT] and self.player_color == 'red'): # Pokud je mezerník stisknut
            self.fire_key_pressed = True # Příznak, že mezerník byl stisknut
        elif self.fire_key_pressed:  # Pokud byla mezerník uvolněna
            self.shoot(self.bullets_group) # Vystřelení střely
            self.fire_key_pressed = False # Příznak, že mezerník byl uvolněn

    def shoot(self, bullets_group):
        '''Vystřelení střely'''
        # Vytvoření střely a přidání do skupiny
        bullet = Bullet(self.rect.centerx + self.width / 1.5 * math.cos(math.radians(self.direction)), self.rect.centery + self.height / 1.5 * math.cos(math.radians(self.direction)), self.direction)
        bullets_group.add(bullet)

