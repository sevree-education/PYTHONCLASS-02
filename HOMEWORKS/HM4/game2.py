scr1 = 0
scr2 = 0

for i in range(3):
    print("Please Pick : Rock, Paper, Scissors")
    pl1 = input("PLAYER 01 CHOICE : ").lower()
    pl2 = input("PLAYER 02 CHOICE : ").lower()

    if(pl1=="rock" and pl2=="scissors") or (pl1 =="scissors" and pl2=="paper") or (pl1=="paper" and pl2=="rock"):
        scr1 +=1
    elif(pl2=="rock" and pl1=="scissors") or (pl2 =="scissors" and pl1=="paper") or (pl2=="paper" and pl1=="rock"):
        scr2 +=1
    elif(pl1 == pl2):
        continue
    else:
        print("INVALID INPUT")

if(scr1 > scr2):
    print("PLAYER 01 HAS WON")
elif(scr2 > scr1):
    print("PLAYER 02 HAS WON")
else:
    print("DRAW")