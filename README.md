# Simple tank game in Python

## Funkce

- **Pohyb postav:** Tanky se ovládají pomocí šipek nebo klávas WSAD.
- **Střelba:** Střely lze vystřelit stisknutím a následným uvolněním mezerníku nebo pravého shiftu (podle hráče).
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
   git clone https://github.com/JedlaTypek/pygame-tanks
   cd pygame-tanks
   ```

2. Nainstalujte požadované knihovny:

   ```bash
   pip install -r requierements.txt
   ```

3. Spusťte aplikaci:

   ```bash
   python main.py
   ```

## Klávesové zkratky

| Akce                  | Červený hráč       | Modrý hráč |
|-----------------------|--------------------|------------|
| Pohyb                 | Šipky              | WSAD       |
| Střelba               | Pravý shift        | Mezerník   |

| Další akce          | Klávesa            |
|---------------------|--------------------|
| Přesun zdi          | Shift + myš        | 
| Změna velikosti zdi | Ctrl + myš         |
| Vytvoření nové zdi  | Levé tlačítko myši |
| Odstranění zdi      | Delete             |
| Ukončení aplikace   | Esc                |

## Náhled

![Screenshot hry](media/screenshot.png) <!-- Nahraďte skutečnou cestou k náhledu -->
