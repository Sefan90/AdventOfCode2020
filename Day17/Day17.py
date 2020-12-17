import copy
def checkcells(lista,z,y,x):
    cells = 0 #becouse of i,j,k = 0,0,0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            for k in [-1,0,1]:
                if not (i == 0 and j == 0 and k == 0) and z+i < len(lista) and y+j < len(lista) and x+k < len(lista):
                    if lista[z+i][y+j][x+k] == "#":
                        cells += 1
    #if cells > 0:
    #    print(cells)
    return cells

def Part1():
    f = open("input.txt","r")
    inputlist = [[i for i in r.strip()]for r in f.readlines()]
    cycle = 6
    listsize = len(inputlist)+(cycle-1)*2 
    lista = [[["." for _ in range(listsize)] for _ in range(listsize)] for _ in range(listsize)]
    y = 0
    for i in inputlist:
        x = 0
        for v in i:
            lista[cycle-1][cycle-1+y][cycle-1+x] = v
            x += 1
        y += 1
    templist = copy.deepcopy(lista)
    for c in range(cycle):
        for z in range(len(lista)):
            for y in range(len(lista)):
                #print(lista[z][y])
                for x in range(len(lista)):
                    activecells = checkcells(lista,z,y,x)
                    if lista[z][y][x] == "#" and (activecells < 2 or activecells > 3):
                        templist[z][y][x] = "."
                    elif lista[z][y][x] == "." and activecells == 3:
                        templist[z][y][x] = "#"
            #print(" ")
        lista = copy.deepcopy(templist)
        #print(c)

    summa = 0
    for z in range(len(lista)):
        for y in range(len(lista)):
            for x in range(len(lista)):
                if lista[z][y][x] == "#":
                    summa += 1
    print(summa)

Part1()