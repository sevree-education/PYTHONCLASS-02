class Character:
    def __init__(self, name):
        self.name = name

    def attack(self, other):
        print(f"{self.name} is attacking {other.name}")

class hero(Character):
    def attack(self, other):
        print(f"SUPER ATTACK BY {self.name} ON {other.name}")

villager = Character("JACK")
aria = hero("ARIA")

villager.attack(aria)
aria.attack(villager)