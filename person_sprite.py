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
        self.image_orig = pygame.image.load(f"media/{player_color}.png").convert_alpha()  # Načtení obrázku
        self.image_orig = pygame.transform.scale(self.image_orig, (int(self.width), int(self.height)))

        self.direction = randint(0, 355)  # Náhodná počáteční rotace

        # Otočení původního obrázku na náhodný směr
        self.image = pygame.transform.rotate(self.image_orig, -self.direction)
        self.rect = self.image.get_rect(center=(x, y))

        # Vytvoření masky pro pixel-perfect kolize
        self.mask = pygame.mask.from_surface(self.image)

        self.player_color = player_color
        self.speed = 4
        self.fire_key_pressed = False
        self.bullets_group = bullets_group
        self.score = 0

    def update(self, keys, walls):
        '''Aktualizace postavy (pohyb + animace)'''
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
        new_center = (self.rect.centerx + dx, self.rect.centery + dy)

        # **Kolize s překážkami pomocí mask**
        new_image = pygame.transform.rotate(self.image_orig, -self.direction)
        new_mask = pygame.mask.from_surface(new_image)
        new_rect = self.image.get_rect(center=new_center)

        collision_detected = any(
            wall.mask.overlap(new_mask, (new_rect.x - wall.rect.x, new_rect.y - wall.rect.y))
            for wall in walls
        )

        if not collision_detected:
            self.rect.center = new_center

            # **Aktualizace úhlu a otočení obrázku**
            self.direction = direction
            self.image = new_image
            self.rect = new_rect

        # Aktualizace masky po otočení
        self.mask = pygame.mask.from_surface(self.image)

        # Střelba při uvolnění mezerníku
        if (keys[pygame.K_SPACE] and self.player_color == 'blue') or (keys[pygame.K_RSHIFT] and self.player_color == 'red'):
            self.fire_key_pressed = True
        elif self.fire_key_pressed:
            self.shoot(self.bullets_group)
            self.fire_key_pressed = False

    def shoot(self, bullets_group):
        '''Vystřelení střely'''
        bullet = Bullet(
            self.rect.centerx + self.width / 1.5 * math.cos(math.radians(self.direction)),
            self.rect.centery + self.height / 1.5 * math.sin(math.radians(self.direction)),  # Oprava směru střely
            self.direction
        )
        bullets_group.add(bullet)
