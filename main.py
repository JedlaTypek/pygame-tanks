import random
import pygame
from custom_surface import CustomSurface
from person_sprite import PersonSprite
from wall import WallManager
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS


class App:
    '''Hlavní třída aplikace'''
    def __init__(self):
        '''Konstruktor - Inicializace hry'''
        pygame.init()   # Inicializace Pygame
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Vytvoření okna
        pygame.display.set_caption("Tanks")  # Název okna
        self.clock = pygame.time.Clock()  # Vytvoření hodin
        self.running = True  # Hra běží

        # Komponenty
        self.custom_surface = CustomSurface(SCREEN_WIDTH, SCREEN_HEIGHT, (0, 0))
        self.walls = WallManager()
        self.person_sprites = pygame.sprite.Group()  # Skupina postav
        self.bullets = pygame.sprite.Group()  # Skupina střel
        self.person_sprites_list = []  # Seznam všech postav pro přepínání
        self.add_person_sprites()  # Přidání postav

    def add_person_sprites(self):
        '''Přidání postav do hry'''
        self.person_sprites_list.append(PersonSprite(100, 100, self.bullets, "red"))
        self.person_sprites_list.append(PersonSprite(400, 300, self.bullets, "blue"))
        for person in self.person_sprites_list:
            self.person_sprites.add(person)

    def run(self):
        '''Hlavní smyčka hry'''
        while self.running:
            self.handle_events()  # Zpracování událostí
            self.update()  # Aktualizace stavu
            self.draw()  # Vykreslení prvků
            self.clock.tick(FPS)  # Počet snímků za sekundu
        pygame.quit()  # Ukončení Pygame

    def handle_events(self):
        '''Zpracování všech událostí v hlavní smyčce hry'''
        for event in pygame.event.get():  # Projít všechny události ve frontě
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False  # Ukončení hry


            # Vytvoření nebo manipulace se zdmi
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Levé tlačítko myši
                    keys = pygame.key.get_pressed()
                    self.walls.start_dragging(event.pos, keys)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.walls.stop_dragging(event.pos)

            if event.type == pygame.MOUSEMOTION:
                self.walls.update_dragging(event.pos)

            # Odstranění zdi
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE:
                self.walls.delete_active_wall()

    def update(self):
        '''Aktualizace herního stavu'''
        keys = pygame.key.get_pressed()
        self.person_sprites.update(keys, self.walls.get_walls())
        self.bullets.update(self.walls.get_walls(), self.person_sprites)

        # Kontrola kolize střel s hráči
        for bullet in self.bullets:
            hit_players = pygame.sprite.spritecollide(bullet, self.person_sprites, True, pygame.sprite.collide_mask)
            for player in hit_players:
                bullet.kill()
                player.kill()
                if player != bullet.firing_player:
                    bullet.firing_player.score += 1

    def draw(self):
        '''Vykreslení herních prvků'''
        self.screen.fill((255, 255, 0))  # Vyplnění obrazovky žlutou barvou
        self.custom_surface.draw(self.screen)  # Vykreslení vlastního Surface
        self.walls.draw(self.screen)  # Vykreslení zdí
        self.person_sprites.draw(self.screen)  # Vykreslení všech postav
        self.bullets.draw(self.screen)  # Vykreslení střel
        pygame.display.flip()  # Zobrazení vykreslených prvků


# Spuštění aplikace
if __name__ == "__main__":
    app = App()
    app.run()
