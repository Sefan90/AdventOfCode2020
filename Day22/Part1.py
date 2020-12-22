import collections
file = open("input.txt","r").readlines()
player1 = []
player2 = []
nextplayer = False

for line in file:
    if line == "\n":
        nextplayer = True
    elif nextplayer == False and "Player" not in line:
        player1.append(int(line.strip()))
    elif "Player" not in line:
        player2.append(int(line.strip()))

while len(player1) != 0 and len(player2) != 0:
    item1 = player1.pop(0)
    item2 = player2.pop(0)
    if item1 < item2:
        player2.append(item2)
        player2.append(item1)
    else:
        player1.append(item1)
        player1.append(item2)

if len(player1) == 0:
    newlist = player2
else:
    newlist = player1

summa = 0
for i in range(len(newlist)):
    summa += newlist[i]*(len(newlist)-i)
    print(newlist[i]*(len(newlist)-i))

print(summa)