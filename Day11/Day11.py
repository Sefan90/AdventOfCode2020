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

def rec2(inputlist,occupied):
    newlist = copy.deepcopy(inputlist)
    for i in range(len(inputlist)):
        for j in range(len(inputlist[i])):
            if inputlist[i][j] == "L":
                checked = ["."]*8
                for k in range(1,len(inputlist)):
                    test = ["."]*8
                    if i-k >= 0:
                        test[0] = inputlist[i-k][j] 
                    if i-k >= 0 and j-k >= 0:
                        test[1] = inputlist[i-k][j-k] 
                    if j-k >= 0:
                        test[2] = inputlist[i][j-k]
                    if i < len(inputlist)-k and j-k >= 0:
                        test[3] = inputlist[i+k][j-k] 
                    if i < len(inputlist)-k:
                        test[4] = inputlist[i+k][j] 
                    if i < len(inputlist)-k and j < len(inputlist[i])-k:
                        test[5] = inputlist[i+k][j+k] 
                    if j < len(inputlist[i])-k:
                        test[6] = inputlist[i][j+k]
                    if i-k >= 0 and j < len(inputlist[i])-k:
                        test[7] = inputlist[i-k][j+k] 
                    for m in range(len(checked)):
                        if checked[m] == "." and test[m] != ".":
                            checked[m] = test[m]
                    if "#" in checked or "." not in checked:
                        break
                if "#" not in checked:
                    newlist[i][j] = "#"
    inputlist = copy.deepcopy(newlist)

    for i in range(len(inputlist)):
        for j in range(len(inputlist[i])):
            if inputlist[i][j] == "#":
                checked = ["."]*8
                for k in range(1,len(inputlist)):
                    test = ["."]*8
                    if i-k >= 0:
                        test[0] = inputlist[i-k][j] 
                    if i-k >= 0 and j-k >= 0:
                        test[1] = inputlist[i-k][j-k] 
                    if j-k >= 0:
                        test[2] = inputlist[i][j-k]
                    if i < len(inputlist)-k and j-k >= 0:
                        test[3] = inputlist[i+k][j-k] 
                    if i < len(inputlist)-k:
                        test[4] = inputlist[i+k][j] 
                    if i < len(inputlist)-k and j < len(inputlist[i])-k:
                        test[5] = inputlist[i+k][j+k] 
                    if j < len(inputlist[i])-k:
                        test[6] = inputlist[i][j+k]
                    if i-k >= 0 and j < len(inputlist[i])-k:
                        test[7] = inputlist[i-k][j+k]
                    for m in range(len(checked)):
                        if checked[m] == "." and test[m] != ".":
                            checked[m] = test[m]
                    if "." not in checked:
                        break
                if checked.count("#") >= 5:
                    newlist[i][j] = "L"
    counter = 0
    for i in range(len(inputlist)):
        for j in range(len(inputlist[i])):
            if newlist[i][j] == "#":
                counter += 1
    if counter == occupied:
        return newlist, counter
    return rec2(newlist, counter)

def Part2():
    f = open("input.txt","r")
    inputlist = f.readlines()
    for i in range(len(inputlist)):
        inputlist[i] = inputlist[i].replace("\n","")
        inputlist[i] = [c for c in inputlist[i]]
    print(rec2(inputlist,0)[1])

import time
start_time = time.time()
Part2()
print("--- %s seconds ---" % (time.time() - start_time))

