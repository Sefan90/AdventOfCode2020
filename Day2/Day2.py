def Part1():
    rowcounter = 0
    f = open("input.txt","r")
    lines = f.readlines() 
    for i in lines:
        words = i.split()
        number = words[0].split('-')
        counter = 0
        for l in words[2]:
            if l == words[1][0]:
                counter = counter + 1 
        if counter >= int(number[0]) and counter <= int(number[1]):
            rowcounter = rowcounter + 1
    print(rowcounter)

def Part2():
    rowcounter = 0
    f = open("input.txt","r")
    lines = f.readlines() 
    for i in lines:
        words = i.split()
        samerow = False
        number = words[0].split('-')
        for l in range(len(words[2])):
            if words[2][l] == words[1][0] and (l+1 == int(number[0]) or l+1 == int(number[1])):
                if samerow == True:
                    rowcounter = rowcounter - 1
                    break
                samerow = True
                rowcounter = rowcounter + 1
    print(rowcounter)

Part2()