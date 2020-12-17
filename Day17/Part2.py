import copy
def checkcells(lista,w,z,y,x):
    cells = 0 #becouse of i,j,k = 0,0,0
    for h in [-1,0,1]:
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                for k in [-1,0,1]:
                    if not (h == 0 and i == 0 and j == 0 and k == 0) and w+h < len(lista) and z+i < len(lista) and y+j < len(lista) and x+k < len(lista):
                        if lista[w+h][z+i][y+j][x+k] == "#":
                            cells += 1
    #if cells > 0:
        #print(cells)
    return cells

def Part2():
    f = open("input.txt","r")
    inputlist = [[i for i in r.strip()]for r in f.readlines()]
    cycle = 6
    listsize = len(inputlist)+cycle*2 
    lista = [[[["." for _ in range(listsize)] for _ in range(listsize)] for _ in range(listsize)] for _ in range(listsize)]
    y = 0
    for i in inputlist:
        x = 0
        for v in i:
            lista[cycle][cycle][cycle+y][cycle+x] = v
            x += 1
        y += 1
    templist = copy.deepcopy(lista)
    for c in range(cycle):
        for w in range(len(lista)):
            for z in range(len(lista)):
                for y in range(len(lista)):
                    #print(lista[w][z][y])
                    for x in range(len(lista)):
                        activecells = checkcells(lista,w,z,y,x)
                        if lista[w][z][y][x] == "#" and (activecells < 2 or activecells > 3):
                            templist[w][z][y][x] = "."
                        elif lista[w][z][y][x] == "." and activecells == 3:
                            templist[w][z][y][x] = "#"
                #print(" ")
        lista = copy.deepcopy(templist)
        #print(c)

    summa = 0
    for w in range(len(lista)):
        for z in range(len(lista)):
            for y in range(len(lista)):
                for x in range(len(lista)):
                    if lista[w][z][y][x] == "#":
                        summa += 1
    print(summa)

Part2()