#from collections import defaultdict
from copy import deepcopy

def flipper(floor, key, iswhite):
    white = set()
    blacktiles = 0
    for x in [1,-1]:
        for y in [0.5,-0.5]:
            if str(key[0]+x)+","+str(key[1]+y) in floor.keys() and floor[str(key[0]+x)+","+str(key[1]+y)] == False:
                blacktiles += 1
            else:
                white.add(str(key[0]+x)+","+str(key[1]+y))
    
    if str(key[0])+","+str(key[1]+1) in floor.keys() and floor[str(key[0])+","+str(key[1]+1)] == False:
        blacktiles += 1
    else:
        white.add(str(key[0])+","+str(key[1]+1))
    
    if str(key[0])+","+str(key[1]-1) in floor.keys() and floor[str(key[0])+","+str(key[1]-1)] == False:
        blacktiles += 1
    else:
        white.add(str(key[0])+","+str(key[1]-1))
    
    if iswhite == False:
        if blacktiles == 0 or blacktiles > 2:
            return True, white
        else:
            return False, white
    else:
        if blacktiles == 2:
            return False
        else:
            return True

def part2():
    file = open("input.txt","r").readlines()
    rows = [row.strip() for row in file]
    currentrow = 0
    currentindex = 0
    floor = {} #defaultdict(lambda: True)
    floor["0.0,0.0"] = True

    while currentrow < len(rows):
        currrenttile = [0.0,0.0]
        while currentindex < len(rows[currentrow]):
            if rows[currentrow][currentindex] == "e":
                currrenttile[1] -= 1.0
                currentindex += 1
            elif rows[currentrow][currentindex] == "w":
                currrenttile[1] += 1.0
                currentindex += 1
            elif rows[currentrow][currentindex] == "s" and rows[currentrow][currentindex+1] == "e":
                currrenttile[0] -= 1.0
                currrenttile[1] -= 0.5
                currentindex += 2
            elif rows[currentrow][currentindex] == "s" and rows[currentrow][currentindex+1] == "w":
                currrenttile[0] -= 1.0
                currrenttile[1] += 0.5
                currentindex += 2
            elif rows[currentrow][currentindex] == "n" and rows[currentrow][currentindex+1] == "w":
                currrenttile[0] += 1.0
                currrenttile[1] += 0.5
                currentindex += 2
            elif rows[currentrow][currentindex] == "n" and rows[currentrow][currentindex+1] == "e":
                currrenttile[0] += 1.0
                currrenttile[1] -= 0.5
                currentindex += 2
        if str(currrenttile[0])+","+str(currrenttile[1]) in floor.keys():
            floor[str(currrenttile[0])+","+str(currrenttile[1])] = not floor[str(currrenttile[0])+","+str(currrenttile[1])]
        else:
            floor[str(currrenttile[0])+","+str(currrenttile[1])] = False
        currentrow += 1 
        currentindex = 0

    for _ in range(100):
        white = set()
        newdict = {}
        for k,v in floor.items():
            if v == False:
                key = [float(k.split(",")[0]),float(k.split(",")[1])]
                tmpvalue, tmpset = flipper(floor, key, False)
                newdict[str(key[0])+","+str(key[1])] = tmpvalue
                white |= tmpset
        for w in white:
            key = [float(w.split(",")[0]),float(w.split(",")[1])]
            tmpvalue = flipper(floor, key, True)
            newdict[w] = tmpvalue
        floor = deepcopy(newdict)
    print(sum(1 for v in floor.values() if v == False))


part2()