import collections
import copy
file = open("input.txt","r").readlines()
player1 = []
player2 = []
nextplayer = False

def rec(deck1, deck2):
    #print("")
    #print(deck1)
    #print(deck2)
    player1hands = []
    player2hands = []
    while len(deck1) != 0 and len(deck2) != 0:
        if deck1 in player1hands and deck2 in player2hands:
            return "p1"
        player1hands.append(copy.deepcopy(deck1))
        player2hands.append(copy.deepcopy(deck2))
        item1 = deck1.pop(0)
        item2 = deck2.pop(0)
        if len(deck1) >= item1 and len(deck2) >= item2:
            tmp = rec(copy.deepcopy(deck1[:item1]),copy.deepcopy(deck2[:item2]))
            #print(tmp)
            if tmp == "p1":
                deck1.append(item1)
                deck1.append(item2)
            else:
                deck2.append(item2)
                deck2.append(item1)
        elif item1 < item2:
            deck2.append(item2)
            deck2.append(item1)
        else:
            deck1.append(item1)
            deck1.append(item2)
    if len(deck1) == 0:
        return "p2"
    elif len(deck2) == 0:
        return "p1"

for line in file:
    if line == "\n":
        nextplayer = True
    elif nextplayer == False and "Player" not in line:
        player1.append(int(line.strip()))
    elif "Player" not in line:
        player2.append(int(line.strip()))

tmp = rec(player1,player2)
print(tmp)
print(player1)
print(player2)
if tmp == "p2":
    newlist = player2
else:
    newlist = player1

summa = 0
for i in range(len(newlist)):
    summa += newlist[i]*(len(newlist)-i)

print(summa)
