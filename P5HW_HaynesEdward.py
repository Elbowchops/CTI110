# Edward Haynes
# 4/8/2025
# P5HW
# Creating a game using pyhton



import random
import time
import sys

# Ship classes
SHIP_CLASSES = {
    "1": {
        "name": "The Scout",
        "weapons": {"Torpedo": 25}
    },
    "2": {
        "name": "Battle Cruiser",
        "weapons": {"Torpedo": 25, "Artillery Cannons (x2)": 50}
    },
    "3": {
        "name": "The Destroyer",
        "weapons": {
            "Torpedo": 25,
            "Artillery Cannons (x2)": 50,
            "Tomahawk Missile": 75
        }
    }
}

PLAYER_GRID_ZONES = ["A", "B", "C", "D", "E"]
PLAYER_GRID_SECTORS = list(range(1, 6))
ENEMY_GRID_ZONES = ["A", "B", "C"]
ENEMY_GRID_SECTORS = list(range(1, 5))
ENEMY_NAMES = ["Phantom", "Oblivion", "Ravager", "Warlord", "Nemesis", "Shadow"]

class Ship:
    def __init__(self, name, ship_class, grid_zone, grid_sector):
        self.name = name
        self.ship_class = ship_class
        self.health = 200
        self.weapons = SHIP_CLASSES[ship_class]["weapons"]
        self.position = f"{grid_zone.upper()}{grid_sector}"

    def display_info(self):
        weapons_str = ", ".join([f"{w} (Power {p})" for w, p in self.weapons.items()])
        return f"{self.name} | Health: {self.health} | Weapons: {weapons_str}"

def dramatic_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def show_burning_ship():
    print(r"""
              _.-^^---....,,--
          _--                  --_
         <                        >)
         |                         |
          \._                   _./
             ```--. . , ; .--'''
                   | |   |
                .-=||  | |=-.
                `-=#$%&%$#=-'
                   | ;  :|
          _____.,-#%&$@%#&#~,._____
    """)

def setup_player():
    print("Welcome to Battle Grid!!")
    military_name = input("Enter the name of your Military: ")
    print(f"\nWelcome, Commander of {military_name}!\n")

    while True:
        try:
            num_ships = int(input("How many ships do you want to use? (1–3): "))
            if 1 <= num_ships <= 3:
                break
            print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.")

    ships = []
    for i in range(1, num_ships + 1):
        print(f"\nSelect ship {i}:")
        for key, value in SHIP_CLASSES.items():
            weapons = ", ".join([f"{w} (Power {p})" for w, p in value["weapons"].items()])
            print(f"{key}. {value['name']} - Weapons: {weapons}")
        while True:
            ship_class = input("Choose Ship class: ")
            print()
            if ship_class in SHIP_CLASSES:
                break
            print("Invalid class. Please enter 1, 2, or 3.")

        ship_name = input("Name your ship: ")

        while True:
            grid_zone = input("Choose grid zone (A-E): ").upper()
            if grid_zone in PLAYER_GRID_ZONES:
                break
            print("Invalid grid zone.")

        while True:
            try:
                grid_sector = int(input("Choose sector (1-5): "))
                if grid_sector in PLAYER_GRID_SECTORS:
                    break
                print("Invalid sector.")
            except ValueError:
                print("Please enter a valid number.")

        new_ship = Ship(ship_name, ship_class, grid_zone, grid_sector)
        ships.append(new_ship)

    return military_name, ships

def setup_enemy():
    num_enemy_ships = random.randint(1, 3)
    print(f"\n⚠️ {num_enemy_ships} ship(s) approaching...\n")
    time.sleep(3)
    enemy_ships = []

    for i in range(num_enemy_ships):
        ship_class = random.choice(list(SHIP_CLASSES.keys()))
        ship_name = f"{random.choice(ENEMY_NAMES)}-{i+1}"
        grid_zone = random.choice(ENEMY_GRID_ZONES)
        grid_sector = random.choice(ENEMY_GRID_SECTORS)

        new_enemy = Ship(ship_name, ship_class, grid_zone, grid_sector)
        enemy_ships.append(new_enemy)

    return enemy_ships

