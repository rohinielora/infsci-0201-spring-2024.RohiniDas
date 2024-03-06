#oop_project.py

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = None

    def equip(self, weapon):
        self.weapon = weapon

class Hero(Character):
    def __init__(self, name, health):
        super().__init__(name, health)

    def attack(self):
        if self.weapon:
            print(f"{self.name} attacks with {self.weapon.name}.")
            self.health += self.weapon.damage  # If the weapon has healing powers, health increases.

class Enemy(Character):
    def __init__(self, name, health, weapon=None):
        super().__init__(name, health)
        if weapon:
            self.equip(weapon)

    def attack(self):
        if self.weapon:
            print(f"{self.name} attacks with {self.weapon.name}.")
            self.health += self.weapon.damage

class Weapon:
    def __init__(self, name, weapon_type, damage, value):
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

empty_handed = Weapon(name="Empty handed", weapon_type="dummy", damage=0, value=0)
healing_staff = Weapon(name="Healing Staff", weapon_type="magic", damage=-3, value=0)

protagonist = Hero(name="Hero", health=100)
protagonist.health = 10  # here i am adjusting health
protagonist.equip(empty_handed)
ally = Enemy(name="Friendly Enemy", health=100, weapon=healing_staff)

# Example game loop 
print(f"Initial health - {protagonist.name}: {protagonist.health}, {ally.name}: {ally.health}")
for turn in range(3):  
    protagonist.attack()
    ally.attack()
    print(f"Turn {turn + 1} - {protagonist.name}: {protagonist.health}, {ally.name}: {ally.health}")
