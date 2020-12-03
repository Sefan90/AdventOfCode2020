def Part1():
    pos = 0
    poschange = 3
    counter = 0
    f = open("input.txt","r")
    lines = f.readlines() 
    for i in lines:
        if i[pos] == "#":
            counter = counter + 1
        pos = (pos + poschange)%(len(i)-1)
    print(counter)

def checker(poschangeY, poschangeX):
    pos = 0
    poschangeX = poschangeX - 1 #Becouse you will always skip 1 row.
    counter = 0
    skiprows = 0
    f = open("input.txt","r")
    lines = f.readlines() 
    for i in lines:
        if skiprows > 0:
            skiprows = skiprows - 1
            continue 
        if i[pos] == "#":
            counter = counter + 1
        pos = (pos + poschangeY)%(len(i)-1)
        skiprows = poschangeX
    return counter

def Part2():
    a = checker(1,1)
    b = checker(3,1)
    c = checker(5,1)
    d = checker(7,1)
    e = checker(1,2)
    print(a*b*c*d*e)
    
Part2()