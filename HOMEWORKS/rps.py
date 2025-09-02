print("Please Pick : Rock, Paper, Scissors")
pl1 = input("PLAYER 01 CHOICE : ").lower()
pl2 = input("PLAYER 02 CHOICE : ").lower()

if(pl1=="rock" and pl2=="scissors") or (pl1 =="scissors" and pl2=="paper") or (pl1=="paper" and pl2=="rock"):
    print("PLAYER 01 HAS WON")
elif(pl2=="rock" and pl1=="scissors") or (pl2 =="scissors" and pl1=="paper") or (pl2=="paper" and pl1=="rock"):
    print("PLAYER 02 HAS WON")
elif(pl1 == pl2):
    print("DRAW")
else:
    print("INVALID INPUT")