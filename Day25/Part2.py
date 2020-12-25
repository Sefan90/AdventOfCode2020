from collections import defaultdict

def part2():
    file = open("input.txt","r").readlines()
    rows = [row.strip() for row in file]
    currentrow = 0
    currentindex = 0
    floor = defaultdict(lambda: True)
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
        floor[str(currrenttile[0])+","+str(currrenttile[1])] = not floor[str(currrenttile[0])+","+str(currrenttile[1])]
        currentrow += 1 
        currentindex = 0
    print(sum(1 for v in floor.values() if v == False))

    for i in range(100):
        for k,v in floor.values():
            
part2()