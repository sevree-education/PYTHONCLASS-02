class player():
    def __init__(self, name, age, level):
        self.name = name 
        self.age = age
        self.level = level
    
    def __str__(self):
        return f" NAME : {self.name}, AGE : {self.age}, LEVEL : {self.level}"
    
    def __eq__(self, other):
        return isinstance(other, player) and self.level == other.level
    
    def __add__(self, other):
        return [self, other]

player1 = player("NAME1", 25, 15)
player2 = player("NAME1", 25, 315)

if(player1 == player2):
    print("EQUALE")

players = player1 + player2

print(players)
