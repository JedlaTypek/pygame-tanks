# Pygame Demo   
## Ukázka možností využití knihovny Pygame

Tento projekt představuje ukázkovou aplikaci vytvořenou pomocí frameworku [Pygame](https://www.pygame.org/). Hra obsahuje interaktivní postavy, střelbu a manipulaci s herními zdmi.

## Funkce

- **Pohyb postav:** Aktivní postava se ovládá pomocí šipek.
- **Přepínání postav:** Klávesa `Tab` umožňuje přepínat mezi dostupnými postavami.
- **Střelba:** Střely lze vystřelit stisknutím a následným uvolněním mezerníku.
- **Manipulace se zdmi:**
  - Přesouvání zdí: podržte `Shift` a přetáhněte zeď myší.
  - Změna velikosti: podržte `Ctrl` a přetáhněte rohy zdi.
  - Vytváření zdí: kliknutím a tažením levého tlačítka myši vytvoříte novou zeď.
  - Odstranění zdí: vyberte zeď a stiskněte klávesu `Delete`.

## Požadavky

- Python 3.7 nebo novější
- Pygame knihovna

## Instalace

1. Naklonujte tento repozitář:

   ```bash
   git clone https://github.com/uzivatel/pygame-demo.git
   cd pygame-demo
   ```

2. Nainstalujte požadované knihovny:

   ```bash
   pip install pygame
   ```

3. Spusťte aplikaci:

   ```bash
   python main.py
   ```

## Struktura projektu

- `main.py`: Hlavní třída aplikace a herní smyčka.
- `bullet.py`: Třída pro správu střel.
- `custom_surface.py`: Třída zajišťující vykreslení vlastního pozadí.
- `person_sprite.py`: Třída postavy s animací a střelbou.
- `wall.py`: Třídy pro manipulaci se zdmi a jejich správu.
- `settings.py`: Konfigurační soubor s konstantami, jako je velikost obrazovky a počet snímků za sekundu.

## Média

Hra využívá následující mediální soubory:

- `media/sprite-person.png`: Sprite sheet postav.
- `media/grass.jpg`: Textura pozadí.
- `media/surface-01.jpg`: Textura pro zdi.

Ujistěte se, že jsou všechny mediální soubory dostupné ve složce `media/`.

## Klávesové zkratky

| Akce                  | Klávesa            |
|-----------------------|--------------------|
| Pohyb                 | Šipky              |
| Přepínání postav      | Tab                |
| Střelba               | Mezerník           |
| Přesun zdi            | Shift + myš        |
| Změna velikosti zdi   | Ctrl + myš         |
| Vytvoření nové zdi    | Levé tlačítko myši |
| Odstranění zdi        | Delete             |
| Ukončení aplikace     | Esc                |

## Náhled

![Screenshot hry](media/screenshot.png) <!-- Nahraďte skutečnou cestou k náhledu -->

## Licence

Tento projekt je licencován pod licencí MIT. Podrobnosti naleznete v souboru `LICENSE`.
