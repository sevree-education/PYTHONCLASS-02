import random

#random() : a float between 0,0 to 1,0
print(random.random())

#randint(a, b) : an integer number between a to b
print(random.randint(1,1234324))

#choice(seq) : pick one element from seq
ai_choice = ["rock", "paper", "scissors"]
print(random.choice(ai_choice))

#sample(seq, k) : pick k unique items from seq
fruits = ["apple", "bannana", "lemons", "watermalon", "oranges"]
print(random.sample(fruits, 2))

#shuffle(seq) : reorder a list
random.shuffle(fruits)
print(fruits)