
def Part1():
    f = open("input.txt","r")
    inputlist = [int(i) for i in f.readlines()]
    start = 25
    for i in range(start,len(inputlist)):
        newlist = inputlist[i-start:i].copy()
        found = False
        for j in range(len(newlist)):
            for k in range(len(newlist)):
                if j != k and newlist[j]+newlist[k] == inputlist[i]:
                    found = True
            if found == True:
                break
        if found == False:
            return inputlist[i]
    return -1

def Part2(input):
    f = open("input.txt","r")
    inputlist = [int(i) for i in f.readlines()]
    for i in range(len(inputlist)):
        counter = inputlist[i]
        for j in range(i+1,len(inputlist)):
            if counter+inputlist[j] == input:
                newlist = inputlist[i:j].copy()
                return max(newlist)+min(newlist)
            elif counter+inputlist[j] > input:
                break
            else:
                counter += inputlist[j]
    return -1

import time
start_time = time.time()
output = Part1()
print("Number:"+str(output))
print(Part2(output))
print("--- %s seconds ---" % (time.time() - start_time))