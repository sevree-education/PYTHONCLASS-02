#how to declare an object/class
class Character:
    village = "C1234T"
    def __init__(self, Nname, Nage, Nphone):
        self.name = Nname
        self.age = Nage
        self.phone = Nphone

    def IntroduceSelf(self):
        print(f"MY NAME IS {self.name} and i am {self.age} years old")


hero = Character("OUSSAMA", 24, "0550347589")
hero.IntroduceSelf()
hero.age = 40
hero.IntroduceSelf()