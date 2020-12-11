import copy 
def rec(inputlist,occupied):
    newlist = copy.deepcopy(inputlist)
    for i in range(len(inputlist)):
        for j in range(len(inputlist[i])):
            if inputlist[i][j] == "L":
                test = False
                if i > 0 and inputlist[i-1][j] == "#":
                    test = True
                if i > 0 and j > 0 and inputlist[i-1][j-1] == "#":
                    test = True
                if j > 0 and inputlist[i][j-1] == "#":
                    test = True
                if i < len(inputlist)-1 and j > 0 and inputlist[i+1][j-1] == "#":
                    test = True
                if i < len(inputlist)-1 and inputlist[i+1][j] == "#":
                    test = True
                if i < len(inputlist)-1 and j < len(inputlist[i])-1 and inputlist[i+1][j+1] == "#":
                    test = True
                if j < len(inputlist[i])-1 and inputlist[i][j+1] == "#":
                    test = True
                if i > 0 and j < len(inputlist[i])-1 and inputlist[i-1][j+1] == "#":
                    test = True
                if test == False:
                    newlist[i][j] = "#"
    inputlist = copy.deepcopy(newlist)
    for i in range(len(inputlist)):
        for j in range(len(inputlist[i])):
            if inputlist[i][j] == "#":
                test = 0
                if i > 0 and inputlist[i-1][j] == "#":
                    test += 1
                if i > 0 and j > 0 and inputlist[i-1][j-1] == "#":
                    test += 1
                if j > 0 and inputlist[i][j-1] == "#":
                    test += 1
                if i < len(inputlist)-1 and j > 0 and inputlist[i+1][j-1] == "#":
                    test += 1
                if i < len(inputlist)-1 and inputlist[i+1][j] == "#":
                    test += 1
                if i < len(inputlist)-1 and j < len(inputlist[i])-1 and inputlist[i+1][j+1] == "#":
                    test += 1
                if j < len(inputlist[i])-1 and inputlist[i][j+1] == "#":
                    test += 1
                if i > 0 and j < len(inputlist[i])-1 and inputlist[i-1][j+1] == "#":
                    test += 1
                if test >= 4:
                    newlist[i][j] = "L"
    counter = 0
    for i in range(len(inputlist)):
        for j in range(len(inputlist[i])):
            if newlist[i][j] == "#":
                counter += 1
    if counter == occupied:
        return newlist, counter
    return rec(newlist, counter)

def Part1():
    f = open("input.txt","r")
    inputlist = f.readlines()
    for i in range(len(inputlist)):
        inputlist[i] = inputlist[i].replace("\n","")
        inputlist[i] = [c for c in inputlist[i]]
    print(rec(inputlist,0)[1])

import time
start_time = time.time()
Part1()
print("--- %s seconds ---" % (time.time() - start_time))

