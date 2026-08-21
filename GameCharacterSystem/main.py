# Parent Class
class GameCharacter:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def show_status(self):
        print(f"{self.name} | Health: {self.health} | Level: {self.level}")


# Child Class: Warrior
class Warrior(GameCharacter):
    def __init__(self, name, health, level, sword_damage):
        super().__init__(name, health, level)
        self.sword_damage = sword_damage

    def sword_attack(self, target):
        print(f"{self.name} attacks {target.name} with a sword!")
        target.take_damage(self.sword_damage)


# Child Class: Archer
class Archer(GameCharacter):
    def __init__(self, name, health, level, arrow_damage):
        super().__init__(name, health, level)
        self.arrow_damage = arrow_damage

    def arrow_attack(self, target):
        print(f"{self.name} shoots an arrow at {target.name}!")
        target.take_damage(self.arrow_damage)


# Child Class: Wizard
class Wizard(GameCharacter):
    def __init__(self, name, health, level, magic_damage):
        super().__init__(name, health, level)
        self.magic_damage = magic_damage

    def magic_attack(self, target):
        print(f"{self.name} casts a magic spell on {target.name}!")
        target.take_damage(self.magic_damage)


# Create Objects
warrior = Warrior("Thor", 100, 5, 20)
archer = Archer("Robin", 80, 4, 15)
wizard = Wizard("Merlin", 70, 6, 25)

# Initial Status
print("=== Initial Status ===")
warrior.show_status()
archer.show_status()
wizard.show_status()

# Character Interactions
print("\n=== Battle Begins ===")
warrior.sword_attack(archer)
archer.arrow_attack(wizard)
wizard.magic_attack(warrior)

# Updated Status
print("\n=== Updated Status ===")
warrior.show_status()
archer.show_status()
wizard.show_status()