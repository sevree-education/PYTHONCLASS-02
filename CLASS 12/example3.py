#how to declare an object/class
class Character:
    village = "C1234T"
    hp = 100
    level = 0
    points = 0
    def __init__(self, Nname, Nage):
        self.name = Nname
        self.age = Nage

    def IntroduceSelf(self):
        print(f"MY NAME IS {self.name} and i am {self.age} years old")

    def attack(self, other):
        other.hp = other.hp - 10
        self.points = self.points + 1
        if self.points == 10:
            self.level = self.level + 1
            self.points = 0
        print(f"{self.name} has just attacked {other.name}")
        print(f"{other.name} : {other.hp}hp")

    def take_damage(self, damage):
        self.hp = self.hp - damage
        print(f"{self.hp} HP")

#inheritence/extends
class Hero(Character):
    def __init__(self, Nname, Nage):
        super().__init__(Nname, Nage)
        self.bouclier = 50

    def take_damage(self, damage):
        super().take_damage(damage/2)
    
    def super_power(self, other):
        other.hp = other.hp / 2
        other.level = 0
        print("SUPERHERO ATTACK")
        print(f"{self.name} has just attacked {other.name}")
        print(f"{other.name} : {other.hp}hp")

villager = Character("ALPHA", 22)
villan = Character("YOUTAS", 25)
hero = Hero("ZEUS", 127)

