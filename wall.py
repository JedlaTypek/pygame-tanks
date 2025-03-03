import pygame


class Wall:
    '''Třída reprezentující zeď'''
    def __init__(self, x, y, width, height, image_path="media/iron.jpg"):
        '''Konstruktor'''
        self.rect = pygame.Rect(x, y, width, height)  # Vytvoření obdélníku
        self.active = False  # Aktivní zeď
        self.texture = pygame.image.load(image_path).convert_alpha()  # Načtení textury
        self.update_mask()  # Vytvoření masky pro přesnou detekci kolizí

    def update_mask(self):
        '''Aktualizace masky podle velikosti zdi'''
        scaled_texture = pygame.transform.scale(self.texture, (self.rect.width, self.rect.height))
        self.mask = pygame.mask.from_surface(scaled_texture)

    def move(self, dx, dy):
        '''Pohyb zdi'''
        self.rect.move_ip(dx, dy)  # Pohyb obdélníku
        self.update_mask()  # Aktualizace masky po pohybu

    def set_active(self, is_active):
        '''Nastavení aktivity zdi'''
        self.active = is_active

    def draw(self, target_surface):
        '''Vykreslení zdi'''
        scaled_texture = pygame.transform.scale(self.texture, (self.rect.width, self.rect.height))
        target_surface.blit(scaled_texture, self.rect.topleft)

        # Pokud je zeď aktivní, vykreslíme obrys
        if self.active:
            pygame.draw.rect(target_surface, (0, 0, 255), self.rect, 3)


class WallManager:
    '''Třída pro správu zdí'''
    def __init__(self):
        self.walls = []  # Seznam zdí
        self.active_wall = None  # Aktivní zeď
        self.dragging = False  # Přetahování zdi
        self.start_pos = None  # Počáteční pozice
        self.mode = None  # 'move' nebo 'resize'

    def start_dragging(self, position, keys):
        '''Začátek přetahování zdi'''
        for wall in self.walls:
            if wall.rect.collidepoint(position):
                self.active_wall = wall
                self.active_wall.set_active(True)
                self.start_pos = position
                self.dragging = True

                # Nastavení módu manipulace
                if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                    self.mode = 'move'
                elif keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
                    self.mode = 'resize'
                else:
                    self.mode = None
                return

        # Pokud neexistuje aktivní zeď, vytvoří novou
        self.active_wall = Wall(position[0], position[1], 0, 0)
        self.walls.append(self.active_wall)
        self.active_wall.set_active(True)
        self.start_pos = position
        self.dragging = True
        self.mode = None  # Nové zdi nejsou přesouvány ani měněny velikost

    def stop_dragging(self, position):
        '''Konec přetahování zdi'''
        self.dragging = False
        self.start_pos = None
        self.mode = None

        # Odstranění zdi s nulovou velikostí
        if self.active_wall and (self.active_wall.rect.width <= 0 or self.active_wall.rect.height <= 0):
            self.walls.remove(self.active_wall)
            self.active_wall = None

    def update_dragging(self, position):
        '''Aktualizace přetahování zdi'''
        if self.dragging and self.active_wall:
            if self.mode == 'move':
                # Přesouvání zdi
                dx = position[0] - self.start_pos[0]
                dy = position[1] - self.start_pos[1]
                self.active_wall.move(dx, dy)
                self.start_pos = position
            elif self.mode == 'resize':
                # Změna velikosti zdi
                x1, y1 = self.start_pos
                x2, y2 = position

                # Úprava rozměrů na základě aktuální pozice
                self.active_wall.rect.width = max(1, abs(x2 - self.active_wall.rect.x))
                self.active_wall.rect.height = max(1, abs(y2 - self.active_wall.rect.y))
            else:
                # Tvorba nové zdi
                x1, y1 = self.start_pos
                x2, y2 = position

                # Určení správných souřadnic a rozměrů
                self.active_wall.rect.x = min(x1, x2)
                self.active_wall.rect.y = min(y1, y2)
                self.active_wall.rect.width = abs(x2 - x1)
                self.active_wall.rect.height = abs(y2 - y1)

            # Aktualizace masky po změně velikosti nebo přesunutí
            self.active_wall.update_mask()

    def delete_active_wall(self):
        '''Odstranění aktivní zdi'''
        if self.active_wall in self.walls:
            self.walls.remove(self.active_wall)
            self.active_wall = None

    def get_walls(self):
        '''Vrácení seznamu zdí'''
        return self.walls

    def draw(self, target_surface):
        '''Vykreslení zdí'''
        for wall in self.walls:
            # Deaktivace zdí, které nejsou aktivní
            if wall != self.active_wall:
                wall.active = False
            wall.draw(target_surface)