def player_turn(player_ships, enemy_ships):
    print("\n=== Player Turn ===")
    print("\nYour fleet status:")
    for i, ship in enumerate(player_ships, 1):
        print(f"{i}. {ship.display_info()} (Position: {ship.position})")
    while True:
        try:
            choice = int(input("\nSelect a ship to attack with (1–{}): ".format(len(player_ships))))
            if 1 <= choice <= len(player_ships):
                selected_ship = player_ships[choice - 1]
                break
            print("Invalid selection.")
        except ValueError:
            print("Enter a valid number.")
    weapons = list(selected_ship.weapons.items())
    print(f"\nAvailable weapons for {selected_ship.name}:")
    for i, (weapon, power) in enumerate(weapons, 1):
        print(f"{i}. {weapon} (Power {power})")
    while True:
        try:
            weapon_choice = int(input("Select a weapon: "))
            if 1 <= weapon_choice <= len(weapons):
                weapon_name, weapon_power = weapons[weapon_choice - 1]
                break
            print("Invalid selection.")
        except ValueError:
            print("Enter a valid number.")

    while True:
        target = input("Enter enemy grid zone (A–C): ").upper()
        if target in ENEMY_GRID_ZONES:
            break
        print("Invalid grid zone.")

    while True:
        try:
            sector = int(input("Enter enemy sector (1–4): "))
            if sector in ENEMY_GRID_SECTORS:
                break
            print("Invalid sector.")
        except ValueError:
            print("Enter a valid number.")

    target_position = f"{target}{sector}"

    for enemy in enemy_ships:
        if enemy.position == target_position:
            enemy.health -= weapon_power
            print(f"\n🔥 Direct hit on {enemy.name}! {weapon_name} did {weapon_power} damage.")
            if enemy.health > 0:
                print(f"{enemy.name} now at {enemy.health} health.")
            if enemy.health <= 0:
                print(f"💥 {enemy.name} has been destroyed!")
                enemy_ships.remove(enemy)
            return True

    print("\n💨 Miss! No enemy at that position.")
    return False

def enemy_turn(enemy_ships, player_ships):
    print("\n=== Enemy Turn ===")
    time.sleep(3)
    attacker = random.choice(enemy_ships)
    weapon_name, weapon_power = random.choice(list(attacker.weapons.items()))
    target = random.choice(player_ships)

    print(f"{attacker.name} fires {weapon_name} at {target.name}!")
    time.sleep(2)

    if random.random() > 0.2:  # 80% chance to hit
        target.health -= weapon_power
        print(f"💥{target.name} takes {weapon_power} damage!")
        time.sleep(2)
        if target.health > 0:
            print(f"{target.name} now at {target.health} health.")
        if target.health <= 0:
            print(f"💥 {target.name} has been destroyed!")
            player_ships.remove(target)
        return True
    else:
        print("💨 Enemy missed!")
        return False

def battle_loop(player_ships, enemy_ships):
    player_turn_active = True

    while player_ships and enemy_ships:
        if player_turn_active:
            hit = player_turn(player_ships, enemy_ships)
            player_turn_active = hit
        else:
            hit = enemy_turn(enemy_ships, player_ships)
            player_turn_active = not hit

    if not enemy_ships:
        print("\nEnemy ships destroyed!")
        dramatic_text("🏆Victory is yours!🏆", delay=0.2)
    elif not player_ships:
        show_burning_ship()
        dramatic_text("☠️ Your fleet is destroyed...Mission Failed ☠️", delay=0.2)

if __name__ == "__main__":
    while True:
        military_name, ships = setup_player()
        print("\nYour fleet is ready for battle, Commander. Happy hunting!!")
        for ship in ships:
            print(f"{ship.name} | Class: {SHIP_CLASSES[ship.ship_class]['name']} | Health: {ship.health}")
            time.sleep(1)

        print("\nScanning for enemy ships....")
        time.sleep(3)

        enemy_ships = setup_enemy()
        print("\n" + "="*40)
        print("BATTLE STATIONS!! Enemy fleet detected!!")
        print("="*40)
        for ship in enemy_ships:
            print(ship.display_info())

        input("\nPress Enter to engage the enemy...")

        battle_loop(ships, enemy_ships)

        replay = input("\nPlay again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing Battle Grid, Commander!")
            break

        



